from django.db import models
from db.base_model import BaseModel


# # Create your models here.
# class ArticleInfo(BaseModel):
#     """基础文章信息
#         title:标题
#         author:作者
#         img_url:首页图片链接
#         page_view:浏览量
#         like_num:喜欢数量
#         abstract:文章摘要
#         label_id:标签外键
#     """
#
#     pass


class ArticleLabel(models.Model):
    """标签类
        label:关键字/标签
    """
    label = models.CharField(max_length=40, verbose_name='标签')

    class Meta:
        db_table = 'article_label'
        verbose_name = '文章标签表'
        verbose_name_plural = verbose_name


# class ArticleContent(BaseModel):
#     """问章详情内容
#         article_id:文章信息外键约束
#         content:文本内容
#     """
#     # content = HTMLField(blank=True, verbose_name='文章详情')
#     # article_id
#     pass
#
#
# class ArticleComment():
#     """
#         content_id:文章id
#         comment:评论
#     """
#     pass
