from django.conf.urls import patterns, url
from .views import EstadoResultado, EstadoResultadoFiltro

urlpatterns = patterns('',
    url(r'^eerr/$', view=EstadoResultado.as_view(), name='home'),
    url(r'^eerr/(?P<pk>\d+)/$', view=EstadoResultadoFiltro.as_view(), name='eerr_filtro'),
    url(r'^carga_margen_acumulado/$', 'financials.views.carga_margen_acumulado', name='carga_margen_acumulado'),
    url(r'^carga_costo_venta/$', 'financials.views.carga_costo_venta', name='carga_costo_venta'),
    url(r'^carga_margen_acumulado_filtro/(?P<pk>\d+)/$', 'financials.views.carga_margen_acumulado_filtro', name='carga_margen_acumulado_filtro'),
    url(r'^carga_costo_venta_filtro/(?P<pk>\d+)/$', 'financials.views.carga_costo_venta_filtro', name='carga_costo_venta_filtro'),
    url(r'^hash_tipoCliente/$', 'financials.views.hash_tipoCliente', name='hash_tipoCliente'),
    url(r'^hash_tipoCliente_filtro/(?P<pk>\d+)/$', 'financials.views.hash_tipoCliente_filtro', name='hash_tipoCliente_filtro'),
    url(r'^hash_sector/$', 'financials.views.hash_sector', name='hash_sector'),
    url(r'^hash_sector_filtro/(?P<pk>\d+)/$', 'financials.views.hash_sector_filtro', name='hash_sector_filtro'),
    url(r'^hash_tipoClienteSector/$', 'financials.views.hash_tipoClienteSector', name='hash_tipoClienteSector'),
    url(r'^hash_tipoClienteSector_filtro/(?P<pk>\d+)/$', 'financials.views.hash_tipoClienteSector_filtro', name='hash_tipoClienteSector_filtro'),
    url(r'^hash_sectores/$', 'financials.views.hash_sectores', name='hash_sectores'),
    url(r'^hash_sectores_filtro/(?P<pk>\d+)/$', 'financials.views.hash_sectores_filtro', name='hash_sectores_filtro'),
)
