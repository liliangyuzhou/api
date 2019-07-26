#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : constants.py
# @Author: LILIANG
# @Date  : 2019/6/3
# @Desc  :  test

"""
路径一般尽量不要写死，可以根据框架的结构来进行动态的获取，可以先确定一个固定的路径（所有的目录都
包括的那一层级）
"""
import os
# ##不建议写成__name__，因为这仅仅写死了当前文件绝对的路径
# # base_dir=os.path.abspath(__name__)
# #写成__file__相当于动态获取当前文件绝对的路径，有利于后面各个路径的拼接
# base_dir=os.path.abspath(__file__)
# print(base_dir)

"""os.path.dirname()获取到当前文件的上一级目录,这里去了当前文件constants的上两级文件，
D:\pytest_dubbo\Api_liliang,这相当于当前目录结构下（project的下一层，不能取到project）
所有文件目录的一个公用目录层级，方面后面路径的拼接，路径拼接使用os.path.join()
"""
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

case_file=os.path.join(base_dir,'data','xiaohai0412_testcases.xlsx')
# print(case_file)

global_file=os.path.join(base_dir,'config','global.conf')

online_file=os.path.join(base_dir,'config','online.conf')

test_file=os.path.join(base_dir,'config','test.conf')

cases_file=os.path.join(base_dir,'test_cases')

report_file=os.path.join(base_dir,'report')

log_file=os.path.join(base_dir,'log')