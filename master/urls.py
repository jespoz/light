from django.conf.urls import patterns, url
from .views import RevisionLocales

urlpatterns = patterns('',
    url(r'^revision/$', view=RevisionLocales.as_view(), name='revision_maestro'),
    url(r'^revision/update_locales_nulos/$', view='master.views.ejecutar_nulos', name='ejecutar_nulos'),
    url(r'^revision/import/$', view='master.views.import_file', name='import_file'),
)
