from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beginner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index)
    #url(r'^$', views.base),
    # url(r'^detail/$', views.myviewclass.detail, name='detail'),  
    #url(r'^$', views.search),
    url(r'^$', views.main_page),  
    url(r'^$', views.register_page),
)
