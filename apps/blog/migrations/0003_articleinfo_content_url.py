# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180109_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleinfo',
            name='content_url',
            field=models.CharField(verbose_name='文章原始链接', max_length=256, default=datetime.datetime(2018, 1, 9, 8, 27, 45, 129048, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
