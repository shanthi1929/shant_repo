from django.conf.urls import patterns, include, url
from bank import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beginner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index)
    #url(r'^$', views.base),
    # url(r'^detail/$', views.myviewclass.detail, name='detail'),  
    #url(r'^$', views.search),
    url(r'^$', views.main_page),  
    url(r'^register/$', views.register_page, name="register"),
    url(r'^register_check/$', views.register_check, name="register_check"),
    url(r'^login/$', views.login_page, name="login"),
    # url(r'^register_success/$', views.register_success, name="regis_success"),  
    #url(r'^account/$', views.account_page),
    url(r'^account_page/$', views.account_page, name='account_page'),
    url(r'^create_page/$', views.create_page, name='create_page'),
    url(r'^modify_page/$', views.modify_page, name='modify_page'),
    url(r'^delete_page/$', views.delete_page, name='delete_page'),




    # url(r'^register/',include('bank.urls')),
)
