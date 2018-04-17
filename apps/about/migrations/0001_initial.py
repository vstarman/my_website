# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='企业名称', max_length=100)),
            ],
            options={
                'verbose_name_plural': '企业信息表',
                'verbose_name': '企业信息表',
                'db_table': 'db_poll',
            },
        ),
    ]
