#!/usr/bin/env python3

import sys
import csv
import json
import os.path
import argparse
import logging
import logging.config
import time
import re
from math import ceil

from secret import username, secret
import yaml
import requests

class ObjectNotFound(Exception):
    pass

class TooManyResults(Exception):
    pass

class NoLastExecutionFound(Exception):
    pass

class ActionFailure(Exception):
    pass

class AuthenticationFailure(Exception):
    pass

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

#Static vars
tower_url = 'http://192.168.2.129:8052'
#tower_url = 'http://192.168.2.128'
api_url = tower_url + '/api/v2/'
here = os.path.dirname(__file__)
yaml_launch_folder = os.path.join(here, 'yaml_launch')
MAX_CONCURRENT_JOBS = 3
COOLDOWN = 90

# return absolute path for file.
def absoluteFilePaths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

# delete double entries in list
def skip_duplicates(iterable, key=lambda x: x):
    fingerprints = set()
    for x in iterable:
        fingerprint = key(x)
        if fingerprint not in fingerprints:
            yield x
            fingerprints.add(fingerprint)

#Authentication
def authentication(username, password):
    url = tower_url + '/api/login/'
    session = requests.session()
    r = session.get(url)
    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise AuthenticationFailure("%d : Authentication Failed : %s" % (r.status_code, r.text))

    headers = {'Referer':url}
    csrf_token = r.cookies['csrftoken']
    payload = {'csrfmiddlewaretoken':csrf_token, 'next':'/api/', 'username':username, 'password':password}
    r = session.post(url, headers=headers, data=payload)
    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise AuthenticationFailure("%d : Authentication Failed : %s" % (r.status_code, r.text))
    return session

#Search one host and return its id
def return_host_id(session, fqdn):
    url = api_url + 'hosts/'
    payload = {'name':fqdn}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search host %s" % (r.status_code, fqdn))

    search_response = json.loads(r.text)
    count = search_response['count']

    if not count:
        raise ObjectNotFound("Host %s doesn't exist" % (fqdn))
    elif count > 1:
        raise TooManyResults("The search return %d results, this isn't something we want", count)
    else:
        host_id = search_response['results'][0]['id']

    logging.debug("Host id: %d", host_id)
    return host_id

#Search one group from inventory and return its id
def return_group_id(session, group_name, inventory_name):
    return_inventory_id(session, inventory_name)

    url = api_url + 'groups/'
    payload = {'name':group_name}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search group %s" % (r.status_code, group_name))

    search_response = json.loads(r.text)
    if not search_response['count']:
        raise ObjectNotFound("Group %s doesn't exist" % (group_name))
    else:
        for result in search_response['results']:
            if result['summary_fields']['inventory']['name'] == inventory_name:
                group_id = result['id']
                break
        else:
            raise ObjectNotFound("Group %s doesn't exist in inventory '%s'" % (group_name, inventory_name))

    logging.debug("Group id: %d", group_id)
    return group_id

#Search one project and return its id
def return_project_id(session, project_name):
    url = api_url + 'projects/'
    payload = {'name':project_name}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search project %s" % (r.status_code, project_name))

    search_response = json.loads(r.text)
    if not search_response['count']:
        raise ObjectNotFound("Project %s doesn't exist" % (project_name))
    else:
        project_id = search_response['results'][0]['id']

    logging.debug("Project id: %d", project_id)
    return project_id

#Search one group from inventory and return its name
def return_group_name(session, group_id):
    url = api_url + 'groups/'
    payload = {'id':group_id}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search group %d" % (r.status_code, group_id))

    search_response = json.loads(r.text)
    if not search_response['count']:
        raise ObjectNotFound("Group %d doesn't exist" % (group_id))
    else:
        group_name = search_response['results'][0]['name']

    logging.debug("Group name: %s", group_name)
    return group_name

#Search one inventory and return its id
def return_inventory_id(session, inventory_name):
    url = api_url + 'inventories/'
    payload = {'name':inventory_name}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search inventory %s" % (r.status_code, inventory_name))

    search_response = json.loads(r.text)
    count = search_response['count']

    if not count:
        raise ObjectNotFound("Inventory %s doesn't exist" % (inventory_name))
    else:
        inventory_id = search_response['results'][0]['id']

    logging.debug("Inventory id: %d", inventory_id)
    return inventory_id

#Search one job_template and return its id
def return_job_template_id(session, job_template_name):
    url = api_url + 'job_templates/'
    payload = {'name':job_template_name}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search job template '%s'" % (r.status_code, job_template_name))

    search_response = json.loads(r.text)
    count = search_response['count']

    if not count:
        raise ObjectNotFound("Job template '%s' doesn't exist" % (job_template_name))
    else:
        job_template_id = search_response['results'][0]['id']

    logging.debug("Job template id: %d", job_template_id)
    return job_template_id

#Search one organization and return its id
def return_organization_id(session, organization_name):
    url = api_url + 'organizations/'
    payload = {'name':organization_name}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search organization %s" % (r.status_code, organization_name))

    search_response = json.loads(r.text)
    count = search_response['count']

    if not count:
        raise ObjectNotFound("Organization %s doesn't exist" % (organization_name))
    else:
        organization_id = search_response['results'][0]['id']

    logging.debug("Organization id: %d", organization_id)
    return organization_id

#Search a group id and return the name of its inventory
def return_inventory_name_from_group(session, group_id):
    url = api_url + 'groups/'
    payload = {'id':group_id}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search inventory of group number %d" % (r.status_code, group_id))

    search_response = json.loads(r.text)
    if not search_response['count']:
        raise ObjectNotFound("Group %d doesn't exist" % (group_id))
    else:
        inventory_name = search_response['results'][0]['summary_fields']['inventory']['name']

    logging.debug("Inventory name: %s", inventory_name)
    return inventory_name

#Search an inventory id and return its name
def return_inventory_name(session, inventory_id):
    url = api_url + 'inventories/' + str(inventory_id)
    r = session.get(url)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search inventory %d" % (r.status_code, inventory_id))

    search_response = json.loads(r.text)
    inventory_name = search_response['name']

    logging.debug("Inventory name: %s", inventory_name)
    return inventory_name

#Search one credential and return its id
def return_credential_id(session, user_name):
    url = api_url + 'credentials/'
    payload = {'name':user_name}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search user %s" % (r.status_code, user_name))

    search_response = json.loads(r.text)
    count = search_response['count']

    if not count:
        raise ObjectNotFound("User " + user_name + " doesn't exist")
    else:
        credential_id = search_response['results'][0]['id']

    logging.debug("Credential id: %d", credential_id)
    return credential_id

#Search one job template and return its name
def return_job_template_name(session, job_template_id):
    url = api_url + 'job_templates/' + str(job_template_id) + '/'
    r = session.get(url)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code == 404):
        raise ObjectNotFound("%d : Job template %d doesn't exist" % (r.status_code, job_template_id))
    else:
        if (r.status_code != requests.codes.ok):
            raise ObjectNotFound("%d : Failed to search job template %d" % (r.status_code, job_template_id))

    search_response = json.loads(r.text)
    job_template_name = search_response['name']

    logging.debug("Job Template name: %s", job_template_name)
    return job_template_name

#Search one project and return its name
def return_project_name(session, project_id):
    url = api_url + 'projects/'
    payload = {'id':project_id}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search project %d" % (r.status_code, project_id))

    search_response = json.loads(r.text)
    if not search_response['count']:
        raise ObjectNotFound("Project %d doesn't exist" % (project_id))
    else:
        project_name = search_response['results'][0]['name']

    logging.debug("Project name: %s", project_name)
    return project_name

