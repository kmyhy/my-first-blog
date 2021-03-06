from django.conf.urls import include, url
from django.contrib import admin
from trips.views import hello_world

import django.contrib.auth.views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('blog.urls')),
    url(r'^accounts/login/$',django.contrib.auth.views.login,name='login'),
    url(r'^accounts/logout/$',django.contrib.auth.views.logout,name='logout',kwargs={'next_page':'/'}),
    url(r'^trips/',include('trips.urls')),
]
