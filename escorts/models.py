# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_str
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
from django.contrib.auth.models import User

import os


class Pais(models.Model):
    pa_slug = models.CharField(primary_key=True, max_length=10)
    pa_nombre = models.CharField(max_length=30)

    def __str__(self):
        return smart_str(self.pa_nombre)


class Provincia(models.Model):
    pr_slug = models.CharField(primary_key=True, max_length=10)
    pr_pais = models.ForeignKey('Pais', default='', null=True, blank=True)
    pr_nombre = models.CharField(max_length=30)

    def __str__(self):
        return smart_str(self.pr_nombre)

    def _get_number_escorts(self):
        "Devuelve el la cantidad de escorts"
        n = Escort.objects.filter(es_pais=self.pr_pais,es_provincia=self).count()
        temp = n
        return temp

    number_escorts = property(_get_number_escorts)


class Ciudad(models.Model):
    cd_slug = models.CharField(primary_key=True, max_length=10)
    cd_pais = models.ForeignKey('Pais', default='SP')
    cd_provincia = models.ForeignKey('Provincia', default='', null=True, blank=True)
    cd_nombre = models.CharField(max_length=30)

    def __str__(self):
        return smart_str(self.cd_nombre)

    def _get_number_escorts(self):
        "Devuelve el la cantidad de escorts"
        n = Escort.objects.filter(es_pais=self.cd_pais,es_provincia=self.cd_provincia,es_ciudad=self).count()
        temp = n
        return temp

    number_escorts = property(_get_number_escorts)


class Escort(models.Model):
    es_slug = models.CharField(max_length=15)
    es_user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="profile")
    es_pais = models.ForeignKey('Pais', blank=True, null=True)
    es_provincia = models.ForeignKey('Provincia', blank=True, null=True)
    es_ciudad = models.ForeignKey('Ciudad', blank=True, null=True)
    es_nombre = models.CharField(max_length=30)
    es_apellido = models.CharField(max_length=30)
    es_descripcion = models.TextField(blank=True, null=True, default='')
    es_telefono = models.CharField(max_length=12, blank=True, null=True, default='')
    es_correo = models.CharField(max_length=30, blank=True, null=True, default='')

    def __str__(self):
        return "%s (%s)" % (smart_str(self.es_nombre), self.es_user.username)

    def _get_full_name(self):
        "Devuelve el nombre completo"
        temp = '%s %s' % (self.es_nombre, self.es_apellido)
        return temp

    full_name = property(_get_full_name)

    def _get_ruta_carpeta(self):
        "Devuelve la ruta de la carpeta de imagenes"
        url = settings.BASE_DIR + '/escorts' + static('imagenes')
        temp = '%s/%s/%s' % (url, self.es_pais.pk, self.es_user.username)
        return temp

    full_ruta_carpeta = property(_get_ruta_carpeta)

    def _get_full_ruta_foto_1(self):
        ruta = self.full_ruta_carpeta + '/img_ppal'
        listaFotos = os.listdir(ruta)
        if listaFotos:
            try:
                return 'imagenes/' + self.es_pais.pk + '/' + self.es_user.username + '/img_ppal/' + listaFotos[0]
            except:
                return ''
        else:
            return ''

    full_ruta_foto_1 = property(_get_full_ruta_foto_1)

    def _get_full_ruta_foto_2(self):
        ruta = self.full_ruta_carpeta + '/img_sec'
        listaFotos = os.listdir(ruta)
        if listaFotos:
            try:
                return 'imagenes/' + self.es_pais.pk + '/' + self.es_user.username + '/img_sec/' + listaFotos[0]
            except:
                return ''
        else:
            return ''

    full_ruta_foto_2 = property(_get_full_ruta_foto_2)

    def _get_full_ruta_foto_3(self):
        ruta = self.full_ruta_carpeta + '/img_sec'
        listaFotos = os.listdir(ruta)
        if listaFotos:
            try:
                return 'imagenes/' + self.es_pais.pk + '/' + self.es_user.username + '/img_sec/' + listaFotos[1]
            except:
                return ''
        else:
            return ''

    full_ruta_foto_3 = property(_get_full_ruta_foto_3)

    def _get_full_ruta_foto_4(self):
        ruta = self.full_ruta_carpeta + '/img_sec'
        listaFotos = os.listdir(ruta)
        if listaFotos:
            try:
                return 'imagenes/' + self.es_pais.pk + '/' + self.es_user.username + '/img_sec/' + listaFotos[2]
            except:
                return ''
        else:
            return ''

    full_ruta_foto_4 = property(_get_full_ruta_foto_4)

    def _get_full_ruta_foto_5(self):
        ruta = self.full_ruta_carpeta + '/img_sec'
        listaFotos = os.listdir(ruta)
        if listaFotos:
            try:
                return 'imagenes/' + self.es_pais.pk + '/' + self.es_user.username + '/img_sec/' + listaFotos[3]
            except:
                return ''
        else:
            return ''

    full_ruta_foto_5 = property(_get_full_ruta_foto_5)


class Servicios(models.Model):
    sv_pais = models.ForeignKey('Pais', blank=True, null=True)
    sv_nombre = models.CharField(max_length=30)

    def __str__(self):
        return smart_str(self.sv_nombre)


class Duracion(models.Model):
    du_nombre = models.CharField(max_length=30)

    def __str__(self):
        return smart_str(self.du_nombre)


class ServiciosEscort(models.Model):
    se_servicio = models.ForeignKey('Servicios', blank=True, null=True)
    se_duracion = models.ForeignKey('Duracion', blank=True, null=True)
    se_precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (smart_str(self.se_servicio), smart_str(self.se_duracion.du_nombre))


class HestiaInfo(models.Model):
    hi_carrusel_cantidad = models.IntegerField(default=3)
    hi_carrusel_1_titulo = models.CharField(max_length=100, null=True, blank=True, default='')
    hi_carrusel_1_descripcion = models.CharField(max_length=100, null=True, blank=True, default='')
    hi_carrusel_2_titulo = models.CharField(max_length=100, null=True, blank=True, default='')
    hi_carrusel_2_descripcion = models.CharField(max_length=100, null=True, blank=True, default='')
    hi_carrusel_3_titulo = models.CharField(max_length=100, null=True, blank=True, default='')
    hi_carrusel_3_descripcion = models.CharField(max_length=100, null=True, blank=True, default='')
    hi_pais = models.ForeignKey('Pais', blank=True, null=True, default='SP')

    def _get_ruta_carpeta(self):
        "Devuelve la ruta de la carpeta de imagenes"
        url = settings.BASE_DIR + '/escorts' + static('imagenes')
        temp = '%s/%s/%s' % (url, self.hi_pais.pk, 'hestia')
        return temp

    full_ruta_carpeta = property(_get_ruta_carpeta)

    def _get_full_ruta_foto_carrusel(self):
        ruta = self.full_ruta_carpeta + '/carrusel'
        listaFotos = os.listdir(ruta)
        fotosCarrusel = []
        if listaFotos:
            for foto in listaFotos:
                fotosCarrusel.append('imagenes/' + self.hi_pais.pk + '/hestia/carrusel/' + foto)

        return fotosCarrusel

    fotos_carrusel = property(_get_full_ruta_foto_carrusel)
