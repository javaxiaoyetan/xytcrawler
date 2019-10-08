# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb as mysqldb
import json
#重置编码格式
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from settings import MYSQL_HOST,MYSQL_DBNAME,MYSQL_USER,MYSQL_PASSWD
import logging
from util.date import get_now

class XytcrawlerPipeline(object):
    def __init__(self):
        self.host = MYSQL_HOST
        self.port = 3306
        self.username = MYSQL_USER
        self.password = MYSQL_PASSWD
        self.dbname = MYSQL_DBNAME


    def get_mysql_conn(self):
        return mysqldb.connect(host=self.host,port=self.port,user=self.username,passwd=self.password,db=self.dbname,charset="utf8")

    def process_item(self, item, spider):
        try :
            print item['city']
            conn = self.get_mysql_conn()
            c = conn.cursor()
            sql = """ INSERT INTO crawler.weather (weather_date, province, city, day, day_temperature, night, night_temperature, sunrise, sunset, create_time) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
            val = (item['weather_date'], item['province'], item['city'],item['day'],item['day_temperature'],item['night'],item['night_temperature'],item['sunrise'],item['sunset'],get_now())
            print sql
            print val
            c.execute(sql,val)
            conn.commit()
            c.close()
            conn.close()
        except Exception as error:
            logging.error(error)

        return item

