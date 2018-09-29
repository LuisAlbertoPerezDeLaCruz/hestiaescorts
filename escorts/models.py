# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Pais(models.Model):
    pa_slug = models.CharField(primary_key=True,max_length=10)
    pa_nombre = models.CharField( max_length=30)

    def __unicode__(self): return "%s" % (unicode(self.pa_nombre))


class Provincia(models.Model):
    pr_slug=models.CharField(primary_key=True,max_length=10)
    pr_pais = models.ForeignKey('Pais', default='SP')
    pr_nombre = models.CharField( max_length=30)

    def __unicode__(self): return "%s" % (unicode(self.pr_nombre))

class Escort(models.Model):
    es_slug=models.CharField(max_length=15)
    es_user=models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="profile")
    es_pais=models.ForeignKey('Pais', blank=True, null=True)
    es_provincia=models.ForeignKey('Provincia', blank=True, null=True)
    es_nombre = models.CharField( max_length=30)
    es_apellido = models.CharField( max_length=30)
    es_descripcion = models.TextField(blank=True,null=True,default='')
    es_foto_1 =  models.CharField(max_length=100, default='', null=True, blank=True)

    def __unicode__(self): return "%s (%s)" % (unicode(self.es_nombre),self.es_user.username)

    def _get_full_name(self):
        "Devuelve el nombre completo"
        temp= '%s %s' % (self.es_nombre,self.es_apellido)
        return temp

    full_name = property(_get_full_name)

    def _get_ruta_foto_1(self):
        "Devuelve el nombre completo"
        temp= '%s/%s/%s/%s' % ('imagenes',self.es_pais.pk,self.es_slug,self.es_foto_1)
        return temp

    full_ruta_foto_1 = property(_get_ruta_foto_1)

class Servicios(models.Model):
    sv_pais = models.ForeignKey('Pais', blank=True, null=True)
    sv_nombre=models.CharField( max_length=30)

    def __unicode__(self): return "%s" % (unicode(self.sv_nombre))

class Duracion(models.Model):
    du_nombre=models.CharField( max_length=30)

    def __unicode__(self): return "%s" % (unicode(self.du_nombre))

class ServiciosEscort(models.Model):
    se_servicio = models.ForeignKey('Servicios', blank=True, null=True)
    se_duracion = models.ForeignKey('Duracion', blank=True, null=True)
    se_precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self): return "%s %s" % (unicode(self.se_servicio),unicode(self.se_duracion.du_nombre))