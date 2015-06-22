from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^bank/',include('bank.urls', namespace='bank')),    
    #url(r'^search/', include('bank.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# htt://www.ghfgh.com/loc/jhgg