#Return a json dump of all something
def return_all(session, search, custom=""):
    url = api_url + search + '/'
    if custom:
        payload = {'order_by':'id', 'page_size':'200', custom['key']:custom['value']}
    else:
        payload = {'order_by':'id', 'page_size':'200'}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ActionFailure("%d : Failed to search all %s : %s" % (r.status_code, search, r.text))

    result = json.loads(r.text)
    nb_search = result['count']
    logging.debug("Tower inventory contains %d %s", nb_search, search)

    full_list = result['results']
    if nb_search > 200:
        page = ceil(nb_search / 200)
        for i in range(2, page+1):
            payload = {'order_by':'id', 'page_size':'200', 'page':i}
            r2 = session.get(url, params=payload)
            logging.debug("%s %s", r.request.method, r.url)
            full_list = full_list + json.loads(r2.text)['results']
        logging.debug("Function 'return_all' found %d %s in %d page(s)", len(full_list), search, page)

    return full_list

#Add one host to inventory
def add_host(session, fqdn, inventory_name, delete=False, variables=''):
    inventory_id = return_inventory_id(session, inventory_name)
    try:
        if delete:
            delete_host(session, fqdn)
        host_id = return_host_id(session, fqdn)
        logging.error("The host %s already exist in %s with ID %d", fqdn, inventory_name, host_id)
    except ObjectNotFound:
        url = api_url + 'hosts/'
        payload = {'name':fqdn, 'inventory':inventory_id, 'variables':variables}
        r = session.post(url, json=payload)

        logging.info("%s %s", r.request.method, r.url)
        if (r.status_code != 201):
            raise ActionFailure("%d : Failed to add host %s %s" % (r.status_code, fqdn, r.text))

        search_response = json.loads(r.text)
        host_id = search_response['id']

        logging.info("Host %s added with ID %s", fqdn, host_id)
    return host_id

#Add one group to inventory
def add_group(session, group_name, inventory_name, delete=False):
    inventory_id = return_inventory_id(session, inventory_name)
    try:
        if delete:
            delete_group(session, group_name, inventory_name)
        group_id = return_group_id(session, group_name, inventory_name)
        logging.error("The group %s already exist in %s with ID %d", group_name, inventory_name, group_id)
    except ObjectNotFound:
        url = api_url + 'groups/'
        payload = {'name':group_name, 'inventory':inventory_id}
        r = session.post(url, json=payload)

        logging.info("%s %s", r.request.method, r.url)
        if (r.status_code != 201):
            raise ActionFailure("%d : Failed to add group %s %s" % (r.status_code, group_name, r.text))

        search_response = json.loads(r.text)
        group_id = search_response['id']

        logging.info("Group %s added with ID %s", group_name, group_id)
    return group_id

