# -*- coding: utf-8 -*-
import scrapy
import re
import json

from lxml import html
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from zhihuSpider.items import  UserInfoItem


class ZhihuComSpider(CrawlSpider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/sgai/following']


    #rules = (
    #    Rule(LinkExtractor(allow=r'/people/(\w+)/following$', process_value='my_process_value', unique=True, deny_domains=deny), callback='parse_item', follow=True),
    #)


    def parse(self, response):
        deny = []
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        token = soup.find("a",{"class":"Tabs-link"})
        pattern = r'e/(.+)/ac'
        urltoken = re.findall(pattern, str(token))[0]
        json_text = soup.body.contents[1].attrs['data-state']
        ob_json = json.loads(json_text)
        followinglist = ob_json['people']['followingByUser'][urltoken]['ids']
        tempset = set(followinglist)
        try:
            tempset.remove(None)
        except:
            pass
        followinglist = list(tempset)
        user_json = ob_json['entities']['users'][urltoken]
        user_info = user_json['headline']
        try:
            school = user_json['educations'][0]['school']['name']
        except:
            school = '该用户尚未填写'
        try:
            major = user_json['educations'][0]['major']['name']
        except:
            major = '该用户尚未填写'
        try:
            job = user_json['employments'][0]['job']['name']
        except:
            job = '该用户尚未填写'
        try:
            company = user_json['employments'][0]['company']['name']
        except:
            company = '该用户尚未填写'
        try: 
            description = user_json['description']
            tree=html.fromstring(description)
            description=tree.xpath('string(.)')
        except:
            description = '该用户尚未填写'
        try:
            business = user_json['business']['name']
        except:
            business = '该用户尚未填写'
        try:
            zhihu_name = user_json['name']
        except:
            zhihu_name = '该用户尚未填写'
        try:
            location = user_json['locations'][0]['name']
        except:
            location = '该用户尚未填写'
        gender = user_json['gender']
        if gender == 1:
            gender = '男'
        elif gender == 0:
            gender = '女'
        else:
            gender = '未知'

        item =UserInfoItem(urltoken=urltoken,user_info=user_info, job=job, company=company, description=description, business=business, zhihu_name=zhihu_name, location=location, gender=gender, school=school, major=major) 
        yield item
        print(followinglist)
        for following in followinglist:
            if following:
                url = 'https://www.zhihu.com/people/'+following+'/following'
            else:
                url = 'https://www.zhihu.com/people/'+urltoken+'/following'

            if url in deny:
                pass
            else:
                deny.append(url)    
                yield scrapy.Request(url=url,callback=self.parse)

    
