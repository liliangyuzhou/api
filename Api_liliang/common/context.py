#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : context.py
# @Author: LILIANG
# @Date  : 2019/6/3
# @Desc  :  test

import re
import configparser
from common.config import config
from common.logger import my_logger
logger=my_logger(__name__)
#反射写入数值专用类
class Context:
    loan_id = None


def replace_re(data):
    p= "#(.*?)#"
    while re.search(p,data):
        logger.info(data)
        m=re.search(p,data)
        v=m.group(1)
        try:
            g=config.get('data',v)
        except configparser.NoOptionError as  e:
            if hasattr(Context,v):
                g=getattr(Context,'loan_id')
            else:
               logger.info("没有此属性值")
        data=re.sub(p,g,data,count=1)
    logger.info("最终替换的data为{}".format(data))


    return data


if __name__ == '__main__':

    data='{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
    replace_re(data)