#Import all hosts listed in txtfile
def mass_import_host(session, txtfile):
    with open(txtfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in reader:
            add_host(session, row[0], row[1])
            count = count + 1
    logging.info("%d host(s) imported", count)

#Enable or disable one host
def change_host_status(session, fqdn, status):
    try:
        host_id = return_host_id(session, fqdn)
        url = api_url + 'hosts/' + str(host_id) + '/'
        payload = {'name':fqdn, 'enabled':status}
        r = session.patch(url, json=payload)

        logging.info("%s %s", r.request.method, r.url)
        if (r.status_code != requests.codes.ok):
            raise ActionFailure("%d : Failed to update host status %s %s" % (r.status_code, fqdn, r.text))

        search_response = json.loads(r.text)
        host_id = search_response['id']

        if status == "True" or status == "true":
            modification = "enabled"
        else:
            modification = "disabled"

        logging.info("Host %s with ID %d has been %s", fqdn, host_id, modification)
        return host_id
    except ObjectNotFound:
        logging.error("The host %s doesn't exist", fqdn)

#Change status of all hosts listed in txtfile
def mass_change_host_status(session, txtfile):
    with open(txtfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in reader:
            change_host_status(session, row[0], row[1])
            count = count + 1
    logging.info("%d host(s) updated", count)

#Remove one host from inventory
def delete_host(session, fqdn):
    host_id = return_host_id(session, fqdn)

    url = api_url + 'hosts/' + str(host_id) + '/'
    r = session.delete(url)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to remove host %s %s" % (r.status_code, fqdn, r.text))

    logging.info("Host %s deleted", fqdn)
    return host_id

#Remove one group from inventory
def delete_group(session, group_name, inventory):
    group_id = return_group_id(session, group_name, inventory)

    url = api_url + 'groups/' + str(group_id) + '/'
    r = session.delete(url)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to remove group %s %s" % (r.status_code, group_name, r.text))

    logging.info("Group %s deleted", group_name)
    return group_id

#Remove one project
def delete_project(session, project_name):
    project_id = return_project_id(session, project_name)

    url = api_url + 'projects/' + str(project_id) + '/'
    r = session.delete(url)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to remove project %s %s" % (r.status_code, project_name, r.text))

    logging.info("Project %s deleted", project_name)
    return project_id

#Remove all hosts listed in txtfile
def mass_delete_host(session, txtfile):
    with open(txtfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in reader:
            delete_host(session, row[0])
            count = count + 1
    logging.info("%d host(s) removed", count)

#Add one host to a group in inventory
def associate_to_group(session, fqdn, group_name, inventory_name):
    host_id = return_host_id(session, fqdn)
    return_inventory_id(session, inventory_name)
    group_id = return_group_id(session, group_name, inventory_name)

    url = api_url + 'hosts/' + str(host_id) + '/groups/'
    payload = {'associate':True, 'id':group_id}
    r = session.post(url, json=payload)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to add host %s  to group %s %s" % (r.status_code, fqdn, group_name, r.text))

    logging.info("%s added to %s in %s", fqdn, group_name, inventory_name)

# associate variable to group
def associate_variable(session, type_var, name, key, value, inventory_name):
    if type_var == "groups":
        id_var = return_group_id(session, name, inventory_name)
    elif type_var == "hosts":
        id_var = return_host_id(session, name)
    else:
        raise ActionFailure("Failed to add variable '%s : %s' to %s '%s' : Type not found (groups or hosts)."
                % (key, value, type_var, name))
    url = api_url + type_var +'/' + str(id_var) + '/variable_data/'
    r = session.get(url)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ActionFailure("%d : Failed to get variale for %s %d" % (r.status_code, type_var, id_var))

    data = json.loads(r.text)
    data[key] = value
    logging.debug(data)

    r = session.put(url, json=data)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 200):
        raise ActionFailure("%d : Failed to add variable '%s : %s' to %s '%s' : %s" %
                (r.status_code, key, value, type_var, name, r.text))

    logging.info("%s : %s added to %s in %s", key, value, name, inventory_name)

#Add one children to a group in inventory
def associate_children_to_group(session, group_parent_name, group_child_name, inventory_name):
    group_child_id = return_group_id(session, group_child_name, inventory_name)
    return_inventory_id(session, inventory_name)
    group_parent_id = return_group_id(session, group_parent_name, inventory_name)

    url = api_url + 'groups/' + str(group_parent_id) + '/children/'
    payload = {'associate':True, 'id':group_child_id}
    r = session.post(url, json=payload)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to add group (child) %s to group (parent) %s %s"
                % (r.status_code, group_child_name, group_parent_name, r.text))

    logging.info("%s added to %s in %s", group_child_name, group_parent_name, inventory_name)

#Associate every host with respective groups from txtfile
def mass_associate(session, txtfile):
    with open(txtfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in reader:
            associate_to_group(session, row[0], row[1], row[2])
            count = count + 1
    logging.info("%d host(s) associated", count)

#Remove one host from a group in inventory
def disassociate_from_group(session, fqdn, group_name, inventory_name):
    host_id = return_host_id(session, fqdn)
    return_inventory_id(session, inventory_name)
    group_id = return_group_id(session, group_name, inventory_name)

    url = api_url + 'hosts/' + str(host_id) + '/groups/'
    payload = {'disassociate':True, 'id':group_id}
    r = session.post(url, json=payload)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to remove host %s from group %s %s" % (r.status_code, fqdn, group_name, r.text))

    logging.info("%s removed from %s in %s", fqdn, group_name, inventory_name)

#Print all host's groups
def host_groups(session, fqdn, manual=True):
    host_id = return_host_id(session, fqdn)

    url = api_url + 'hosts/' + str(host_id) + '/all_groups/'
    payload = {'page_size':'100'}
    r = session.get(url, params=payload)

    if manual:
        logging.info("%s %s", r.request.method, r.url)

    if (r.status_code != requests.codes.ok):
        raise ActionFailure("%d : Failed to search all groups of host %s : %s" % (r.status_code, fqdn, r.text))

    host_groups_list = json.loads(r.text)

    if manual:
        if host_groups_list['count']:
            logging.info("Host %s (ID %d) has %d group(s):", fqdn, host_id, host_groups_list['count'])
            for result in host_groups_list['results']:
                logging.info("%s", result['name'])
        else:
            logging.error("Host %s (ID %d) has no group", fqdn, host_id)
    else:
        return host_groups_list['results']

#Return all hosts in inventory
def return_all_hosts_from_inventory(session, inventory_name):
    inventory_id = return_inventory_id(session, inventory_name)

    url = api_url + 'hosts/'
    payload = {'order_by':'id', 'inventory':inventory_id, 'page_size':'200'}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search first 200 hosts" % r.status_code)

    result = json.loads(r.text)
    nb_search = result['count']
    logging.debug("Tower inventory '%s' contains %d hosts", inventory_name, nb_search)

    full_list = result['results']
    if nb_search > 200:
        page = ceil(nb_search / 200)
        for i in range(2, page+1):
            payload = {'order_by':'id', 'inventory':inventory_id, 'page_size':'200', 'page':i}
            r2 = session.get(url, params=payload)
            logging.debug("%s %s", r.request.method, r.url)
            full_list = full_list + json.loads(r2.text)['results']
        logging.debug("Function 'return_all_hosts' found %d host(s) in inventory %s in %d page(s)",
                len(full_list), inventory_name, page)

    if nb_search:
        return full_list
    else:
        raise ObjectNotFound("Inventory %s is empty" % (inventory_name))

#Print all members of several groups
def groupList_members(session, inventory_name, inverse, grouplist):
    all_members = []
    for group_name in grouplist:
        group_id = return_group_id(session, group_name, inventory_name)

        url = api_url + 'groups/' + str(group_id) + '/hosts'
        payload = {'page_size':'200'}
        r = session.get(url, params=payload)

        logging.debug("%s %s", r.request.method, r.url)

        if (r.status_code != requests.codes.ok):
            raise ObjectNotFound("%d : Failed to search group members for %s %s" % (r.status_code, group_name, r.text))

        members = json.loads(r.text)
        if not members['count']:
            #TODO: Test children
            logging.info("Group %s (ID %d) in inventory '%s' has no member", group_name, group_id, inventory_name)
        else:
            logging.info("Group %s (ID %d) in inventory '%s' has %d member(s)", group_name, group_id, inventory_name, members['count'])
            all_members.extend(members['results'])

    if not len(all_members):
        logging.error("No host found in your group list in inventory '%s'", inventory_name)
        return 0
    else:
        if inverse:
            all_hosts_from_inventory = return_all_hosts_from_inventory(session, inventory_name)
            inverse_list = [item for item in all_hosts_from_inventory if item not in all_members]
            for member in inverse_list:
                logging.info("%s", member['name'])
            return len(inverse_list)
        else:
            for member in all_members:
                logging.info("%s", member['name'])
            return len(all_members)

#Print all group members in inventory and return their number
def group_members(session, group_name=None, inventory_name=None, export=False, group_id=None):
    manual = False
    if group_name is None:
        group_name = return_group_name(session, group_id)
    if inventory_name is None:
        inventory_name = return_inventory_name_from_group(session, group_id)
    if group_id is None:
        group_id = return_group_id(session, group_name, inventory_name)
        manual = True

    url = api_url + 'groups/' + str(group_id) + '/hosts'
    payload = {'page_size':'200'}
    r = session.get(url, params=payload)

    logging.debug("%s %s", r.request.method, r.url)

    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search group members for %s %s" % (r.status_code, group_name, r.text))

    members = json.loads(r.text)
    if not members['count']:
        #TODO: Test children
        logging.error("Group %s (ID %d) in inventory '%s' has no member", group_name, group_id, inventory_name)
        return 0
    else:
        if manual:
            logging.info("Group %s (ID %d) in inventory '%s' has %d member(s)", group_name, group_id, inventory_name, members['count'])
            for member in members['results']:
                logging.info("%s", member['name'])
        if export:
            with open('export_group_vars', 'w') as stream:
                for member in members['results']:
                    stream.write(member['name'] + "\n")
        return members['count']

#Print or return all group vars in inventory
def group_vars(session, group_name=None, inventory_name=None, group_id=None):
    manual = False
    if group_id is None:
        group_id = return_group_id(session, group_name, inventory_name)
        manual = True

    url = api_url + 'groups/' + str(group_id) + '/'
    r = session.get(url)

    if manual:
        logging.info("%s %s", r.request.method, r.url)

    if (r.status_code != requests.codes.ok):
        raise ObjectNotFound("%d : Failed to search group variables for %s %s" % (r.status_code, group_name, r.text))

    search_response = json.loads(r.text)
    gvars = re.sub('---\n', '', search_response['variables'])

    if manual:
        if gvars == '' or gvars == '{}':
            logging.error("Group %s (ID %d) has no var", group_name, group_id)
        else:
            logging.info('\n' + '='*15 + ' GROUP ' + group_name + ' ' + '='*15)
            logging.info("%s", gvars)
    else:
        if gvars == '' or gvars == '{}':
            return ""
        else:
            return gvars

#Return the last job template execution status
def last_execution_status(session, quiet, job_template_id):
    job_template_name = return_job_template_name(session, job_template_id)

    url = api_url + 'job_templates/' + str(job_template_id) + '/jobs/'
    payload = {'started__isnull':'False', 'order_by':'-started', 'page_size':'1'}
    r = session.get(url, params=payload)

    if not quiet:
        logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != requests.codes.ok):
        raise NoLastExecutionFound("Search of last execution status failed : status code %d" % (r.status_code))

    search_response = json.loads(r.text)
    if not search_response['count']:
        raise NoLastExecutionFound("No launch history for %s" % (job_template_name))

    status = search_response['results'][0]['status']
    job_id = search_response['results'][0]['id']

    logging.info("Last execution of '%s' was '%s' - Job ID : %d", job_template_name, status, job_id)
    return (status, job_id)

#Show if last job template execution change anything
def last_execution_change(session, quiet, job_template_id):
    status, job_id = last_execution_status(session, quiet, job_template_id)
    logging.info("Full output : %s/#/jobs/%d", tower_url, job_id)

    if (status != "successful"):
        logging.error("Last execution status was '%s' please relaunch the job", status)
        sys.exit(99)
    else:
        url = api_url + 'jobs/' + str(job_id) + '/job_events/'
        payload = {'changed':'true', 'page_size':'200'}
        r = session.get(url, params=payload)

        if not quiet:
            logging.info("%s %s", r.request.method, r.url)
        if (r.status_code != requests.codes.ok):
            raise NoLastExecutionFound("Search of last execution change failed : status code %d" % (r.status_code))

        search_response = json.loads(r.text)
        count = 0
        for result in search_response['results']:
            if result['event_level'] == 3:
                count += 1
                logging.info("%d : %s : %s", result['id'], result['event_data']['task'], result['event_data']['host'])
        logging.info("%d task(s) have a 'changed' status in job ID %d ", count, job_id)
        sys.exit(count)

#Print all vars in all tower groups
def all_group_vars(session):
    groups = return_all(session, 'groups')

    #for idx, group in enumerate(groups['results']):
    for group in groups:
        group_id = group['id']
        group_name = group['name']
        group_inventory = group['summary_fields']['inventory']['name']

        variables = group_vars(session, group_id=group_id)

        if variables != '{}' and variables != '':
            logging.info("%d/%s/%s : %s", group_id, group_inventory, group_name, variables)
        #if idx == 5:
        #    break

#Print all vars in all hosts
def all_host_vars(session):
    hosts = return_all(session, 'hosts')

    for result in hosts:
        host_id = result['id']
        host_name = result['name']
        host_inventory = result['summary_fields']['inventory']['name']

        url = api_url + 'hosts/' + str(host_id) + '/variable_data/'
        r = session.get(url)

        logging.debug("%s %s", r.request.method, r.url)
        if (r.status_code != requests.codes.ok):
            raise ActionFailure("%d : Failed to search all vars of host %s : %s" % (r.status_code, host_name, r.text))

        if r.text != '{}' and r.text != '':
            variables = json.loads(r.text)
            logging.info("%d/%s/%s : %s", host_id, host_inventory, host_name, str(variables))

#Print all hosts that aren't in any group
def all_lonely_hosts(session):
    hosts = return_all(session, 'hosts')

    for host in hosts:
        host_id = host['id']
        host_name = host['name']
        host_inventory = host['summary_fields']['inventory']['name']

        url = api_url + 'hosts/' + str(host_id) + '/all_groups/'
        r = session.get(url)

        logging.debug("%s %s", r.request.method, r.url)
        if (r.status_code != requests.codes.ok):
            raise ActionFailure("%d : Failed to search all groups of host %s : %s" % (r.status_code, host_name, r.text))

        host_groups_list = json.loads(r.text)

        if not host_groups_list['count']:
            logging.error("Host %s (ID %d) in inventory '%s' has no group", host_name, host_id, host_inventory)

#Print all groups that don't have any member
def all_lonely_groups(session):
    groups = return_all(session, 'groups')

    count = 0
    for group in groups:
        group_nb_member = group_members(session, group_id=group['id'])

        if not group_nb_member:
            count += 1
    logging.info("There is %d lonely group(s)", count)

#Print all templates not using Default project
def all_not_default_project(session):
    templates = return_all(session, 'job_templates')

    count = 0
    for template in templates:
        try:
            project_id = int(template['related']['project'].split('/')[-2])
            if project_id not in [6, 7, 12, 16]:
                project_name = return_project_name(session, project_id)
                logging.info("(id:{:5d}) {:60s} is using (id:{:5d}) {:30s}".format(
                    template['id'], template['name'], project_id, project_name))
                count += 1
        except KeyError:
            logging.info("(id:{:5d}) {:60s} is NOT using ANY project".format(template['id'], template['name']))
            count += 1
    logging.info("There is %d template(s) using non default projects", count)

def all_projects_with_old_branch(session):
    projects = return_all(session, 'projects')
    count = 0
    with open("%s" % ('branchList'), 'r') as stream:
        branchList = stream.read().splitlines()
    sortedProjects = sorted(projects, key=lambda k: k['name'])

    for project in sortedProjects:
        if project['scm_url'] == 'git@gitlab.example.com:infra/ansible.git' and project['scm_branch']:
            if project['scm_branch'] not in branchList:
                count += 1
                logging.info("Project {:30s} is using not existing branch {:30s}".format(project['name'], project['scm_branch']))
    logging.info("There is %d project(s) using obsolete branch", count)

#Print all job templates using surveys
def all_templates_with_survey(session):
    templates = return_all(session, 'job_templates')

    count = 0
    for template in templates:
        if template['survey_enabled']:
            logging.info("%d : %s", template['id'], template['name'])
            count += 1
    logging.info("There is %d template(s) with survey", count)

# Print host variables
def host_vars(session, fqdn, nested=False):
    host_id = return_host_id(session, fqdn)

    url = api_url + 'hosts/' + str(host_id)
    r = session.get(url)

    logging.debug("%s %s", r.request.method, r.url)

    if (r.status_code != requests.codes.ok):
        raise ActionFailure("%d : Failed to search host vars for %s : %s" % (r.status_code, fqdn, r.text))

    search_response = json.loads(r.text)
    hvars = search_response['variables']

    if hvars == '' or hvars == '{}':
        logging.error("Host %s (ID %d) has no var", fqdn, host_id)
    else:
        logging.info('\n' + '='*15 + ' HOST ' + fqdn + ' ' + '='*15)
        logging.info(re.sub('---\n', '', hvars))

    if nested:
        group_list = host_groups(session, fqdn, False)
        for group in group_list:
            inventory_name = return_inventory_name(session, search_response['inventory'])
            group_id = return_group_id(session, group['name'], inventory_name)
            gvars = group_vars(session, group['name'], inventory_name, group_id)
            if gvars:
                logging.info('\n' + '='*15 + ' GROUP ' + group['name'] + ' ' + '='*15)
                logging.info(gvars)

# Cancel a job in progress
def stop_job(session, job_id):
    url = api_url + 'jobs/' + str(job_id) + '/cancel/'
    json_payload = {'can_cancel': 'false'}
    r = session.post(url, json=json_payload)
    logging.info("%s %s", r.request.method, r.url)

    if (r.status_code != 202):
        raise ActionFailure("%d : Failed to stop Job %s : %s" % (r.status_code, job_id, r.text))

    logging.info("Stop successful : %s", job_id)

def launch_job(session, login, password, jsonfile, tags, inventory, limit, si_version, job_type, disable_cooldown, returnId=False):
    global MAX_CONCURRENT_JOBS # pylint: disable=global-statement
    with open("%s/%s.yaml" % (yaml_launch_folder, jsonfile), 'r') as stream:
        exec_settings = yaml.load(stream)

    if disable_cooldown:
        MAX_CONCURRENT_JOBS = 50

    launchCount = 0
    for job_template_id in exec_settings['job_template_id']:
        launchCount += 1
        if launchCount > MAX_CONCURRENT_JOBS:
            logging.info("%d jobs are now running, waiting %d seconds for performance saving", MAX_CONCURRENT_JOBS, COOLDOWN)
            time.sleep(COOLDOWN)
            launchCount = 1
        url = api_url + 'job_templates/' + str(job_template_id) + '/launch/'
        r = session.get(url)

        logging.debug("%s %s", r.request.method, r.url)
        if (r.status_code != requests.codes.ok):
            raise ActionFailure("%d : Failed to launch Job Template %d" % (r.status_code, job_template_id))

        prelaunch_result = json.loads(r.text)
        logging.debug(prelaunch_result)
        for variable in prelaunch_result['variables_needed_to_start']:
            if variable not in exec_settings['survey']:
                raise ActionFailure("Failed to launch Job Template %d : Missing mandatory var %s" % (job_template_id, variable))

        #extra_vars = yaml.load(prelaunch_result['defaults']['extra_vars'])
        extra_vars = {}
        try:
            if exec_settings['survey']:
                for k, v in exec_settings['survey'].items():
                    extra_vars[k] = v
        except KeyError:
            pass

        credential_id = return_credential_id(session, login)
        json_payload = {'credential': credential_id,
                'ssh_password': password,
                'ssh_key_unlock': password,
                'become_password': password,
                'extra_vars':extra_vars
        }
        if tags:
            json_payload['job_tags'] = tags
        if inventory:
            json_payload['inventory'] = inventory
        if limit:
            json_payload['limit'] = limit
        elif 'limit' in exec_settings:
            json_payload['limit'] = exec_settings['limit']
        if si_version:
            json_payload['extra_vars']['si_version'] = si_version
        if job_type:
            json_payload['job_type'] = job_type
        elif 'job_type' in exec_settings:
            json_payload['job_type'] = exec_settings['job_type']

        logging.debug(json_payload)

        r = session.post(url, json=json_payload)
        logging.info("%s %s", r.request.method, r.url)
        if (r.status_code != 201):
            raise ActionFailure("%d : Failed to launch Job Template %d : %s" % (r.status_code, job_template_id, r.text))

        launch_result = json.loads(r.text)
        logging.info("Launch successful : %s/#/jobs/%d", tower_url, launch_result['id'])
        logging.debug(launch_result)
        if returnId:
            logging.info("IDJOB:%s", launch_result['id'])

# Function to import ansible inventory
def import_ansible_inventory(session, filename, inventory, organization='Default',
        export_host_file=False, group_var_directory_path=None, host_var_directory_path=None):
    add_inventory(session, inventory, organization, False)
    with open(filename, 'r') as stream:
        groupChildren = group = None
        list_hosts = []
        for line in stream.readlines():
            line = line.replace('\n', '')
            if line and not line.isspace():
                if line[0] == '[':
                    if ':children' in line:
                        groupChildren = line.replace(':children', '')
                        groupChildren = groupChildren[1:-1]
                        add_group(session, groupChildren, inventory)
                        if group is not None:
                            group = None
                    else:
                        group = line
                        group = group[1:-1]
                        add_group(session, group, inventory)
                        if groupChildren is not None:
                            groupChildren = None
                elif 'ip' in line and '#' not in line and groupChildren is None and group is None:
                    if 'ansible_host' in line:
                        line = line.split()
                        fqdn = str(line[1].replace('ansible_host=', ''))
                        del line[1], line[0]
                    else:
                        line = line.split()
                        fqdn = str(line[0])
                        del line[0]
                    list_hosts.append(fqdn)
                    variables = '\n'.join(line)
                    variables = variables.replace('=', ': ')
                    add_host(session, fqdn, inventory, True, variables)
                elif groupChildren != None:
                    associate_children_to_group(session, groupChildren, line, inventory)
                elif group != None:
                    for host in list_hosts:
                        if line in host:
                            associate_to_group(session, host, group, inventory)
    if group_var_directory_path != None:
        browse_yaml_inventory(session, 'groups', group_var_directory_path, inventory)
    if host_var_directory_path != None:
        browse_yaml_inventory(session, 'hosts', host_var_directory_path, inventory)
    if export_host_file:
        list_hosts = list(skip_duplicates(list_hosts))
        with open('export_host_list', 'w') as stream:
            for host in list_hosts:
                stream.write(host + '\n')

# Function to export ansible inventory
def export_ansible_inventory(session, jsonfile, inventory_name, bash=False):
    inventory_id = return_inventory_id(session, inventory_name)

    url = api_url + 'inventories/' + str(inventory_id) + '/script'
    payload = {'hostvars':'1', 'all':'1'}
    r = session.get(url, params=payload)
    export_result = json.loads(r.text)
    logging.debug(export_result)
    with open(jsonfile, 'w') as stream:
        if bash:
            stream.writelines(['#!/bin/bash\n',
                'if [ "$1" == "--list" ] ; then\n',
                'cat << "EOF"\n'])
        stream.write(r.text)
        if bash:
            stream.writelines(['\nEOF\n',
                'elif [ "$1" == "--host" ]; then\n',
                '  echo \'{"_meta": {"hostvars": {}}}\'\n',
                'else\n',
                '  echo "{ }"\n',
                'fi\n'])
    logging.info("Inventory '%s' exported into %s file", inventory_name, jsonfile)

#Add one schedule
def add_schedule(session, job_template_id, payload):
    url = api_url + 'job_templates/' + str(job_template_id) + '/schedules/'
    r = session.post(url, json=payload)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 201):
        raise ActionFailure(">>> %d : Failed to add schedule %s %s" % (r.status_code, payload['name'], r.text))

    result = json.loads(r.text)
    schedule_id = result['id']

    logging.info("Schedule '%s' added with ID %s", payload['name'], schedule_id)
    return schedule_id

