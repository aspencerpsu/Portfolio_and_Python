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
"""

settings_dict = {}

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_revamp.settings'
# os.environ.get("DJANGO_SETTINGS_MODULE")
def app(params=None):
	with open('/home/mrspencer/Documents/portfolio/src/portfolio_revamp/settings.py') as f:
    		exec(f.read(), settings_dict)

	return get_wsgi_application()

application = app()
