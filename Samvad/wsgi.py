"""
WSGI config for Samvad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

setting_module = 'Samvad.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'Samvad.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Samvad.settings')

application = get_wsgi_application()
