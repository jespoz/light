from django.conf.urls import patterns, url
from .views import ImportReport

urlpatterns = patterns('',

    url(r'^reports/$', view=ImportReport.as_view(), name='reports'),
    url(r'^reports/import/(?P<pk>\d+)/$', view='imports.views.import_file', name='import'),
    url(r'^reports/data_exist/1/(?P<pk>\d+)/$', view='imports.views.data_exist_eerr', name='data_exist_eerr'),
    url(r'^reports/data_exist/2/(?P<pk>\d+)/$', view='imports.views.data_exist_pp_vs_zn', name='data_exist_pp_vs_zn'),
    url(r'^reports/data_exist/3/(?P<pk>\d+)/$', view='imports.views.data_exist_precio_desc', name='data_exist_precio_desc'),
    url(r'^reports/data_exist/4/(?P<pk>\d+)/$', view='imports.views.data_exist_unit', name='data_exist_unit'),
    url(r'^reports/data_exist/5/(?P<pk>\d+)/$', view='imports.views.data_exist_formula_ingreso', name='data_exist_formula_ingreso'),
)
