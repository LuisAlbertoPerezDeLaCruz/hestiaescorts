# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .views import *

class PerfilEscort:
    """Facilita el despliegue de informacion en template del perfil de la escort"""

    def __init__(self, escortId):
        self.escortId = escortId
        self.escortSlug = None
        self.escortNombre = None
        self.escortDescripcion = None
        self.escortTelefono = None
        self.escortPais = None
        self.escortProvincia = None
        self.escortCiudad = None
        self.escortCaracteristicas = None
        self.escortServicios = None

        self.cargaInfoEscort()

    def cargaInfoEscort(self):
        escort= Escort.objects.get(id=self.escortId)
        self.escortSlug = escort.es_slug
        self.escortNombre = escort.es_nombre
        self.escortDescripcion = escort.es_descripcion
        self.escortTelefono = escort.es_telefono
        self.escortPais = escort.es_pais.pa_nombre
        self.escortProvincia = escort.es_provincia.pr_nombre
        self.escortCiudad = escort.es_ciudad.cd_nombre
        caracteristicas=CaracteristicasEscort.objects.filter(ce_escort=escort)
        aca=[]
        for caracteristica in caracteristicas:
            cJson={}
            cJson['caracteristicaNombre']=caracteristica.ce_caracteristica.ca_nombre
            aca.append(cJson)
        self.escortCaracteristicas = aca

        servicios=ServiciosEscort.objects.filter(se_escort=escort)
        asv=[]
        for servicio in servicios:
            sJson={}
            sJson['servicioNombre']=servicio.se_servicio.sv_nombre
            sJson['servicioDuracion']=servicio.se_duracion.du_nombre
            sJson['servicioPrecio']=servicio.se_precio
            asv.append(sJson)
        self.escortServicios = asv

        return
