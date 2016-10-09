from django.views.generic import TemplateView

from .settings import LIMITER_INTERVAL, LIMITER_TEMPLATE_NAME


class SetCookieView(TemplateView):
    template_name = LIMITER_TEMPLATE_NAME

    def get_context_data(self, **kwargs):
        return {
            'timeout': int(LIMITER_INTERVAL * 1000) + 10,
            'path': self.request.GET.get('next', '/'),
            'request': self.request
        }


set_cookie_view = SetCookieView.as_view()
