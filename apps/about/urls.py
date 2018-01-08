from django.conf.urls import url
from apps.blog.views import blog_home


urlpatterns = [
    url(r'^$', blog_home, name='about')
]