#Add one job_template
def add_job_template(session, data):
    url = api_url + 'job_templates/'
    payload = {'name':data['name'],
            'description':data['description'],
            'job_type':data['job_type'],
            'inventory':data['inventory'],
            'project':data['project'],
            'playbook':data['playbook'],
            'credential':data['credential'],
            'vault_credential':data['vault_credential'],
            'forks':data['forks'],
            'limit':data['limit'],
            'verbosity':data['verbosity'],
            'extra_vars':data['extra_vars'],
            'job_tags':data['job_tags'],
            'force_handlers':data['force_handlers'],
            'skip_tags':data['skip_tags'],
            'start_at_task':data['start_at_task'],
            'timeout':data['timeout'],
            'use_fact_cache':data['use_fact_cache'],
            'host_config_key':data['host_config_key'],
            'ask_diff_mode_on_launch':data['ask_diff_mode_on_launch'],
            'ask_variables_on_launch':data['ask_variables_on_launch'],
            'ask_limit_on_launch':data['ask_limit_on_launch'],
            'ask_tags_on_launch':data['ask_tags_on_launch'],
            'ask_skip_tags_on_launch':data['ask_skip_tags_on_launch'],
            'ask_job_type_on_launch':data['ask_job_type_on_launch'],
            'ask_verbosity_on_launch':data['ask_verbosity_on_launch'],
            'ask_inventory_on_launch':data['ask_inventory_on_launch'],
            'ask_credential_on_launch':data['ask_credential_on_launch'],
            'survey_enabled':data['survey_enabled'],
            'become_enabled':data['become_enabled'],
            'diff_mode':data['diff_mode'],
            'allow_simultaneous':data['allow_simultaneous']}

    r = session.post(url, json=payload)
    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != 201):
        if r.status_code == 400 and "already exists" in r.text:
            logging.info("Job Template '%s' already exist", data['name'])
            return -1
        if r.status_code == 400 and "Playbook not found for project" in r.text:
            logging.info(">>> %d : Failed to add job template '%s': Playbook not found for project", r.status_code, data['name'])
            return -1
        raise ActionFailure(">>> %d : Failed to add job template '%s': %s" % (r.status_code, data['name'], r.text))
    response = json.loads(r.text)
    logging.debug(response)

    job_template_id = response['id']
    logging.info("Job template '%s' added with ID %s", data['name'], job_template_id)

    if 'extra_credentials' in data:
        url = api_url + 'job_templates/' + str(job_template_id) + '/extra_credentials/'
        for cred_id in data['extra_credentials']:
            payload = {'id':cred_id}
            r = session.post(url, json=payload)
            logging.info("%s %s", r.request.method, r.url)
            if (r.status_code != 204):
                raise ActionFailure(">>> %d : Failed to add extra credential to job template '%s': %s" %
                        (r.status_code, data['name'], r.text))
        logging.info("%d extra credential(s) added to job template '%s'", len(data['extra_credentials']), data['name'])

    if 'schedule' in data:
        for schedule in data['schedule']['results']:
            payload = {'name':schedule['name'],
                    'description':schedule['description'],
                    'enabled':schedule['enabled'],
                    'rrule':schedule['rrule'],
                    'extra_data':schedule['extra_data']}
            add_schedule(session, job_template_id, payload)
        logging.info("%d schedule(s) added to job template '%s'", data['schedule']['count'], data['name'])

    if 'survey' in data:
        url = api_url + 'job_templates/' + str(job_template_id) + '/survey_spec/'
        payload = {'name':data['survey']['name'],
                'description':data['survey']['description'],
                'spec':data['survey']['spec']}

        r = session.post(url, json=payload)
        logging.info("%s %s", r.request.method, r.url)
        if (r.status_code != requests.codes.ok):
            raise ActionFailure(">>> %d : Failed to add survey to job template '%s': %s" % (r.status_code, data['name'], r.text))
        logging.info("Survey added to job template '%s'", data['name'])

    return job_template_id

