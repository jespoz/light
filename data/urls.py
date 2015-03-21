from django.conf.urls import patterns, url
from .views import FormulaIngreso, FormulaIngresoFiltro

urlpatterns = patterns('',
    url(r'^venta/$', view=FormulaIngreso.as_view(), name='formula_ingreso'),
    url(r'^venta/(?P<pk>\d+)/$', view=FormulaIngresoFiltro.as_view(), name='venta_filtro'),
    url(r'^carga_venta_acumulada/$', 'data.views.carga_ventas_acumuladas', name='carga_ventas_acumuladas'),
    url(r'^carga_venta_acumulada_filtro/(?P<pk>\d+)/$', 'data.views.carga_ventas_acumuladas_filtro', name='carga_venta_acumulada_filtro'),
)
