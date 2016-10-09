from time import time

from django.http import HttpResponse
from django.utils.http import urlencode
from django.shortcuts import redirect

from .settings import LIMITER_COOKIE_NAME, SET_COOKIE_URL, LIMITER_EXCEPT, LIMITER_INTERVAL

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    MiddlewareMixin = object


# cast lazy objects
LIMITER_EXCEPT = tuple(str(i) for i in LIMITER_EXCEPT if str(i).startswith('/'))


class RateLimiter(MiddlewareMixin):
    @staticmethod
    def process_response(request, response):
        response.set_signed_cookie(LIMITER_COOKIE_NAME, time())
        return response

    @staticmethod
    def process_request(request):
        if request.path.startswith(LIMITER_EXCEPT):
            return
        now = time()
        cookie = request.get_signed_cookie(LIMITER_COOKIE_NAME, None)

        if cookie is None:
            params = urlencode({'next': request.get_full_path()})
            return redirect('%s?%s' % (SET_COOKIE_URL, params))

        if callable(LIMITER_INTERVAL):
            interval = LIMITER_INTERVAL(request)
        else:
            interval = LIMITER_INTERVAL

        if float(cookie) + interval > now:
            return HttpResponse('Too Many Requests', status=429)
