from django.db import models
from db.base_model import BaseModel


# Create your models here.
class ArticleInfo(BaseModel):
    """
    base_model:
        create_time:创建时间
        update_time:更新时间
        is_delete:是否删除
    ArticleInfo:
        title:标题
        author:作者
        img_url:首页图片链接
        page_view:浏览量
        label:关键字标签
        abstract:文章摘要
    ArticleDetail:
        content:文本内容
        comment:评论
    """
    pass


class ArticleDetail(BaseModel):
    pass
