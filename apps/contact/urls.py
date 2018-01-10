from django.conf.urls import url
from apps.contact.views import contact_home


urlpatterns = [
    url(r'^$', contact_home, name='contact')
]
