"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),    # 富文本编辑器
    url(r'^tinymce/', include('tinymce.urls')),    # 博客
    url(r'^tinymce/', include('apps.user.urls', namespace='user')),    # 用户
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),    # 首页
    url(r'^home/', include('apps.home.urls', namespace='home')),    # 文件
    url(r'^portfolio/', include('apps.portfolio.urls', namespace='portfolio')),    # 更多详情
    url(r'^about/', include('apps.about.urls', namespace='about')),    # 联系地址
    url(r'^contact/', include('apps.contact.urls', namespace='contact')),
]
