#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_login.py
# @Author: LILIANG
# @Date  : 2019/5/27
# @Desc  :  test

import unittest
from ddt import ddt,data
from common import do_excel
from common.config import config
from common import constants
from common.http_requests import HttpRequests1

from common import logger

logger=logger.my_logger(__name__)


@ddt
class TestLogin(unittest.TestCase):


    do_excel=do_excel.DoExcel(constants.case_file,'login')
    cases=do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info('测试前置')
        cls.http_requests=HttpRequests1()

    @data(*cases)
    def test_login(self,case):
        logger.info("测试开始{}".format(case.title))
        resp=self.http_requests.requests(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.do_excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.do_excel.write_result(case.case_id+1,resp.text,'FAIL')
            logger.error("报错了，{0}".format(e))
            raise e
        logger.info('结束测试：{0}'.format(case.title))
    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_requests.close()