# Function to import job templates from file
def import_job_templates(session, jsonfile):
    with open(jsonfile, 'r') as stream:
        job_templates = json.loads(stream.read().replace('\n', ''))
    logging.info("%d job template(s) loaded from json file", len(job_templates))

    for job_template in job_templates:
        add_job_template(session, job_template)

    logging.info("All job templates successfully imported")

# Function to export all job templates
def export_all_job_templates(session, jsonfile):
    templates = return_all(session, 'job_templates')

    countJob = countSurvey = countSchedule = countExtraCredential = 0
    for template in templates:
        countJob += 1

        url = api_url + 'job_templates/' + str(template['id']) + '/extra_credentials/'
        r = session.get(url)
        logging.debug("%s %s", r.request.method, r.url)
        request_result = json.loads(r.text)
        logging.debug(request_result)
        if request_result['count']:
            countExtraCredential += 1
            cred_list = []
            for result in request_result['results']:
                cred_list.append(result['id'])
            template['extra_credentials'] = cred_list

        if template['survey_enabled']:
            countSurvey += 1
            url = api_url + 'job_templates/' + str(template['id']) + '/survey_spec/'
            r = session.get(url)
            logging.debug("%s %s", r.request.method, r.url)
            request_result = json.loads(r.text)
            logging.debug(request_result)
            template['survey'] = request_result

        if 'next_schedule' in template['related']:
            countSchedule += 1
            url = api_url + 'job_templates/' + str(template['id']) + '/schedules/'
            r = session.get(url)
            logging.debug("%s %s", r.request.method, r.url)
            request_result = json.loads(r.text)
            logging.debug(request_result)
            template['schedule'] = request_result

    with open(jsonfile, 'w') as stream:
        stream.write(json.dumps(templates))
    logging.info("All %d job templates have been exported, with %d surveys, %d schedules and %d extra_credential",
            countJob, countSurvey, countSchedule, countExtraCredential)

