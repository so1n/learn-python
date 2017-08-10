import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-09-02&leftTicketDTO.from_station=CBQ&leftTicketDTO.to_station=IZQ&purpose_codes=ADULT'
response = requests.get(url, verify=False)
rowlists = json.loads(response.text)['data']['result']
ticket_info_list = []
for rowlist in rowlists:
	row9 = rowlist.split('|')
	train_num = row[3]
	from_station = row[4]
	to_station = row[7]
	from_time = row[8]
	to_time = row[9]
	all_time = row[10]
	swz_num = row[32] or '--'
	ydz_num = row[31] or '--'
	edz_num = row[30] or '--'
	gjrw_num = row[21] or '--'
	rw_num = row[23] or '--'
	dw_num = row[27] or '--'
	yw_num = row[28] or '--'
	rz_num = row[24] or '--'
	yz_num = row[29] or '--'
	wz_num = row[26] or '--'
	ticket_info = [train_num, from_station, to_station, from_time, to_time, all_time , swz_num, ydz_num, edz_num, gjrw_num, rw_num, dw_num, yw_num, rz_num, yz_num, wz_num]
	ticket_info_list.append(ticket_info)
print(ticket_info_list)