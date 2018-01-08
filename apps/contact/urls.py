from django.conf.urls import url
from apps.blog.views import contact_home


urlpatterns = [
    url(r'^$', contact_home, name='contact')
]
