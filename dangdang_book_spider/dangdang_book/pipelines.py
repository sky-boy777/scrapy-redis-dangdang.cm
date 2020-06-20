# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
client = MongoClient(host="127.0.0.1", port=27017)
db = client["dangdang_db"]


class DangdangBookPipeline:
    def process_item(self, item, spider):
        """保存数据到mongodb"""
        print(item)
        db.book.insert_one(dict(item))
        return item
