import datetime
from django.db import models
from django.utils import timezone


# Create your models here.


class Article(models.Model):
    title = models.CharField('Article title', max_length=100)
    text = models.TextField('Article text')
    date = models.DateTimeField('Publish date')

    def __str__(self):
        return self.title

    def is_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('Author', max_length=100)
    text = models.TextField('Comment text', max_length=1000)
