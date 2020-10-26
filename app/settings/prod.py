from .base import *



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'HOST':'localhost',
        'PORT':'5432',
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

#STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'