#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_recharge.py
# @Author: LILIANG
# @Date  : 2019/5/28
# @Desc  :  test

import unittest
from ddt import ddt,data
from common.do_excel import *
from common.config import config
from common import constants
from common.http_requests import HttpRequests1

from common import logger

logger=logger.my_logger(__name__)


@ddt
class TestRecharge(unittest.TestCase):


    do_excel=DoExcel(constants.case_file,'recharge')
    cases=do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info('测试前置')
        cls.http_requests=HttpRequests1()

    @data(*cases)
    def test_recharge(self,case):
        logger.info("目前执行第{0}条测试用例，测试开始:{1}".format(case.case_id,case.title))
        resp=self.http_requests.requests(case.method,case.url,case.data)
        actual=resp.json()['code']

        try:
            self.assertEqual(str(case.expected),actual)
            self.do_excel.write_result(case.case_id+1,resp.text,'PASS')
            logger.info("测试通过")

        except AssertionError as e:
            self.do_excel.write_result(case.case_id+1,resp.text,'FAIL')
            logger.error("测试失败，报错，{0}".format(e))
            raise e

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_requests.close()