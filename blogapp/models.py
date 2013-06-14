from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField(verbose_name='Content', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=40)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
    
    def get_url(self):
        return self.pub_date.strftime('%Y/%b') + "/" + self.slug


class Comment(models.Model):
    author = models.CharField("name", max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField("")
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))



