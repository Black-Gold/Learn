#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import time
import json
import urllib
from urllib import request


class CloudXNS_API():
    api_key = None
    secret_key = None
    debug_log = False

    def __init__(self, api_key=None, secret_key=None, debug_log=False):
        self.api_key = api_key
        self.secret_key = secret_key
        self.debug_log = debug_log

    def print_debug(self, msg):
        if self.debug_log != False:
            print(msg)

    def json_strtodict(self, json_str):
        jsonData = {}
        try:
            if len(json_str) != 0:
                jsonData = json.loads(json_str)
        except Exception as e:
            self.print_debug(e)
        finally:
            return jsonData

    # 计算api头数据
    def get_api_headers(self, URL, BODY):
        API_REQUEST_DATE = time.strftime('%a %b %d %H:%M:%S %Y',
                                         time.localtime())
        API_HMAC = hashlib.md5((
                                           self.api_key + URL + BODY + API_REQUEST_DATE + self.secret_key).encode()).hexdigest()
        headers = {
            'Content-Type': 'application/json',
            'user-agent': 'CloudXNS-Python/v3',
            'API-KEY': self.api_key,
            'API-REQUEST-DATE': API_REQUEST_DATE,
            'API-HMAC': API_HMAC,
            'API-FORMAT': 'json',
        }
        return headers

    def urlopen(self, URL, BODY='', METHOD='GET'):
        strdata = ''
        try:
            req = urllib.request.Request(URL)
            req.method = METHOD
            if len(BODY) != 0:
                req.data = BODY.encode('UTF-8', 'ignore')
            resp = urllib.request.urlopen(req)
            strdata = resp.read().decode('UTF-8', 'ignore')
        except urllib.error.HTTPError as e:
            self.print_debug(e)
            pass
        except urllib.error.URLError as e:
            self.print_debug(e)
            pass
        except Exception as e:
            self.print_debug(e)
            pass
        finally:
            return strdata

    def urlopen_api(self, URL, BODY, METHOD='GET'):
        strdata = ''
        try:
            req = urllib.request.Request(URL, headers=self.get_api_headers(URL,
                                                                           BODY))
            req.method = METHOD
            if len(BODY) != 0:
                req.data = BODY.encode('UTF-8', 'ignore')
            resp = urllib.request.urlopen(req)
            strdata = resp.read().decode('UTF-8', 'ignore')
        except urllib.error.HTTPError as e:
            self.print_debug(e)
            pass
        except urllib.error.URLError as e:
            self.print_debug(e)
            pass
        except Exception as e:
            self.print_debug(e)
            pass
        finally:
            return strdata

    """
    功能 域名列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """

    def domain_list(self):
        url = 'https://www.cloudxns.net/api2/domain'
        body = ''
        strdata = self.urlopen_api(url, body)
        # json_strtodict
        return strdata

    """
    功能 主机记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/host/:domain_id?offset=:offset&row_num=:row_num
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer 是 域名ID
            offset Integer  否 记录开始的偏移,第一条记录为 0,依次类推
            row_num Integer 否 要获取的记录的数量,比如获取 30 条,则为 30,最大可取 2000条
    :return: String
    """

    def domain_host_list(self, domain_id, offset=0, row_num=30, hostname=None):
        if row_num > 2000:
            row_num = 2000
        url = 'https://www.cloudxns.net/api2/host/' + str(
            domain_id) + '?offset=' + str(offset) + '&row_num=' + str(
            row_num)
        if hostname != None:
            url += '&host_name=' + hostname
        body = ''
        strdata = self.urlopen_api(url, body)
        return strdata

    """
    功能 暂停、启用解析记录
    参数名称 类型 必填 描述
    domain_id Integer 是 域名ID
    host_id Integer 是 主机记录ID
    pause_record bool 是 暂停还是启用
    """

    def domain_host_record_pause(self, domain_id, host_id, pause_record=False):
        url = 'https://www.cloudxns.net/api2/record/pause'
        object_body = {}
        object_body['id'] = str(host_id)
        object_body['domain_id'] = str(domain_id)
        # 0暂停1启用
        if pause_record == False:
            object_body['status'] = str(0)
        else:
            object_body['status'] = str(1)
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'POST')
        return strdata

    """
    功能 删除主机记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/host/:id
        请求参数：
            参数名称 类型 必填 描述
            host_id Integer 是 主机记录id
    :return: String
    """

    def domain_host_delete(self, domain_host_id):
        url = 'https://www.cloudxns.net/api2/host/' + str(domain_host_id)
        body = ''
        strdata = self.urlopen_api(url, body, 'DELETE')
        return strdata

    """
    功能 获取解析记录列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/:domain_id?host_id=0&offset=:offset&row_num=:row_num
    URL 参数说明
        domain_id:域名 id
        host_id:主机记录 id(传 0 查全部)
        offset:记录开始的偏移，第一条记录为 0，依次类推,默认取 0
        row_num:要获取的记录的数量， 比如获取 30 条， 则为 30,最大可取 2000
        条,默认取 30 条.
    :return:
        code int 请求状态，详见附件 code 对照表
        message String 操作信息，提示操作成功或错误信息
        total int 总记录条数
        offset int 记录开始的偏移
        row_num int 要获取的记录的数量
        data array 记录列表
            record_id: 解析记录 id
            host_id:主机记录 id
            host：主机记录名
            line_id：线路 ID
            line_zh：中文名称
            line_en：英文名称
            mx：优先级
            Value：记录值
            Type：记录类型
            Status：记录状态(ok 已生效 userstop 暂停)
            create_time：创建时间
            update_time：更新时间
    """

    def domain_host_record_list(self, domain_id, host_id=0, offset=0,
                                row_num=30, host_name=None):
        if row_num > 2000:
            row_num = 2000
        #:domain_id?host_id=0&offset=:offset&row_num=:row_numURL
        if host_name == None:
            url = 'https://www.cloudxns.net/api2/record/' + str(
                domain_id) + '?host_id=' + str(host_id) \
                  + '&offset=' + str(offset) + '&row_num=' + str(row_num)
        else:
            url = 'https://www.cloudxns.net/api2/record/' + str(
                domain_id) + '?host_name=' + str(host_name) \
                  + '&offset=' + str(offset) + '&row_num=' + str(row_num)

        body = ''
        strdata = self.urlopen_api(url, body)
        return strdata

    """
    功能 添加解析记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer  域名 id
            host_name String  主机记录名称 如 www, 默认@
            value String 记录值, 如IP:8.8.8.8,CNAME:cname.cloudxns.net., MX: mail.cloudxns.net.
            type String 记录类型,通过 API 获得记录类型,大写英文,比如:A
            mx Integer 优先级,范围 1-100。当记录类型是 MX/AX/CNAMEX 时有效并且必选
            ttl Integer TTL,范围 60-3600,不同等级域名最小值不同
            line_id Integer 线路id,(通过 API 获得记录线路 id)
        :return: String
    """

    def domain_host_record_add(self, domain_id, host, host_value, record_type,
                               line_id=1, mx=10, ttl=600):
        url = 'https://www.cloudxns.net/api2/record'
        object_body = {}
        object_body['domain_id'] = domain_id
        if host != '@':
            object_body['host'] = host
        object_body['value'] = host_value
        object_body['type'] = record_type
        object_body['line_id'] = line_id
        if record_type == 'MX' or record_type == 'CNAMEX' or record_type == 'AX':
            object_body['mx'] = mx
        object_body['ttl'] = ttl
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'POST')
        return strdata

    """
    功能 添加备记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/spare
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer  域名 id
            host_id Integer  主机记录名称 如 www, 默认@
            record_id Integer 解析记录id
            value String 记录值, 如IP:8.8.8.8,CNAME:cname.cloudxns.net., MX: mail.cloudxns.net.
        :return: String
    """

    def domain_host_record_spare(self, domain_id, host_id, record_id, value):
        url = 'https://www.cloudxns.net/api2/record'
        object_body = {}
        object_body['domain_id'] = domain_id
        object_body['host_id'] = host_id
        object_body['record_id'] = record_id
        object_body['value'] = value
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'POST')
        return strdata

    """
    功能 更新解析记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/:id
        请求参数：
            参数名称 类型 必填 描述
            record_id Integer 解析记录id
            domain_id Integer 域名id
            host_name String 主机记录名称 如 www, 默认@
            value String 记录值, 如IP:8.8.8.8,CNAME:cname.cloudxns.net., MX: mail.cloudxns.net.
            record_type String 记录类型,通过 API 获得记录类型,大写英文,比如:A
            mx Integer 优先级,范围 1-100。当记录类型是 MX/AX/CNAMEX 时有效并且必选
            ttl Integer TTL,范围 60-3600,不同等级域名最小值不同
            line_id Integer 线路 id,(通过 API 获得记录线路 id)
            spare_data String 备IP
        :return: String
    """

    def domain_host_record_update(self, domain_id, record_id, host, host_value,
                                  record_type, line_id=1, mx=10, ttl=600,
                                  bak_ip=None):
        url = 'https://www.cloudxns.net/api2/record/' + str(record_id)
        object_body = {}
        object_body['domain_id'] = domain_id
        if host != '@':
            object_body['host'] = host
        object_body['value'] = host_value
        object_body['type'] = record_type
        object_body['line_id'] = line_id
        if record_type == 'MX' or record_type == 'CNAMEX' or record_type == 'AX':
            object_body['mx'] = mx
        object_body['ttl'] = ttl
        if bak_ip != None:
            object_body['bak_ip'] = bak_ip
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'PUT')
        return strdata

    """
    功能 删除解析记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/:id/:domain_id
        请求参数：
            参数名称 类型 必填 描述
            record_id Integer 解析记录id
            domain_id Integer  域名 id
        :return: String
    """

    def domain_host_record_delete(self, domain_id, host_id):
        url = 'https://www.cloudxns.net/api2/record/' + str(
            host_id) + '/' + str(domain_id)
        body = ''
        strdata = self.urlopen_api(url, body, 'DELETE')
        return strdata

    """功能：是否启用X优化"""

    def domain_host_record_x_ai(self, domain_id, host_id, enable=False):
        url = 'https://www.cloudxns.net/api2/record/ai'
        object_body = {}
        object_body['id'] = host_id
        object_body['domain_id'] = domain_id
        if enable == False:
            object_body['status'] = 0
        else:
            object_body['status'] = 1
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'POST')
        return strdata

    """
    功能：设置DDNS解析
    修改 domain 下线路为 line_id（默认为 1（全网默认））、
    记录类型为 A 的记录值为新的 IP 值（为空时 API 自动获取客户端 IP）；
    如果 domain 存在但不存在线路为line_id的记录类型为A的解析记录则添加新的解析记录
    参数名称 类型 描述
    domain string 含主机记录的域名（如主机记录为@时 domain 是 cloudxns.net，为 www 时 domain 是 www.cloudxns.net）
    ip string 记录 IP 值（8.8.8.8）或者多个 IP 值中间用|分割 （8.8.8.8|1.1.1.1） ;为空时 IP 值由 API 自动获取客户端 IP
    line_id int 线路 id(通过 API 获取)，默认值 1（全网默认）
    """

    def domain_host_DDNS(self, domain, ip='', line_id=1):
        url = 'https://www.cloudxns.net/api2/ddns'
        object_body = {}
        object_body['domain'] = domain
        if len(ip) != 0:
            object_body['ip'] = ip
        object_body['line_id'] = line_id
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'POST')
        return strdata

    """
    功能 添加域名
    HTTP 请求方式 POST
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """

    def domain_add(self, domain):
        url = 'https://www.cloudxns.net/api2/domain'
        object_body = {}
        object_body['domain'] = domain
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'POST')
        return strdata

    """
    功能 删除域名
    HTTP 请求方式 DELETE
    URL https://www.cloudxns.net/api2/domain
    请求参数：
        参数名称 类型 必填 描述
        domain_id Integer 是 域名ID
    :return: String
    """

    def domain_delete(self, domain_id):
        url = 'https://www.cloudxns.net/api2/domain/' + str(domain_id)
        body = ''
        strdata = self.urlopen_api(url, body, 'DELETE')
        return strdata

    # 获取 NS 服务器列表信息
    def get_domain_ns(self):
        url = 'https://www.cloudxns.net/api2/ns_server'
        body = ''
        strdata = self.urlopen_api(url, body)
        return strdata

    # 获取记录类型列表
    def get_record_type(self):
        url = 'http://www.cloudxns.net/api2/type'
        body = ''
        strdata = self.urlopen_api(url, body)
        return strdata

    # 获取线路列表
    def get_line(self):
        url = 'https://www.cloudxns.net/api2/line'
        body = ''
        strdata = self.urlopen_api(url, body)
        return strdata

    # 获取区域列表
    def get_line_region(self):
        url = 'https://www.cloudxns.net/api2/line/region'
        body = ''
        strdata = self.urlopen_api(url, body)
        return strdata

    # 获取 ISP 列表
    def get_isp_list(self):
        url = 'https://www.cloudxns.net/api2/line/isp'
        body = ''
        strdata = self.urlopen_api(url, body)
        return strdata

    """
    功能 获取某域名解析量统计数据
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/domain_stat/:id
    URL 参数说明 Id：域名 ID
    请求参数：
        参数名称 类型 必填 描述
        host String 是 主机名，查询全部传 all
        code String 是 统计区域 Id 或统 ISP Id，查询全部传 all
        start_date Date 是 开始时间 格式：yyyy-mm-dd
        end_date Date 是 结束时间 格式：yyyy-mm-dd
    :return:
    """

    def domain_get_domain_stat(self, domain_id, host, code, start_date,
                               end_date):
        url = 'https://www.cloudxns.net/api2/domain_stat/' + str(domain_id)
        object_body = {}
        object_body['host'] = host
        object_body['code'] = code
        object_body['start_date'] = start_date
        object_body['end_date'] = end_date
        body = json.dumps(object_body)
        strdata = self.urlopen_api(url, body, 'POST')
        return strdata

    def http_dns_get(self, domain, client_ip='', ttl='',
                     http_dns_interface='http://httpdnsv3.ffdns.net'):
        if domain == None or len(domain) == 0:
            return ''
        url = http_dns_interface + '/httpdns?dn=' + str(domain)
        if client_ip != None and len(client_ip) != 0:
            url += '&cip=' + str(client_ip)
        if ttl != None and len(ttl) != 0:
            url += '&ttl=' + str(ttl)
        strdata = self.urlopen(url)
        return strdata


if __name__ == '__main__':
    api = CloudXNS_API(api_key='a7fe5ecbb823e7b0c968b2a885a18e98',
                       secret_key='a5e984dd94e24f60891cc32746b115d7',
                       debug_log=True)
    api.domain_add('test.org')
    print(api.domain_list())
    # api.domain_host_record_add(216271,'test','127.0.0.1','A',1)
    api = CloudXNS_API()
    # str=api.http_dns_get('www.test.net')
    # dict=api.json_strtodict(str)
    # print(str)
    pass
