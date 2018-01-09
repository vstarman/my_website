# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180109_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleinfo',
            name='abstract',
            field=models.CharField(verbose_name='文章摘要', max_length=500),
        ),
        migrations.AlterField(
            model_name='articleinfo',
            name='author',
            field=models.CharField(default='', verbose_name='作者', max_length=20),
        ),
        migrations.AlterField(
            model_name='articleinfo',
            name='label',
            field=models.CharField(default='', verbose_name='标签', max_length=40),
        ),
    ]
