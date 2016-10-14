#!/usr/bin/env python
import sys
import os
from django.conf.__init__ import LazySettings
#from django.conf.__init__ import BaseSettings
#from django.conf.__init__ import Settings
#from django.conf.__init__ import UserSettingsHolder
from django.core.management import execute_from_command_line

settings = LazySettings()
if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_revamp.settings")
	#import django
	#django.setup()
    	settings.configure()
    	execute_from_command_line(sys.argv)