# Function to display credentials used by job templates
def display_job_templates_credentials(session):
    templates = return_all(session, 'job_templates')

    logging.info("name,id,machine,vault,extra")
    for template in templates:
        url = api_url + 'job_templates/' + str(template['id']) + '/extra_credentials/'
        r = session.get(url)
        logging.debug("%s %s", r.request.method, r.url)
        request_result = json.loads(r.text)
        logging.debug(request_result)
        if request_result['count']:
            cred_list = []
            for result in request_result['results']:
                cred_list.append(result['id'])
            template['extra_credentials'] = cred_list
        logging.info("%s,%d,%s,%s,%s", template['name'], template['id'],
                template['credential'], template['vault_credential'], str(template.get('extra_credentials')))

#Add one credential
def add_credential(session, data, delete=False):
    if data['organization'] is None:
        data['organization'] = return_organization_id(session, 'Default')

    if 'password' in data['inputs']:
        data['inputs']['password'] = 'ASK'
    if 'become_password' in data['inputs']:
        data['inputs']['become_password'] = 'ASK'
    if 'ssh_key_data' in data['inputs']:
        data['inputs']['ssh_key_data'] = ''
    if 'ssh_key_unlock' in data['inputs']:
        data['inputs']['ssh_key_unlock'] = ''
    if 'vault_password' in data['inputs']:
        data['inputs']['vault_password'] = 'password'

    url = api_url + 'credentials/'
    payload = {'name':data['name'],
            'description':data['description'],
            'organization':data['organization'],
            'credential_type':data['credential_type'],
            'inputs':data['inputs']}

    r = session.post(url, json=payload)
    logging.debug("%s %s", r.request.method, r.url)
    if (r.status_code != 201):
        if r.status_code == 400 and "already exists" in r.text:
            logging.info("Credential '%s' already exist in organization %s", data['name'], data['organization'])
            return -1
        raise ActionFailure("%d : Failed to add credential '%s': %s" % (r.status_code, data['name'], r.text))
    response = json.loads(r.text)
    logging.debug(response)

    credential_id = response['id']
    logging.info("Credential '%s' added with ID %s", data['name'], credential_id)

    return credential_id

#Add one project
def add_project(session, data, delete=False):
    url = api_url + 'projects/'
    payload = {'name':data['name'],
            'description':data['description'],
            'organization':data['organization'],
            'scm_type':data['scm_type'],
            'scm_url':data['scm_url'],
            'local_path':data['local_path'],
            'scm_branch':data['scm_branch'],
            'credential':data['credential'],
            'scm_clean':data['scm_clean'],
            'scm_delete_on_update':data['scm_delete_on_update'],
            'scm_update_on_launch':data['scm_update_on_launch'],
            'scm_update_cache_timeout':data['scm_update_cache_timeout'],
            'timeout':data['timeout']}

    r = session.post(url, json=payload)
    logging.info("%s %s", r.request.method, r.url)
    if r.status_code == 400 and "already exists" in r.text and delete:
        delete_project(session, data['name'])
        r = session.post(url, json=payload)
    if (r.status_code != 201):
        raise ActionFailure("%d : Failed to add project '%s': %s" % (r.status_code, data['name'], r.text))
    response = json.loads(r.text)
    logging.debug(response)

    project_id = response['id']
    logging.info("Project '%s' added with ID %s", data['name'], project_id)

    return project_id

# Function to import something from file
def import_all(session, jsonfile, object_type, delete=False):
    with open(jsonfile, 'r') as stream:
        results = json.loads(stream.read().replace('\n', ''))
    logging.info("%d %s loaded from json file", len(results), object_type)

    command = 'add_' + object_type[:-1]
    for result in results:
        globals()[command](session, result, delete)

    logging.info("All %s successfully imported", object_type)

# Function to export all something
def export_all(session, jsonfile, object_type):
    if object_type == 'disabledHosts':
        results = return_all(session, 'hosts', {"key":"enabled", "value":"false"})
    else:
        results = return_all(session, object_type)

    with open(jsonfile, 'w') as stream:
        stream.write(json.dumps(results))
    logging.info("All %d %s have been exported", len(results), object_type)

# Create tower inventory
def add_inventory(session, inventory_name, organization_name, delete=False, variables=""):
    organization_id = return_organization_id(session, organization_name)
    try:
        if delete:
            delete_inventory(session, inventory_name)
        inventory_id = return_inventory_id(session, inventory_name)
        logging.error("The inventory %s already exist with ID %d", inventory_name, inventory_id)
    except ObjectNotFound:
        url = api_url + 'inventories/'
        payload = {'name':inventory_name, 'organization':organization_id, 'variables':variables}
        r = session.post(url, json=payload)

        logging.info("%s %s", r.request.method, r.url)
        if (r.status_code != 201):
            raise ActionFailure("%d : Failed to add inventory %s %s" % (r.status_code, inventory_name, r.text))

        search_response = json.loads(r.text)
        inventory_id = search_response['id']

        logging.info("Inventory %s added with ID %s", inventory_name, inventory_id)
    return inventory_id

