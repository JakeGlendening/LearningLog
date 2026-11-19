import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_log.settings')
from django.core.asgi import get_asgi_application
application=get_asgi_application()
