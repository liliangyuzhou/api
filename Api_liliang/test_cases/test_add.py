#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_add.py
# @Author: LILIANG
# @Date  : 2019/5/30
# @Desc  :  test
import unittest
from common.http_requests import HttpRequests1
from common import do_excel
from common import constants
from common.config import config
from ddt import ddt,data
from common.logger import my_logger
logger=my_logger(__name__)

@ddt
class TestAdd(unittest.TestCase):
    excel=do_excel.DoExcel(constants.case_file,'add')
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info("测试前置")
        cls.http_requests=HttpRequests1()

    @data(*cases)
    def test_add(self,case):
        logger.info("测试开始，当前执行第 {0} 条用例，标题为:{1}".format(case.case_id,case.title))
        case.data=eval(case.data)
        if case.data.__contains__('mobilephone') and case.data['mobilephone']=='normal_user':
            case.data['mobilephone']=config.get('data','normal_user')
        if case.data.__contains__('pwd') and case.data['pwd']=='normal_pwd':
            case.data['pwd']=config.get('data','normal_pwd')
        if case.data.__contains__('memberId') and case.data['memberId']=='loan_member_id':
            case.data['memberId']=config.get('data','loan_member_id')



        print(case.data)

        resp=self.http_requests.requests(case.method,case.url,case.data)


        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,'Pass')
        except AssertionError as e:
            logger.error("测试执行失败，报错{}".format(e))
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            raise e
        logger.info("测试结束，当前执行完成第 {0} 条用例，标题为:{1}".format(case.case_id,case.title))
        logger.info('******************')

    @classmethod
    def tearDownClass(cls):
        cls.http_requests.close()

