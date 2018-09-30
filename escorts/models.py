# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_str, smart_unicode
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings

import os

class Pais(models.Model):
    pa_slug = models.CharField(primary_key=True,max_length=10)
    pa_nombre = models.CharField( max_length=30)

    def __str__(self):
        return smart_str(self.pa_nombre)

class Provincia(models.Model):
    pr_slug=models.CharField(primary_key=True,max_length=10)
    pr_pais = models.ForeignKey('Pais', default='SP')
    pr_nombre = models.CharField( max_length=30)

    def __str__(self):
        return smart_str(self.pr_nombre)

class Escort(models.Model):
    es_slug=models.CharField(max_length=15)
    es_user=models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="profile")
    es_pais=models.ForeignKey('Pais', blank=True, null=True)
    es_provincia=models.ForeignKey('Provincia', blank=True, null=True)
    es_nombre = models.CharField( max_length=30)
    es_apellido = models.CharField( max_length=30)
    es_descripcion = models.TextField(blank=True,null=True,default='')

    def __str__(self):
        return "%s (%s)" % (unicode(self.es_nombre),self.es_user.username)

    def _get_full_name(self):
        "Devuelve el nombre completo"
        temp= '%s %s' % (self.es_nombre,self.es_apellido)
        return temp

    full_name = property(_get_full_name)

    def _get_ruta_carpeta(self):
        "Devuelve la ruta de la carpeta de imagenes"
        url='../proyecto_escorts/escorts/static/imagenes'
        temp= '%s/%s/%s' % (url,self.es_pais.pk,self.es_user.username)
        return temp

    full_ruta_carpeta = property(_get_ruta_carpeta)

    def _get_full_ruta_foto_1(self):
        ruta=self.full_ruta_carpeta+'/img_ppal'
        listaFotos=os.listdir(ruta)
        if listaFotos:
            return 'imagenes/'+self.es_pais.pk+'/'+self.es_user.username+'/img_ppal/'+listaFotos[0]
        else:
            return None

    full_ruta_foto_1 = property(_get_full_ruta_foto_1)

class Servicios(models.Model):
    sv_pais = models.ForeignKey('Pais', blank=True, null=True)
    sv_nombre=models.CharField( max_length=30)

    def __str__(self):
        return unicode(self.sv_nombre)


class Duracion(models.Model):
    du_nombre=models.CharField( max_length=30)

    def __str__(self):
        return unicode(self.du_nombre)


class ServiciosEscort(models.Model):
    se_servicio = models.ForeignKey('Servicios', blank=True, null=True)
    se_duracion = models.ForeignKey('Duracion', blank=True, null=True)
    se_precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (unicode(self.se_servicio), unicode(self.se_duracion.du_nombre))
