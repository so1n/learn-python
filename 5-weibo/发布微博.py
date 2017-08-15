import re
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'}
cookie = {"Cookie": "SCF=As2n3qGYtJY8BBNqGCij4sh2aYjJGhNkN4qv5pwVSXYN88udeGOeNxNA0ZI_Za4AJP41-1pFqJfxUtPbqVEK0pk.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhvFRn81NOLI18NapekR53J5JpX5o2p5NHD95Qp1h.cSoqEeoM0Ws4DqcjMTCH81C-41C-R1FH8Sb-ReF-4xFH8SE-RSC-4B7tt; _T_WM=dcedffc6036ff64d2e8ff3f0a86abc4c; ___rl__test__cookies=1502619609613; OUTFOX_SEARCH_USER_ID_NCOO=1417673029.29369; H5_INDEX=3; H5_INDEX_TITLE=-%E9%99%88%E6%80%9D%E7%85%9C; SUB=_2A250lFp8DeRhGedG4lQX9izOzD-IHXVUd2Y0rDV6PUJbkdBeLVHTkW0JbzhXr11KqOE-K5ov9x4a7d4tAQ..; SUHB=0ida-3GQF3qZTD; SSOLoginState=1502620204; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home%26uicode%3D20000174"}
url = 'https://m.weibo.cn/compose'
html = requests.get(url, cookies=cookie).text
pattern = r'st:(.+)'
st = re.findall(pattern, html)[0].replace("'",'').replace(',','').replace(' ','')
post_url = 'https://m.weibo.cn/api/statuses/update'
postdata = {
            'st':st,
            'content':'测试Python发微博!',
            }
update = requests.post(post_url, data=postdata, headers=headers, cookies=cookie)





