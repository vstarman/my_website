from django.conf.urls import url
from apps.about.views import about_home


urlpatterns = [
    url(r'^$', about_home, name='about')
]
