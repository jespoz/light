from django.conf.urls import url, patterns
from actions.views import AccLocalView, AccPrecioView

urlpatterns = patterns('',
    url(r'^accionables/locales/(?P<pk>\d+)/$', AccLocalView.as_view(), name='accionables_locales'),
    url(r'^accionables/locales/(?P<pk>\d+)/(?P<tc>\d+)/$', 'actions.views.accionable_filtro', name='accionables_locales_filtro'),
    url(r'^accionables/precios/dispersion/(?P<pk>\d+)/$', 'actions.views.dispersion_view', name='dispersion_view'),
    url(r'^accionables/precios/(?P<pk>\d+)/$', AccPrecioView.as_view(), name='accionables_precios'),
    url(r'^accionables/precios/negocio/(?P<pk>\d+)/(?P<ng>\d+)/$', 'actions.views.detalle_materiales', name='detalle_materiales'),
    url(r'^accionables/precios/negocio/apertura/(?P<pk>\d+)/(?P<mt>\d+)/$', 'actions.views.detalle_materiales_apertura', name='detalle_materiales_apertura'),
)

