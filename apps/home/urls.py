from django.conf.urls import url
from apps.home.views import index_home


urlpatterns = [
    url(r'^$', index_home, name='home')
]
