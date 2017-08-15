import re
import requests
import json
from lxml import etree


cookie = {"Cookie": "SCF=As2n3qGYtJY8BBNqGCij4sh2aYjJGhNkN4qv5pwVSXYN88udeGOeNxNA0ZI_Za4AJP41-1pFqJfxUtPbqVEK0pk.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhvFRn81NOLI18NapekR53J5JpX5o2p5NHD95Qp1h.cSoqEeoM0Ws4DqcjMTCH81C-41C-R1FH8Sb-ReF-4xFH8SE-RSC-4B7tt; _T_WM=dcedffc6036ff64d2e8ff3f0a86abc4c; ___rl__test__cookies=1502619609613; OUTFOX_SEARCH_USER_ID_NCOO=1417673029.29369; H5_INDEX=3; H5_INDEX_TITLE=-%E9%99%88%E6%80%9D%E7%85%9C; SUB=_2A250lFp8DeRhGedG4lQX9izOzD-IHXVUd2Y0rDV6PUJbkdBeLVHTkW0JbzhXr11KqOE-K5ov9x4a7d4tAQ..; SUHB=0ida-3GQF3qZTD; SSOLoginState=1502620204; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home%26uicode%3D20000174"}
url = 'https://m.weibo.cn/api/container/getSecond?containerid=1005051896662273_-_FOLLOWERS&page=7'
html = requests.get(url, cookies=cookie)
ob_json=json.loads(html.text)
list_cards=ob_json['cards']
for card in list_cards:
	if card['card_type'] == 10:
		id = card['user']['id']
		name = card['user']['screen_name']
		description = card['user']['description']
		urank = card['user']['urank']
		gender = card['user']['gender']
		follow_me = card['user']['follow_me']
		if gender == 'm':
			gender =='男'
		if gender == 'f':
			gender =='女'
		else:
			gender == '其他'
		if follow_me:
			follow_me == '是'
		else:
			follow_me == '否'
		print('id:', id, '姓名:', name ,'简介:', description ,'等级:', urank, '性别:', gender ,'是否关注我:', follow_me)





