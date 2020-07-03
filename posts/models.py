from django.db import models
from tagging.fields import TagField
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(verbose_name='subject', max_length=200)
    content = models.TextField(verbose_name='content')
    tag = TagField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-modified',)

    def __str__(self):
        return self.subject


class Contact(models.Model):
    name = models.CharField(verbose_name='name', max_length=50)
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(verbose_name='phone', max_length=12)
    message = models.TextField(verbose_name='message')
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:10]
