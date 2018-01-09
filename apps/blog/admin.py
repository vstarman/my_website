from django.contrib import admin
from apps.blog import models
# Register your models here.


admin.site.register(models.ArticleComment)
admin.site.register(models.ArticleContent)
admin.site.register(models.ArticleInfo)
