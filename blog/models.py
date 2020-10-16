from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#作者，外键
    title = models.CharField(max_length=200)#标题，用有限的字符定义一个文本
    text = models.TextField()#内容，长文本
    created_date = models.DateTimeField(
            default=timezone.now)#创建日期
    published_date = models.DateTimeField(
            blank=True, null=True)#发布日期

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title