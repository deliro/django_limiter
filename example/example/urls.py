from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
import django_limiter

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lambda x: HttpResponse('hello')),
    url(r'^limiter/', include(django_limiter.urls)),
]
