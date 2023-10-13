#!/usr/bin/env python3
# coding=utf-8
# liyongjian5179@163.com
# 需要先安装阿里云的接口
# pip3 install aliyun-python-sdk-core-v3
# pip3 install pycryptodome==3.14.1

import sys
import json
import argparse
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def help_doc():
    aaa = '''
                  !!!something wrong, plz check it!!!
    usage: alidns.py [-h] [--add | --delete | --update | --get]
                          RR TYPE ADDRESS [RR TYPE ADDRESS ...]

    针对 xxx.com 域名记录进行相关操作

    positional arguments:
        RR TYPE ADDRESS  记录 类型 地址

    optional arguments:
        -h, --help       show this help message and exit
        -a, --add            add domain record. (e.g. --add RR TYPE ADDRESS)
        -d, --delete         delete domain record. (e.g. --delete RR)
        -u, --update         update domain record. (e.g. --update RR TYPE ADDRESS)
        -g, --get            get record ip. (e.g. --get RR)
    '''
    print(aaa)


def add_domain_record(rr, add_type, address):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('AddDomainRecord')

    request.add_query_param('DomainName', domain_name)
    request.add_query_param('RR', rr)
    request.add_query_param('Type', add_type)
    request.add_query_param('Value', address)
    request.add_query_param('TTL', '600')
    request.add_query_param('Line', 'default')

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))


def get_record_id(rr):
    sub_domain_name = rr + "." + domain_name
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('DescribeSubDomainRecords')

    request.add_query_param('SubDomain', sub_domain_name)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    # print(str(response, encoding='utf-8'))
    aaa = str(response, encoding='utf-8')
    bbb = json.loads(aaa)
    # print(bbb['RecordId'])
    recordid = bbb['DomainRecords']["Record"][0]["RecordId"]
    return recordid


def get_ip_address(rr):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('DescribeDomainRecords')
    request.add_query_param('PageSize', '500')

    request.add_query_param('DomainName', domain_name)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    # print(str(response, encoding = 'utf-8'))
    aaa = str(response, encoding='utf-8')
    bbb = json.loads(aaa)
    # print(bbb['RecordId'])
    rr_name = bbb['DomainRecords']['Record']
    # print(rr_name)

    for item in rr_name:
        if item['RR'] == rr:
            address = item['Value']
            print('The ip address :' + item['Value'])
        else:
            continue


def delete_domain_record(rr):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('DeleteSubDomainRecords')

    request.add_query_param('DomainName', domain_name)
    request.add_query_param('RR', rr)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))


def update_domain_record(rr, record_id, update_type, address):

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')

    request.add_query_param('RecordId', record_id)
    request.add_query_param('RR', rr)
    request.add_query_param('Type', update_type)
    request.add_query_param('Value', address)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

# parser = argparse.ArgumentParser(description='针对 xxx.com 域名记录进行相关操作')
# parser.add_argument('LIST', metavar='RR TYPE ADDRESS', type=str, nargs='+',
#                     help='记录 类型 地址')
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-a', '--add', action='store_true', help='add domain record. (e.g. --add RR TYPE ADDRESS)')
# group.add_argument('-d', '--delete', action='store_true', help='delete domain record. (e.g. --delete RR)')
# group.add_argument('-u', '--update', action='store_true', help="update domain record. (e.g. --update RR TYPE ADDRESS)")
# group.add_argument('-g', '--get', action='store_true', help='get record ip. (e.g. --get RR)')

# args = parser.parse_args()
# # print(args.add)
# # print(args.LIST)

# if args.add:
#     # print(args.add)
#     if len(args.LIST) != 3:
#         help_doc()
#         sys.exit(1)
#     RR = args.LIST[0]
#     ADD_TYPE = args.LIST[1]
#     ADDRESS = args.LIST[2]
#     add_domain_record(RR, ADD_TYPE, ADDRESS)

# elif args.delete:
#     if len(args.LIST) != 1:
#         help_doc()
#         sys.exit(1)
#     # print(args.delete)
#     RR = args.LIST[0]
#     delete_domain_record(RR)

# elif args.update:
#     # print(args.update)
#     if len(args.LIST) != 3:
#         help_doc()
#         sys.exit(1)
#     RR = args.LIST[0]
#     UPDATE_TYPE = args.LIST[1]
#     ADDRESS = args.LIST[2]
#     RECORD_ID = get_record_id(RR)
#     # print(RECORD_ID)
#     update_domain_record(RR, RECORD_ID, UPDATE_TYPE, ADDRESS)

# elif args.get:
#     # print(len(args.LIST))
#     if len(args.LIST) != 1:
#         help_doc()
#         sys.exit(1)

#     RR = args.LIST[0]
#     get_ip_address(RR)
#     # print(args.get)
# else:
#     help_doc()
#     sys.exit(1)


##ywz
from Crypto.Cipher import AES
import base64


BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def aesEncrypt(key, data):
    '''
    AES的ECB模式加密方法
    :param key: 密钥
    :param data:被加密字符串（明文）
    :return:密文
    '''
    key = key.encode('utf8')
    # 字符串补位
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    result = cipher.encrypt(data.encode())
    encodestrs = base64.b64encode(result)
    enctext = encodestrs.decode('utf8')
    print(enctext)
    return enctext

def aesDecrypt(key, data):
    '''

    :param key: 密钥
    :param data: 加密后的数据（密文）
    :return:明文
    '''
    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)

    # 去补位
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    print(text_decrypted)
    return text_decrypted



if __name__ == "__main__":
    import os
    from p2pinfo import *
    key = os.environ["key"]
    ##
    AccessKey_ID = "LTAI5tE733Ab3n5jcws1admK"
    Access_Key_Secret = "QwaNvnLxPvrDRYrp2yFSaW/dBDi3aUDKaayhg16imFk=" #hardcode
    key = '%016s' % (key)
    Access_Key_Secret = aesDecrypt(key, Access_Key_Secret)
    #for-each
    # RR = "207"
    # ADDRESS = '10.134.162.162'
    for server in config:
        try:
            RR = server
            ADDRESS = config[server]
            ###
            UPDATE_TYPE = 'A'
            domain_name = 'buaamc2.net'
            client = AcsClient(AccessKey_ID, Access_Key_Secret, 'default')
            RECORD_ID = get_record_id(RR)
            # print(RECORD_ID)
            update_domain_record(RR, RECORD_ID, UPDATE_TYPE, ADDRESS)
        except:
            print("cannot sync {}".format(server))