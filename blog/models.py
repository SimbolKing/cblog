from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.timezone import now


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=50, default='匿名')
    email = models.EmailField()
    created_time = models.CharField(max_length=50, default=now)
    comment_num = models.PositiveIntegerField(verbose_name='评论数', default=0)
    avatar = models.ImageField(upload_to='media', default="media/default.png")

    def __str__(self):
        return self.username

    def comment(self):
        self.comment_num += 1
        self.save(update_fields=['comment_num'])

    def comment_del(self):
        self.comment_num -= 1
        self.save(update_fields=['comment_num'])


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
# 修饰器
