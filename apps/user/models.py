from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
from tinymce.models import HTMLField


# Create your models here.
class User(AbstractUser, BaseModel):
    phone = models.CharField(max_length=11, default='', verbose_name='手机号')

    class Meta:
        db_table = 'auth_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
