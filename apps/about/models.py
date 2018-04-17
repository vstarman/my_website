from django.db import models


# Create your models here.
# 企业信息表
class Poll(models.Model):
    """企业信息模型"""
    name = models.CharField(max_length=100, verbose_name='企业名称')

    class Meta:
        db_table = 'db_poll'
        verbose_name = '企业信息表'
        verbose_name_plural = verbose_name
