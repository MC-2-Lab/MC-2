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
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest


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
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Type(add_type)
    request.set_Value(address)
    request.set_Line('default')
    request.set_TTL('600')
    request.set_RR(rr)
    request.set_DomainName(domain_name)


    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))


def get_record_id(rr):
    sub_domain_name = rr + "." + domain_name
    try:
        request = DescribeSubDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_SubDomain(SubDomain=sub_domain_name)
        response = client.do_action_with_exception(request)
        json_data = json.loads(str(response, encoding='utf-8'))
        for RecordId in json_data['DomainRecords']['Record']:
            print(RecordId, rr)
            if rr == RecordId['RR']:
                return RecordId['RecordId'], RecordId['Value']
    except Exception as e:
        print("Get RecordId Fail")
        print(e)
        sys.exit(-1)


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
    try:
        request = UpdateDomainRecordRequest()
        request.set_accept_format('json')
        DomainValue = address
        request.set_Value(DomainValue)
        request.set_Type(update_type)
        request.set_RR(rr)
        request.set_RecordId(RecordId=record_id)
        response = client.do_action_with_exception(request)
        print("update domain success!")
    except Exception as e:
        print("update domain fail")
        print(e)



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
    Access_Key_Secret = "lR6v9mc5F5TkwyfczKGuSNMw7nVbEluyuoBTAqxeftw=" #hardcode
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
            response = get_record_id(RR)
            print(response)
            if response is not None:
                RECORD_ID, VALUE = response
                if VALUE != ADDRESS:
                    update_domain_record(RR, RECORD_ID, UPDATE_TYPE, ADDRESS)
            else:
                add_domain_record(RR, UPDATE_TYPE, ADDRESS)
        except:
            print("cannot sync {}".format(server))
