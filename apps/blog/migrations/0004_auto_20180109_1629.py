# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_articleinfo_content_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecontent',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='articlecontent',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='articlecontent',
            name='update_time',
        ),
    ]
