# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserInfoItem(scrapy.Item):

    #id
    urltoken = scrapy.Field()
    #个人简介
    user_info = scrapy.Field()
    #姓名
    zhihu_name = scrapy.Field()
    #居住地
    location = scrapy.Field()
    #技术领域
    business = scrapy.Field()
    #性别
    gender = scrapy.Field()
    #公司
    company = scrapy.Field()
    #职位
    job = scrapy.Field()
    #学校
    school = scrapy.Field()
    #教育经历
    major = scrapy.Field()
    #简介
    description = scrapy.Field()



