#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : http_requests.py
# @Author: LILIANG
# @Date  : 2019/6/3
# @Desc  :  test



import requests
from common import logger
from common.config import config #这里是直接导入的config的对象，需要明白不然会报错

logger=logger.my_logger(__name__)


"""
   独立session，cookies需要自己传递
   使用这类的reuquests方法去完成不同的HTTP请求，并返回相应结果
"""
class HttpRequests:
    def requests(self,method,url,data=None,json=None,cookies=None):
        if method.upper() == 'GET':
            resp=requests.get(url,params=data,cookies=cookies)
        elif method.upper() == 'POST':
            if json is None:
                resp=requests.post(url,json=json,cookies=cookies)
            else:
                resp=requests.post(url,data=data,cookies=cookies)
        else:
            resp=None
            print('un-support this method')
        return resp



"""
    共用一个session，cookies自动传递
    使用这类的requests方法去完成不同的HTTP请求，并返回响应结果
"""

class HttpRequests1:

    def __init__(self):
        self.session=requests.sessions.session()

    def requests(self,method,url,data=None,json=None):
        method=method.upper()
#注意str不能加引号，否则不会转换类型
        if type(data)==str:
            data=eval(data)

        # 拼接url
        url = config.get('api', 'pre_url') + url
        logger.debug('请求url{}'.format(url))
        logger.debug('请求url:{0}'.format(url))
        logger.debug('请求data:{0}'.format(data))

        if method == 'GET':
            resp=self.session.request(method,url,params=data)
        elif method =='POST':
            if json:
                resp=self.session.request(method,url,json=json)
            else:
                resp=self.session.request(method,url,data=data)
        else:
            resp = None
            logger.error('un-support this method')
        logger.debug('请求response:{0}'.format(resp.text))
        return resp

    def close(self):
        self.session.close()
        # 用完记得关闭，很关键！！！




if __name__ == '__main__':
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    http_request = HttpRequests()
    # 调用登陆
    resp = http_request.requests('get', url, data=params)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)

    # 调用充值
    params = {"mobilephone": "15810447878", "amount": "1000"}
    url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    resp2 = http_request.requests('get', url, data=params,cookies=resp.cookies)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)

    # params = {"mobilephone": "15810447878", "pwd": "123456"}
    # url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    # http_requests=HttpRequests1()
    # resp1=http_requests.requests('get',url,data=params)
    # print(resp1.status_code)
    # print(resp1.text)
    # print(resp1.cookies)
    #
    # # 调用充值
    # params = {"mobilephone": "15810447878", "amount": "1000"}
    # url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    # resp2 = http_requests.requests('get',url, data=params)
    # print(resp2.status_code)
    # print(resp2.text)
    # print(resp2.cookies)
