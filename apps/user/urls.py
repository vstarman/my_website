from django.conf.urls import url
from apps.user.views import LoginView, RegisterView, UserHome


urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'register$', RegisterView.as_view(), name='register'),
    url(r'home$', UserHome.as_view(), name='home'),
]
