from wxpy import *
from pyecharts import Map

b = '市'
def s(x):
	return x+b


bot = Bot(cache_path = True)
friends = bot.friends(update=False).search(province = '广东')
citys = []
for f in friends :
    city = f.city
    citys.append(city)

r = map(s,citys)
cityss = list(r)
a = {}
for i in cityss:
	a[i] = cityss.count(i)
a.pop('市')
attrs = []
values = []
for value, attr in a.items():
	values.append(attr)
	attrs.append(value)
print(attrs)
print(values)
map = Map("广东地图示例", width=1200, height=600)
map.add("", attrs, values, maptype='广东', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render("city.html")
