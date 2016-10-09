from django.conf import settings
from django.core.urlresolvers import reverse_lazy


LIMITER_TEMPLATE_NAME = getattr(settings, 'LIMITER_TEMPLATE_NAME', 'django_limiter/set_cookie.html')
LIMITER_COOKIE_NAME = getattr(settings, 'LIMITER_COOKIE_NAME', 'limiter')
LIMITER_INTERVAL = getattr(settings, 'LIMITER_INTERVAL', 0.333)
LIMITER_EXCEPT = getattr(settings, 'LIMITER_EXCEPT', [])
SET_COOKIE_URL = reverse_lazy('limiter:set_cookie')
LIMITER_EXCEPT.append(SET_COOKIE_URL)

LIMITER_EXCEPT.append(settings.MEDIA_URL)
LIMITER_EXCEPT.append(settings.STATIC_URL)
