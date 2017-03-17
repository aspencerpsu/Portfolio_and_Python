from django.conf.urls import url

from .views import *

urlpatterns = [
                url(r'^$', wedding_create, name='wedding_info')
              ]
