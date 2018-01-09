from django.shortcuts import render
from django.views.generic import View
from apps.blog.models import ArticleInfo


# /blog/
class BlogHomeView(View):
    """博客主页(列表页)"""
    def get(self, request):
        return render(request, 'blog.html')

