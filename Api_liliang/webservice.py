#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webservice.py
# @Author: LILIANG
# @Date  : 2019/6/5
# @Desc  :  test
from suds.client import Client


#注册接口
# user_url="http：//120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
#短信验证接口
user_url="http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
#这里是你的webservice访问地址
client=Client(user_url)
#Client里面直接放访问的URL，可以生成一个webservice对象
print(client)
#打印所webservice里面的所有接口方法名称




