

from .base import *



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

print(SECRET_KEY)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carne',
        'HOST':'localhost',
        'PORT':'5432',
        'USER': 'florm2496',
        'PASSWORD':'pan1994245',
    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

#STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


STATIICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

db_from_env=dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)