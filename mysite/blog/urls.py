from django.conf.urls import *
#from django.contrib import admin
from blog.views import *
   
#admin.autodiscover()

#app_name = 'blog'
urlpatterns=patterns('blog.views', 
	url(r'^$', index),
	url(r'^(?P<slug>[\w\-]+)/$', post),)

'''
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blog.views.index),
    url(r'^(?P<slug>[\w\-]+)/$', blog.views.post),
]
'''

'''
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
'''