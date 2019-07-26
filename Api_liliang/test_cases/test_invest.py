#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_invest.py
# @Author: LILIANG
# @Date  : 2019/5/30
# @Desc  :  test
import unittest
from ddt import ddt,data
from common.http_requests import HttpRequests1
from common.do_excel import DoExcel
from common import constants
from common.logger import my_logger
from common.context import replace_re
from common.do_mysql import DoMysql
from common.context import  Context

logger=my_logger(__name__)
@ddt
class TestInvest(unittest.TestCase):

    excel=DoExcel(constants.case_file,'invest')
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info("测试前置")
        cls.http_requests=HttpRequests1()
        cls.mysql=DoMysql()


    @data(*cases)
    def test_invest(self,case):
        logger.info("测试开始执行第 {0} 条测试用例，用例标题是{1}".format(case.case_id,case.title))

        case.data=replace_re(case.data)

        print(case.data)
        resp=self.http_requests.requests(case.method,case.url,case.data)
        if resp.json()['msg']=="加标成功":
            sql='select id from future.loan where memberid = 1008 order by id desc limit 1'
            loan_id=self.mysql.fetch_one(sql)['id']
            setattr(Context,'loan_id',str(loan_id))


        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,"PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,"FAIL")
            logger.error("测试不通过，报错%s",e)
            raise e
        logger.info("第 {0} 条测试用例执行完毕，用例标题是{1}".format(case.case_id, case.title))


    @classmethod
    def tearDownClass(cls):
        cls.http_requests.close()
