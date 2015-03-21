from django.db import models
from django.contrib.auth.models import User

class Indicador(models.Model):
    indicador = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Indicadores'

    def __unicode__(self):
        return self.indicador

class Visualizacion(models.Model):
    indicador = models.ForeignKey(Indicador)
    resultado = models.FloatField(default=0)
    analista = models.ForeignKey(User, related_name='analista')
    actualizacion = models.DateTimeField(auto_now_add=True, blank=True)
    periodo = models.CharField(max_length=20)
    visualizacion = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, related_name='usuario')

    class Meta:
        verbose_name_plural = 'Visualizaciones'

    def __unicode__(self):
        return self.indicador
