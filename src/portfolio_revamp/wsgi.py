"""
WSGI config for portfolio_revamp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


"""
Use this config file in your script like this:
$ gunicorn project_name.wsgi:application -c read_django_settings.py
You need to replace the exec() call if you want it to work on Python 2.

May use for later
"""

settings_dict = {}

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_revamp.settings'
# os.environ.get("DJANGO_SETTINGS_MODULE")

application = get_wsgi_application()
