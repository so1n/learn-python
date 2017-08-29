from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    #自动添加时间
    created_time = models.DateTimeField(auto_now_add=True)
    #一对多关系，一篇文章对应多个评论
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
