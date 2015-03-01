from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^mapp/$',views.login,name='login'),
    url(r'^login/$',views.login,name='login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^regist/$',views.regist,name='regist'),
    #url(r'^registm/$',views.registm,name='registm'),
)
