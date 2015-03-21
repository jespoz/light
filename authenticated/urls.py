from django.conf.urls import url, patterns
from views import *

urlpatterns = patterns('',
    url(r'^logout/$', 'authenticated.views.logout', name='logout'),
)
