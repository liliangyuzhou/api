#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : do_mysql.py
# @Author: LILIANG
# @Date  : 2019/6/3
# @Desc  :  test
import pymysql
from common.config import config
from common.logger import my_logger
logger=my_logger(__name__)

class DoMysql:
    """
    完成mysql数据库的交互
    """
    def __init__(self):
        """
        因为数据库，每次连接才能操作，所以直接将连接数据库的方法修改为初始化方法
        """
        try:
            logger.info("读取配置文件中的mysql")
            host=config.get('mysql','host')
            user=config.get('mysql','user')
            password = config.get('mysql', 'password')
            port = int(config.get('mysql', 'port'))

            # 创建连接
            logger.info("创建连接")
            self.mysql=pymysql.Connect(host=host, user=user, password=password, port=port, charset='utf8')
            logger.info('数据库连接成功')
            #设置查询比并返回字典，self.cursor是实例变量属性，可以在该类的所有方法中使用
            self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)

        except Exception as e:
            logger.info('数据库连接失败')
            raise e

    def fetch_one(self,sql):
        logger.info("执行sql语句")
        self.cursor.execute(sql)
        self.mysql.commit()
         #返回一条数据，元组
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        logger.info("执行sql语句")
        self.cursor.execute(sql)
        return self.cursor.fetchall()#返回一组数据

    def close(self):
        logger.info("关闭查询页面并关闭数据库连接")
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql=DoMysql()
    sql = 'select max(mobilephone) from future.member'
    result=mysql.fetch_one(sql)
    print(type(result),result)
    sql='select * from future.loan limit 2'
    result=mysql.fetch_all(sql)
    print(type(result), result)

    mysql.close()
