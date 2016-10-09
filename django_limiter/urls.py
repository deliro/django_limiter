from django.conf.urls import url
from .views import set_cookie_view


urlpatterns = [
    url(r'set-cookie/$', set_cookie_view, name='set_cookie')
]
