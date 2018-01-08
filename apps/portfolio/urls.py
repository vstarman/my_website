from django.conf.urls import url
from apps.blog.views import portfolio_home


urlpatterns = [
    url(r'^$', portfolio_home, name='portfolio')
]
