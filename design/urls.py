from django.conf.urls import patterns, url
from .views import IndexView, TimelineView, AccionableView

urlpatterns = patterns('',
    url(r'^index/', view=IndexView.as_view(), name='maqueta'),
    url(r'^timeline/', view=TimelineView.as_view(), name='timeline'),
    url(r'^accionable/', view=AccionableView.as_view(), name='accionable'),
    url(r'^acumulados/(?P<pk>\d+)/$', 'design.views.Acumulados', name='acumulados'),
    url(r'^chat/', view='design.views.chat', name='chat'),
)
