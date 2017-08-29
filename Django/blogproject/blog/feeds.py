#RSS订阅存放和功能代码
from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    #显示在聚合阅读器的镖旗标题
    title = "so1n blog"
    #网址
    link = "/"
    #显示在聚合阅读器上的描述信息
    description = "简介：略"
    #显示内容条目
    def items(self):
        return Post.objects.all()
    #内容条目的标题
    def item_title(self, item):
        return '[%s]%s' % (item.category, item.title)
    #内容条目的描述
    def item_Description(self, item):
        return item.body
