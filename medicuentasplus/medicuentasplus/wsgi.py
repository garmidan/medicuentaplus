"""
WSGI config for medicuentasplus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicuentasplus.settings')
application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(settings.BASE_DIR, 'staticfiles'))
