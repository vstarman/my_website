from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from apps.user.models import User
import re


# /user/login
class LoginView(View):
    """登录页"""
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        """处理登录"""
        # TODO 验证用户
        phone = request.POST.get('phone')
        password = request.POST.get('pwd')
        if not all([password, phone]):
            pass
        return redirect(reverse('user:home'))


# TODO 登出视图
class LogoutView(View):
    pass


# /user/register TODO 定义登录校验的 LoginRequireViewMixin
class RegisterView(View):
    """注册页"""
    def get(self, request):
        """注册处理"""
        return render(request, 'register.html')
    
    def post(self, request):
        """注册处理"""
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        re_password = request.POST.get('re_pwd')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print([username, password, re_password, email, phone])
        # 数据校验
        if not all([username, password, re_password, email, phone]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱不合法'})

        if password != re_password:
            return render(request, 'register.html', {'errmsg': '两次密码不相同'})

        if re.match(r'1[\d]{10}', phone):
            return render(request, 'register.html', {'errmsg': '手机号格式错误'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户名以存在'})

        # 业务处理,注册用户
        user = User.objects.create_user(username, password, email, phone)
        user.is_active = 0
        user.save()

        # TODO celery发送手机验证码


# /user/home
class UserHome(View):
    """个人页"""

    def get(self, request):
        """注册处理"""
        # TODO 设计个人中心页
        return render(request, 'index.html')
