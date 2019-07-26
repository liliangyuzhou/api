#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_register.py
# @Author: LILIANG
# @Date  : 2019/5/29
# @Desc  :  test
import unittest
from common import do_excel
from common import constants
from common.http_requests import HttpRequests1
from common.logger import my_logger
from ddt import ddt,data
from common.do_mysql import DoMysql
logger=my_logger(__name__)



@ddt
class TestRegister(unittest.TestCase):

    do_excel=do_excel.DoExcel(constants.case_file,'register')
    cases=do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info("测试前置条件")
        cls.http_requests=HttpRequests1()
        cls.do_sql = DoMysql()


    @data(*cases)
    def test_register(self,case):
        logger.info("目前执行第{0}条测试用例，测试开始:{1}".format(case.case_id, case.title))


        if case.data.find('register_mobile'):
            sql="select max(mobilephone) from future.member"
            mobile=self.do_sql.fetch_one(sql)['max(mobilephone)']
            mobile=int(mobile)+1
            logger.info("用来发送请求的手机号码是{0}".format(mobile))
            # replace方法是特换之后重新返回一个新的字符串，所以需要使用case.data重新接收
            case.data=case.data.replace('register_mobile', str(mobile))# 特换参数值
            logger.info("替换后的case.data为{0}".format(case.data))




        resp=self.http_requests.requests(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.do_excel.write_result(case.case_id+1,resp.text,"PASS")
            logger.info("测试通过")
        except AssertionError as e:
            self.do_excel.write_result(case.case_id + 1, resp.text, "FAIL")
            logger.error("测试失败，报错{0}".format(e))
            raise e

    @classmethod
    def tearDownClass(cls):
      cls.http_requests.close()
      cls.do_sql.close()
