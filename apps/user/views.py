from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from apps.blog.models import ArticleInfo


# /blog/
class LoginView(View):
    """登录页"""
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        """处理登录"""
        phone = request.POST.get('phone')
        password = request.POST.get('pwd')
        if not all([password, phone]):
            pass
        return redirect(reverse('user:home'))


class RegisterView(View):
    """注册页"""
    def get(self, request):
        """注册处理"""
        return render(request, 'register.html')
    
    def post(self, request):
        """注册处理"""
        name = request.POST.get('user_name')
        password = request.POST.get('pwd')
        re_password = request.POST.get('re_pwd')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print([name, password, re_password, email, phone])
        if not all([name, password, re_password, email, phone]):
            pass

        return redirect(reverse('user:login'))


class UserHome(View):
    """个人页"""

    def get(self, request):
        """注册处理"""
        return render(request, 'index.html')

    def post(self, request):
        """注册处理"""

        return redirect(reverse('user:login'))