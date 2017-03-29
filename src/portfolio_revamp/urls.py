"""portfolio_revamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

"""

import sys 
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

#import everything from the main app src's url constructor.

from portfolio_revamp.views import *

import settings
from django.conf.urls import handler404, handler500
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

sys.dont_write_bytecode = True

urlpatterns = [ url(r'^admin/', include(admin.site.urls)), 
	        url(r'^posts/', include("posts.urls", namespace='posts')),	
		url(r'^thebigday/', include("weddings.urls", namespace="weddings")),
		url(r'^$', main),
		url(r'^what-we-do/$', about),
		url(r'^contacts/$', contacts),
		url(r'^tools', tools),
		url(r'^about-us', us),
		url(r'^considerations', considerations),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

#urlpatterns.append(url(r'^media/(?P<path>.*)$', include("../ ))
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "portfolio_revamp.views.page_cannot_load"
