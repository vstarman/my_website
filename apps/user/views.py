from django.shortcuts import render
from django.views.generic import View
from apps.blog.models import ArticleInfo


# /blog/
class BlogHomeView(View):
    """博客主页(列表页)"""
    def get(self, request):
        # 获取列表也数据,展示
        article_list = ArticleInfo.objects.all()[:12]
        # 组织模板
        context = {
            'article_list': article_list
        }
        return render(request, 'blog.html', context)

