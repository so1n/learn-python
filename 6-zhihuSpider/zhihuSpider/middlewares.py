# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random



class RandomProxy(object):
    def __init__(self,iplist):
        self.iplist=iplist

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('IPLIST'))

    def process_request(self, request, spider):
        proxy = random.choice(self.iplist)
        request.meta['proxy'] =proxy

