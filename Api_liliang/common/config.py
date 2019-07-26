#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: LILIANG
# @Date  : 2019/6/3
# @Desc  :  test

import configparser
from common import constants
from common import logger
logger=logger.my_logger(__name__)

class ReadConfig:

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(constants.global_file)
        switch=self.config.getboolean('switch','on')
        if switch:#开关状态为打开状态
            self.config.read(constants.online_file,encoding='utf-8')
            logger.info("目前测试环境为线上环境")
        else:
            self.config.read(constants.test_file,encoding='utf-8')
            logger.info("目前测试环境为测试环境")

    def get(self,section,option):
        return self.config.get(section,option)


config=ReadConfig()