==============
Django Limiter
==============

.. image::
    https://img.shields.io/pypi/v/django_limiter.svg
    :target: https://pypi.python.org/pypi/django_limiter

Django Limiter is a Signed Cookie based RPS (Requests per second) limiter.


How it works?
=============
If a user (or a parser) visits your site first time, he redirected to the special page and
receives an signed cookie with current timestamp. On this page he will be redirected by JavaScript to the URL
he requested before.

If a user visits your site with Limiter's cookie, Limiter checks the cookie and if the last request had little time,
Limiter throws HTTP Response with 429 status code (Too Many Requests)

Otherwise nothing will happen.

Client can't properly change Limiter's cookie and abuse (read more about signing here: https://docs.djangoproject.com/en/dev/topics/signing/)

Installation
============
Install from PyPI:

.. code-block::

    $ pip install django_limiter


Append ``'django_limiter'`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # your apps
        'django_limiter',
    ]

Insert ``'django_limiter.middleware.RateLimiter'`` **BEFORE** any other middleware into ``MIDDLEWARE`` setting (or ``MIDDLEWARE_CLASSES``):

.. code-block:: python

    MIDDLEWARE = [
        'django_limiter.middleware.RateLimiter',
        # Another middlewares
    ]

Add ``url(r'^limiter/', include(django_limiter.urls))`` to your url config:

.. code-block:: python

    import django_limiter

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        # Another url patterns
        url(r'^limiter/', include(django_limiter.urls)),
    ]

Configuration
=============
Here is several settings you can set:

``LIMITER_COOKIE_NAME`` — The name of the cookie. Default: **'limiter'**

``LIMITER_INTERVAL`` — The time (in seconds, can be float) client must wait before he can send next request. Default: **0.333**

``LIMITER_TEMPLATE_NAME`` — The name of the template for page to which the client gets temporarily. This page should redirect client to requested page after ``LIMITER_INTERVAL`` seconds pass. Template receives ``'timeout'``, ``'path'`` and ``'request'`` context.

``LIMITER_EXCEPT`` — List of URLs Limiter must except. You shouldn't add root (``'/'``) into this list. Default: **[]**

.. code-block:: python

    LIMITER_EXCEPT = ['/my/custom/path', reverse_lazy('or-lazy-reverse')]
