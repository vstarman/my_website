from django.conf.urls import url
from apps.home.views import contact_home


urlpatterns = [
    url(r'^$', contact_home, name='contact')
]
