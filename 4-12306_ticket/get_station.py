import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

url = 'https://kyfw.12306.cn/otn/leftTicket/init'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")
station_get = soup.find_all("script", {"type":"text/javascript"})[7]
a = re.sub(' ',"",str(station_get))
a = re.sub('"', "" ,a)
b = re.search('otn(.+)type', a).group()
c = b[:-4]
station_html = "https://kyfw.12306.cn/"+c
response = requests.get(station_html, verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
stations_dict = dict(stations)
with open('stations_dict.json', 'w') as fp:
	json.dump(stations_dict,fp=fp,ensure_ascii = False)