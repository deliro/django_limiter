from setuptools import setup

setup(
    name='django_limiter',
    description='Signed Cookie based limiting RPS module for Django',
    keywords='django rps limit',
    py_modules=['django_limiter'],
    version='1.0.0',
    author='Roman Kitaev',
    author_email='t4k.kitaetz@gmail.com',
    url='https://github.com/deliro/django_limiter',
    license='BSD',
    install_requires=[
        'django>=1.8,<1.11',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
    ],
)