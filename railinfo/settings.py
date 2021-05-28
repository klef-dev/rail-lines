SECRET_KEY = 'django-insecure-w$^^5qo!btbc0b%uta)wl)7aykn1d@eyuhi!cd1@7n*-oz4jpq'

DEBUG = False

ALLOWED_HOSTS = ["lanternrail.herokuapp.com", "127.0.0.1", "localhost"]

ROOT_URLCONF = 'railinfo.urls'

WSGI_APPLICATION = 'railinfo.wsgi.application'

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]