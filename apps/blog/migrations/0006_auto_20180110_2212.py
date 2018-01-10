# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180109_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleinfo',
            options={'verbose_name': '文章列表页', 'verbose_name_plural': '文章列表页'},
        ),
    ]
