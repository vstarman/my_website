# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('label', models.CharField(verbose_name='标签', max_length=40)),
            ],
            options={
                'verbose_name': '文章标签表',
                'verbose_name_plural': '文章标签表',
                'db_table': 'article_label',
            },
        ),
    ]
