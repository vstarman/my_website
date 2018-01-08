from django.conf.urls import url
from apps.blog.views import about_home


urlpatterns = [
    url(r'^$', about_home, name='about')
]
