from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

#最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#归档模板标签
@register.simple_tag
def archives():
    #dates方法返回一个列表，列表中的元素为文章的3个数值，created_time即POst的创建时间，month是精度
    #order='DESC'表明降序排列
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
    #使用annotate计算从数据库返回对应category的文章，但是count会计算数量。最后通过把filter
    #把num_posts的值小鱼1的分类过滤掉
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


#以上都是利用template模块，然后实例化一个template.Library类，并将函数get_recent_posts装饰为register.simple_tag。这样就可以在模板中使用语法{% get_recent_posts %}调用这个函数了