#Import all inventory in txtfile
def mass_import_inventory(session, txtfile):
    with open(txtfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in reader:
            add_inventory(session, row[0], row[1])
            count = count + 1
    logging.info("%d inventory(ies) imported", count)

#Remove inventory
def delete_inventory(session, inventory):
    inventory_id = return_inventory_id(session, inventory)

    url = api_url + 'inventories/' + str(inventory_id) + '/'
    r = session.delete(url)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to remove inventory %s %s" % (r.status_code, inventory, r.text))

    logging.info("Inventory %s deleted", inventory)
    return inventory_id

#Remove job template
def delete_job_template(session, job_template):
    job_template_id = return_job_template_id(session, job_template)

    url = api_url + 'job_templates/' + str(job_template_id) + '/'
    r = session.delete(url)

    logging.info("%s %s", r.request.method, r.url)
    if (r.status_code != 204):
        raise ActionFailure("%d : Failed to remove job_template %s %s" % (r.status_code, job_template, r.text))

    logging.info("Job Template '%s' deleted", job_template)
    return job_template_id

# browse yaml inventory (group_vars and host_vars)
def browse_yaml_inventory(session, type_var, path, inventory):
    list_file = absoluteFilePaths(path)
    for f in list_file:
        if '.yaml' in f or '.yml' in f:
            filename = f.split("/")
            filename = filename[-1].replace(".yaml", "").replace('.yml', '')
            with open(f, 'r') as stream:
                doc = yaml.safe_load(stream)
                for variable in doc:
                    if type_var == 'groups' or type_var == 'hosts':
                        associate_variable(session, type_var, filename, variable, doc[variable], inventory)
                    else:
                        raise ActionFailure("Error (Browse_yaml_inventory) : Type not found")

def main():
    parser = argparse.ArgumentParser()
    verbosity_choices = ['INFO', 'ERROR', 'DEBUG']
    parser.add_argument('--verbosity', action='store', choices=verbosity_choices, type=str, default='INFO')
    parser.add_argument('--username', action='store', type=str, default=username)
    parser.add_argument('--password', action='store', type=str, default=secret)
    subparsers = parser.add_subparsers(dest='subcommand')
    subparsers.required = True

    parser_addHost = subparsers.add_parser('addHost')
    parser_addHost.add_argument('fqdn', action="store", default=None)
    parser_addHost.add_argument('inventory_name', action="store", default=None)

    parser_massImportHost = subparsers.add_parser('massImportHost')
    parser_massImportHost.add_argument('txtfile', action="store", default=None)

    parser_massImportInventory = subparsers.add_parser('massImportInventory')
    parser_massImportInventory.add_argument('txtfile', action="store", default=None)

    parser_deleteHost = subparsers.add_parser('deleteHost')
    parser_deleteHost.add_argument('fqdn', action="store", default=None)

    parser_massDeleteHost = subparsers.add_parser('massDeleteHost')
    parser_massDeleteHost.add_argument('txtfile', action="store", default=None)

    parser_massChangeHostStatus = subparsers.add_parser('massChangeHostStatus')
    parser_massChangeHostStatus.add_argument('txtfile', action="store", default=None)

    parser_addGroup = subparsers.add_parser('addGroup')
    parser_addGroup.add_argument('group_name', action="store", default=None)
    parser_addGroup.add_argument('inventory_name', action="store", default=None)
    parser_addGroup.add_argument('--force-create', dest='force_create', action='store_true')
    parser_addGroup.set_defaults(disable_cooldown=False)

    parser_deleteGroup = subparsers.add_parser('deleteGroup')
    parser_deleteGroup.add_argument('group_name', action="store", default=None)
    parser_deleteGroup.add_argument('inventory_name', action="store", default=None)

    parser_addInventory = subparsers.add_parser('addInventory')
    parser_addInventory.add_argument('inventory_name', action="store", default=None)
    parser_addInventory.add_argument('--org', dest='organization_name', type=str, nargs='?', action="store", default="Default")
    parser_addInventory.add_argument('--force-create', dest='force_create', action='store_true')
    parser_addInventory.set_defaults(disable_cooldown=False)

    parser_deleteInventory = subparsers.add_parser('deleteInventory')
    parser_deleteInventory.add_argument('inventory_name', action="store", default=None)

    parser_deleteJobTemplate = subparsers.add_parser('deleteJobTemplate')
    parser_deleteJobTemplate.add_argument('job_template_name', action="store", default=None)

    parser_associate = subparsers.add_parser('associate')
    parser_associate.add_argument('fqdn', action="store", default=None)
    parser_associate.add_argument('group_name', action="store", default=None)
    parser_associate.add_argument('inventory_name', action="store", default=None)

    parser_associateVariable = subparsers.add_parser('associateVariable')
    type_choices = ['hosts', 'groups']
    parser_associateVariable.add_argument('type', action="store", choices=type_choices, type=str, default=None)
    parser_associateVariable.add_argument('name', action="store", type=str, default=None)
    parser_associateVariable.add_argument('key', action="store", type=str, default=None)
    parser_associateVariable.add_argument('value', action="store", type=str, default=None)
    parser_associateVariable.add_argument('inventory_name', action="store", type=str, default=None)

    parser_associateChildren = subparsers.add_parser('associateChildren')
    parser_associateChildren.add_argument('group_parent_name', action="store", default=None)
    parser_associateChildren.add_argument('group_child_name', action="store", default=None)
    parser_associateChildren.add_argument('inventory_name', action="store", default=None)

    parser_massAssociate = subparsers.add_parser('massAssociate')
    parser_massAssociate.add_argument('txtfile', action="store", default=None)

    parser_disassociate = subparsers.add_parser('disassociate')
    parser_disassociate.add_argument('fqdn', action="store", default=None)
    parser_disassociate.add_argument('group_name', action="store", default=None)
    parser_disassociate.add_argument('inventory_name', action="store", default=None)

    parser_hostGroups = subparsers.add_parser('hostGroups')
    parser_hostGroups.add_argument('fqdn', action="store", default=None)

    parser_groupMembers = subparsers.add_parser('groupMembers')
    parser_groupMembers.add_argument('group_name', action="store", default=None)
    parser_groupMembers.add_argument('inventory_name', action="store", default=None)
    parser_groupMembers.add_argument('--export', dest='export', action="store_true")
    parser_groupMembers.set_defaults(export=False)

    parser_groupListMembers = subparsers.add_parser('groupListMembers')
    parser_groupListMembers.add_argument('inventory_name', action="store", default=None)
    parser_groupListMembers.add_argument('group_list', nargs='+', action="store", default=None)
    parser_groupListMembers.add_argument('--inverse', dest='inverse', action="store_true")
    parser_groupListMembers.set_defaults(export=False)

    parser_groupVars = subparsers.add_parser('groupVars')
    parser_groupVars.add_argument('group_name', action="store", default=None)
    parser_groupVars.add_argument('inventory_name', action="store", default=None)

    parser_hostVars = subparsers.add_parser('hostVars')
    parser_hostVars.add_argument('fqdn', action="store", default=None)
    parser_hostVars.add_argument('--nested', action="store_true")

    parser_lastExecutionStatus = subparsers.add_parser('lastExecutionStatus')
    parser_lastExecutionStatus.add_argument('id', type=int, action="store", default=None)
    parser_lastExecutionStatus.add_argument('-q', '--quiet', dest='quiet', action="store_true")
    parser_lastExecutionStatus.set_defaults(quiet=False)

    parser_lastExecutionChange = subparsers.add_parser('lastExecutionChange')
    parser_lastExecutionChange.add_argument('id', type=int, action="store", default=None)
    parser_lastExecutionChange.add_argument('-q', '--quiet', dest='quiet', action="store_true")
    parser_lastExecutionChange.set_defaults(quiet=False)

    subparsers.add_parser('getAllGroupVars')
    subparsers.add_parser('getAllHostVars')
    subparsers.add_parser('getLonelyHosts')
    subparsers.add_parser('getLonelyGroups')
    subparsers.add_parser('getTemplatesWithSurvey')
    subparsers.add_parser('getTemplatesNotUsingDefault')
    subparsers.add_parser('getProjectsWithOldBranch')
    subparsers.add_parser('displayJobTemplatesCredentials')

    parser_launchJob = subparsers.add_parser('launchJob')
    parser_launchJob.add_argument('jsonfile', action="store", default=None)
    parser_launchJob.add_argument('--remote_username', action='store', type=str, default="")
    parser_launchJob.add_argument('--remote_password', action='store', type=str, default="")
    parser_launchJob.add_argument('--tags', action="store", default="")
    parser_launchJob.add_argument('--inventory', action="store", default="")
    parser_launchJob.add_argument('--limit', action="store", default="")
    parser_launchJob.add_argument('--si_version', action="store", default="")
    parser_launchJob.add_argument('--job_type', action="store", default="")
    parser_launchJob.add_argument('--disable_cooldown', dest='disable_cooldown', action='store_true')
    parser_launchJob.set_defaults(disable_cooldown=False)
    parser_launchJob.add_argument('--return_id', dest='return_id', action='store_true')
    parser_launchJob.set_defaults(return_id=False)

    parser_stopJob = subparsers.add_parser('stopJob')
    parser_stopJob.add_argument('job_id', action="store", default=None)

    parser_importAnsibleInventory = subparsers.add_parser('importAnsibleInventory')
    parser_importAnsibleInventory.add_argument('file', type=str, action="store", default=None)
    parser_importAnsibleInventory.add_argument('inventory', type=str, action="store", default=None)
    parser_importAnsibleInventory.add_argument('--export', dest='export_host_file', action="store_true")
    parser_importAnsibleInventory.set_defaults(export_host_file=False)
    parser_importAnsibleInventory.add_argument('--org', dest='organization_name', type=str,
            nargs='?', action="store", default="Default")
    parser_importAnsibleInventory.add_argument('--groupvars', dest='group_var_directory_path', type=str,
            nargs='?', action="store", default=None)
    parser_importAnsibleInventory.add_argument('--hostvars', dest='host_var_directory_path', type=str,
            nargs='?', action="store", default=None)

    parser_exportAnsibleInventory = subparsers.add_parser('exportAnsibleInventory')
    parser_exportAnsibleInventory.add_argument('jsonfile', type=str, action="store", default=None)
    parser_exportAnsibleInventory.add_argument('inventory_name', type=str, action="store", default=None)
    parser_exportAnsibleInventory.add_argument('--bash', action="store_true")

    parser_importJobTemplates = subparsers.add_parser('importJobTemplates')
    parser_importJobTemplates.add_argument('jsonfile', type=str, action="store", default=None)

    parser_exportAllJobTemplates = subparsers.add_parser('exportAllJobTemplates')
    parser_exportAllJobTemplates.add_argument('jsonfile', type=str, action="store", default=None)

    import_object_type = ['credentials', 'projects']
    parser_importAll = subparsers.add_parser('importAll')
    parser_importAll.add_argument('jsonfile', type=str, action="store", default=None)
    parser_importAll.add_argument('object_type', type=str, choices=import_object_type, action="store", default=None)
    parser_importAll.add_argument('--delete', dest='delete', action='store_true')

    export_object_type = ['credentials', 'projects', 'disabledHosts']
    parser_exportAll = subparsers.add_parser('exportAll')
    parser_exportAll.add_argument('jsonfile', type=str, action="store", default=None)
    parser_exportAll.add_argument('object_type', type=str, choices=export_object_type, action="store", default=None)

    args = parser.parse_args()

    logging.getLogger("requests").setLevel(logging.CRITICAL)

    logging.config.dictConfig({
        "version": 1,
        "handlers": {
            "console": {
                "level": args.verbosity,
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {
            "level": args.verbosity,
            "handlers": ["console"],
        },
    })

    mapp_call = {
        'addHost': add_host,
        'massImportHost': mass_import_host,
        'massImportInventory': mass_import_inventory,
        'deleteHost': delete_host,
        'massDeleteHost': mass_delete_host,
        'massChangeHostStatus': mass_change_host_status,
        'addGroup': add_group,
        'deleteGroup': delete_group,
        'addInventory': add_inventory,
        'deleteInventory': delete_inventory,
        'deleteJobTemplate': delete_job_template,
        'associate': associate_to_group,
        'associateVariable': associate_variable,
        'associateChildren': associate_children_to_group,
        'massAssociate': mass_associate,
        'disassociate': disassociate_from_group,
        'hostGroups': host_groups,
        'groupMembers': group_members,
        'groupListMembers': groupList_members,
        'groupVars': group_vars,
        'hostVars': host_vars,
        'lastExecutionStatus': last_execution_status,
        'lastExecutionChange': last_execution_change,
        'getAllGroupVars': all_group_vars,
        'getAllHostVars': all_host_vars,
        'getLonelyHosts': all_lonely_hosts,
        'getLonelyGroups': all_lonely_groups,
        'getTemplatesWithSurvey': all_templates_with_survey,
        'getTemplatesNotUsingDefault': all_not_default_project,
        'getProjectsWithOldBranch': all_projects_with_old_branch,
        'displayJobTemplatesCredentials': display_job_templates_credentials,
        'launchJob': launch_job,
        'stopJob': stop_job,
        'importAnsibleInventory': import_ansible_inventory,
        'exportAnsibleInventory': export_ansible_inventory,
        'importJobTemplates': import_job_templates,
        'exportAllJobTemplates': export_all_job_templates,
        'importAll': import_all,
        'exportAll': export_all,
    }

    if args.subcommand == "lastExecutionStatus" or args.subcommand == "lastExecutionChange":
        myargs = (args.quiet, args.id,)
    elif args.subcommand == "hostVars":
        myargs = (args.fqdn, args.nested)
    elif args.subcommand in {"deleteHost", "hostGroups"}:
        myargs = (args.fqdn,)
    elif args.subcommand == "addHost":
        myargs = (args.fqdn, args.inventory_name)
    elif args.subcommand == "associate" or args.subcommand == "disassociate":
        myargs = (args.fqdn, args.group_name, args.inventory_name)
    elif args.subcommand == "launchJob":
        if args.remote_username != "" and args.remote_password != "":
            myargs = (args.remote_username, args.remote_password, args.jsonfile, args.tags,
                    args.inventory, args.limit, args.si_version, args.job_type, args.disable_cooldown, args.return_id)
        else:
            myargs = (args.username, args.password, args.jsonfile, args.tags,
                    args.inventory, args.limit, args.si_version, args.job_type, args.disable_cooldown, args.return_id)
    elif args.subcommand == "stopJob":
        myargs = (args.job_id,)
    elif args.subcommand == "associateChildren":
        myargs = (args.group_parent_name, args.group_child_name, args.inventory_name)
    elif args.subcommand == "groupVars":
        myargs = (args.group_name, args.inventory_name)
    elif args.subcommand == "groupMembers":
        myargs = (args.group_name, args.inventory_name, args.export)
    elif args.subcommand == "groupListMembers":
        myargs = (args.inventory_name, args.inverse, args.group_list)
    elif args.subcommand in {"exportAllJobTemplates", "importJobTemplates"}:
        myargs = (args.jsonfile,)
    elif args.subcommand in {"exportAll"}:
        myargs = (args.jsonfile, args.object_type)
    elif args.subcommand in {"importAll"}:
        myargs = (args.jsonfile, args.object_type, args.delete)
    elif args.subcommand in {"massDeleteHost", "massImportHost", "massAssociate", "massImportInventory", "massChangeHostStatus"}:
        myargs = (args.txtfile,)
    elif args.subcommand in {"getAllGroupVars", "getAllHostVars", "getLonelyHosts", "getLonelyGroups",
            "getTemplatesWithSurvey", "getTemplatesNotUsingDefault", "getProjectsWithOldBranch", "displayJobTemplatesCredentials"}:
        myargs = ()
    elif args.subcommand == "importAnsibleInventory":
        myargs = (args.file, args.inventory, args.organization_name,
                args.export_host_file, args.group_var_directory_path, args.host_var_directory_path)
    elif args.subcommand == "exportAnsibleInventory":
        myargs = (args.jsonfile, args.inventory_name, args.bash)
    elif args.subcommand == "addGroup":
        myargs = (args.group_name, args.inventory_name, args.force_create)
    elif args.subcommand == "deleteGroup":
        myargs = (args.group_name, args.inventory_name)
    elif args.subcommand == "deleteInventory":
        myargs = (args.inventory_name,)
    elif args.subcommand == "deleteJobTemplate":
        myargs = (args.job_template_name,)
    elif args.subcommand == "addInventory":
        myargs = (args.inventory_name, args.organization_name, args.force_create)
    elif args.subcommand == "associateVariable":
        myargs = (args.type, args.name, args.key, args.value, args.inventory_name)

    try:
        session = authentication(args.username, args.password)
        mapp_call[args.subcommand](session, *myargs)
    except FileNotFoundError as e:
        logging.error("%s %s", type(e), e)
        sys.exit(2)
    except IndexError as e:
        logging.error("%s %s", e, ': You should check your txtfile syntax !')
        sys.exit(3)
    except ActionFailure as e:
        logging.error("%s", e)
        sys.exit(4)
    except Exception as e: # pylint: disable=broad-except
        if args.verbosity == 'DEBUG':
            logging.error("%s", e, exc_info=True)
        else:
            logging.error("%s %s", type(e), e)
        sys.exit(1)

if __name__ == '__main__':
    main()
