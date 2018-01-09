from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField


# Create your models here.
class ArticleInfo(BaseModel):
    """文章列表页信息
        title:标题
        author:作者
        img_url:首页图片链接
        page_view:浏览量
        like_num:喜欢数量
        abstract:文章摘要
        label_id:标签外键
    """
    title = models.CharField(max_length=40, verbose_name='标题')
    author = models.CharField(max_length=20, verbose_name='作者')
    img_url = models.CharField(max_length=256, verbose_name='首页图片链接')
    page_view = models.IntegerField(default=0, verbose_name='浏览量')
    like_num = models.IntegerField(default=0, verbose_name='喜欢数量')
    abstract = models.CharField(max_length=256, verbose_name='文章摘要')
    label = models.CharField(max_length=40, verbose_name='标签')

    class Meta:
        db_table = 'article_info'
        verbose_name = '文章列表页信息'
        verbose_name_plural = verbose_name


class ArticleContent(BaseModel):
    """文章详情内容
        article_id:文章信息外键约束
        content:文本内容
    """
    content = HTMLField(blank=True, verbose_name='文章详情')
    article_id = models.ForeignKey('ArticleInfo', verbose_name='文章简介外键')

    class Meta:
        db_table = 'article_content'
        verbose_name = '文章详情内容'
        verbose_name_plural = verbose_name


class ArticleComment(BaseModel):
    """文章评论(以后存到redis中)
        content_id:文章id
        comment:评论
    """
    content_id = models.ForeignKey('ArticleContent', verbose_name='文章评论')
    comment = models.CharField(max_length=500, verbose_name='文章评论')

    class Meta:
        db_table = 'article_comment'
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
