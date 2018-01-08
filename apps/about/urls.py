from django.conf.urls import url
from apps.home.views import about_home


urlpatterns = [
    url(r'^$', about_home, name='about')
]
