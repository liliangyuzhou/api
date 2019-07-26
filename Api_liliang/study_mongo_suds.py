#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : study_mongo_suds.py
# @Author: LILIANG
# @Date  : 2019/6/17
# @Desc  :  test


# -*- coding:utf-8 _*-
"""
@author:mongo
@time: 2018/12/17
@email:3126972006@qq.com
@function：
"""
import suds
from suds.client import Client

# 建立一个客户端
# 获取短信验证码
url = 'http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl '
client = Client(url)
print(client)
data = {"client_ip": "127.0.0.1", "tmpl_id": 1, "mobile": "15878787878"}
# try:
#     resp = client.service.sendMCode(data)
#     print("返回码", resp.retCode)
#     print("返回信息", resp.retInfo)
# except suds.WebFault as e:
#     print(e.fault.faultstring)

# 注册
# url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
# data = {"verify_code": 947716, "user_id": "霹雳娇娃", "channel_id": 1, "pwd": "123456", "mobile": "15878787878",
#         "ip": "127.0.0.1"}
# client = Client(url)
# try:
#     resp = client.service.userRegister(data)
#     print("返回码", resp.retCode)
#     print("返回信息", resp.retInfo)
# except suds.WebFault as e:
#     print(e.fault.faultstring)


def ws_request(url, data, method):
    client = Client(url)
    try:
        resp = eval("client.service.{0}({1})".format(method, data))
        print(type(resp))

        msg = resp.retInfo
        print("返回码", resp.retCode)
        print("返回信息", resp.retInfo)
    except suds.WebFault as e:
        print(e.fault.faultstring)
        msg = e.fault.faultstring

    return msg


url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
data = {"uid": 100010710, "true_name": "张三", "cre_id": "43041219900729002Z"}
resp = ws_request(url, data, "verifyUserAuth")

print("调用ws的返回",resp)
