from django.conf.urls import url
from apps.blog.views import BlogHomeView


urlpatterns = [
    url(r'^$', BlogHomeView.as_view(), name='blog')
]
