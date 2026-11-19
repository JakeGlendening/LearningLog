import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_log.settings')
from django.core.wsgi import get_wsgi_application
application=get_wsgi_application()
