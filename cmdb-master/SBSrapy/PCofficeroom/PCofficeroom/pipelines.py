# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.utils.project import get_project_settings

class PcofficeroomPipeline(object):
    InsertSQL = '''insert into room(roomid, title)VALUES('{roomid}', '{title}')'''

    def __init__(self):
        # self.conn = pymysql.connect(host="118.190.36.135",user="root",passwd="1111",db="hexun")
        self.settings = get_project_settings()
        self.connect = pymysql.connect(
            host=self.settings.get("MYSQL_HOST"),
            port=self.settings.get("MYSQL_PORT"),
            db=self.settings.get("MYSQL_DBNAME"),
            user=self.settings.get("MYSQL_USER"),
            passwd=self.settings.get("MYSQL_PASSWD"),
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        # print("===========================进入item方法:".format(item['roomno']))

        sqltest = self.InsertSQL.format(roomid=item["roomid"],title=item["roomtile"])
        try:
            self.cursor.execute(sqltest)
            self.connect.commit()
        except Exception as e:
            print('插入数据失败了',e)
        return item

    def close_spider(self, spiker):
        self.cursor.close()
        self.connect.close()
        # for j in range(0, len(item[' '])):
        #     roomid = item["roomid"][j]
        #     title = item["title"][j]
        #     sql = "insert into room(roomid,title) VALUES('" + roomid + "','\
        #            " + title + "')"
        #     self.conn.commit()
        #     self.conn.query(sql)
        #
        # return item
        #
        # def close_spider(self, spider):
        #     # 最后关闭数据库连接
        #     self.conn.close()
