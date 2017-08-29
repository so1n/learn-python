import markdown
from django.utils.html import strip_tags
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    #记录阅读量
    views = models.PositiveIntegerField(default=0)
    #时间倒序
    created_time = models.DateTimeField()
    #标题
    title = models.CharField(max_length=100)
    #文章，由于文章文字比较多，所以使用TextField
    body = models.TextField()
    #创建时间
    created_time = models.DateTimeField()
    #修改时间
    modified_time = models.DateTimeField()
    #文章摘要,有些情况是没有文章摘要的，而CharField默认情况下
    #要求我们需要写入数据，设置blank=True参数后就可以空值了
    excerpt = models.CharField(max_length=200, blank=True)
    #分类，因为一个分类可以有很多文章，所以使用一对多关系
    category = models.ForeignKey(Category)
    #标签，因为一个文章有多个标签，一个标签有多个文章，所以使用多对多关系
    #原教程说文章可以没标签，但我都是有写标签的，就不设置blank了
    tags = models.ManyToManyField(Tag, blank=True)
    #文章作者，这里的User是从django,contrib,auth,models导入的
    #是Django内置的应用，专门处理网站用户注册登录，User是Django为我们准备好的，
    #博客作者就我一个，所以和User关联起来，同时一个作者写多篇文章，是一对多关系
    author = models.ForeignKey(User)
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extenstions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:60]
            super(Post,self).save(*args, **kwargs)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']

