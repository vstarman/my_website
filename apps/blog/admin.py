from django.contrib import admin
from apps.blog import models
# Register your models here.


class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'label', 'page_view']


admin.site.register(models.ArticleComment)
admin.site.register(models.ArticleContent)
admin.site.register(models.ArticleInfo, ArticleInfoAdmin)
