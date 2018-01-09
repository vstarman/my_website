# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('comment', models.CharField(max_length=500, verbose_name='文章评论')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'db_table': 'article_comment',
            },
        ),
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('content', tinymce.models.HTMLField(verbose_name='文章详情', blank=True)),
            ],
            options={
                'verbose_name': '文章详情内容',
                'verbose_name_plural': '文章详情内容',
                'db_table': 'article_content',
            },
        ),
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('img_url', models.CharField(max_length=256, verbose_name='首页图片链接')),
                ('page_view', models.IntegerField(default=0, verbose_name='浏览量')),
                ('like_num', models.IntegerField(default=0, verbose_name='喜欢数量')),
                ('abstract', models.CharField(max_length=256, verbose_name='文章摘要')),
                ('label', models.CharField(max_length=40, verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章列表页信息',
                'verbose_name_plural': '文章列表页信息',
                'db_table': 'article_info',
            },
        ),
        migrations.DeleteModel(
            name='ArticleLabel',
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='article_id',
            field=models.ForeignKey(verbose_name='文章简介外键', to='blog.ArticleInfo'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='content_id',
            field=models.ForeignKey(verbose_name='文章评论', to='blog.ArticleContent'),
        ),
    ]
