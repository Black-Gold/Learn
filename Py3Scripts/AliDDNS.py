#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from aliyunsdkcore import client
from aliyunsdkcore.request import RpcRequest

product = "Domain"
version = "2016-05-11"
accesskey = "XXXXXXXXXXXXXXXXXXXX"   # 请替换成自己的accesskey
accesspasswd = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"     # 请替换成自己的accesspasswd


def getip():
    return os.popen("curl http://members.3322.org/dyndns/getip  -s").read().replace('\n', '').replace('\r\n', '')


def getDNSrecords():
    global product, version, accesskey, accesspasswd
    clt = client.AcsClient(accesskey, accesspasswd, 'cn-hangzhou')
    request = RpcRequest('Alidns', '2015-01-09', 'DescribeDomainRecords')
    request.add_query_param("DomainName", "XXXXXXXXXXXXXXX")   # 请替换成自己的域名
    request.set_accept_format('json')
    response = clt.do_action_with_exception(request)
    return eval(response.replace('false', '0'))


def setDNSrecord(record, ip):
    global product, version, accesskey, accesspassw
    clt = client.AcsClient(accesskey, accesspasswd, 'cn-hangzhou')
    request = RpcRequest('Alidns', '2015-01-09', 'UpdateDomainRecord')
    request.add_query_param("RecordId", record['RecordId'])
    request.add_query_param("RR", record['RR'])
    request.add_query_param("Type", record['Type'])
    request.add_query_param("Value", ip)
    request.set_accept_format('json')
    response = clt.do_action_with_exception(request)
    print(response)


if __name__ == "__main__":
    ip = getip()
    print(ip)
    recordlist = getDNSrecords()
    for record in recordlist["DomainRecords"]["Record"]:
        setDNSrecord(record, ip)
