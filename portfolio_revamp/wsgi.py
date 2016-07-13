"""
WSGI config for portfolio_revamp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

# os.environ.get("DJANGO_SETTINGS_MODULE")
application = get_wsgi_application()