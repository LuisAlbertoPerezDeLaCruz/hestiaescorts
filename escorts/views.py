# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .clases import *
import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


provincias = Provincia.objects.all().order_by('pr_nombre')
hestiaInfo = HestiaInfo.objects.all()[0]

def index(request):
    return render(request, "index.html", {'provincias':provincias,'info':hestiaInfo})

def v404(request):
    return render(request, "404.html", {'provincias':provincias})

def about(request):
    return render(request, "about.html", {'provincias':provincias})

def blog_home_1(request):
    return render(request, "blog-home-1.html", {'provincias':provincias})

def blog_home_2(request):
    return render(request, "blog-home-2.html", {'provincias':provincias})

def blog_post(request):
    return render(request, "blog-post.html", {'provincias':provincias})

def contact(request):
    return render(request, "contact.html", {'provincias':provincias})

def faq(request):
    return render(request, "faq.html", {'provincias':provincias})

def portfolio_1_col(request):
    return render(request, "portfolio-1-col.html", {'provincias':provincias})

def portfolio_2_col(request):
    return render(request, "portfolio-2-col.html", {'provincias':provincias})

def portfolio_3_col(request):
    return render(request, "portfolio-3-col.html", {'provincias':provincias})

def portfolio_4_col(request):
    return render(request, "portfolio-4-col.html", {'provincias':provincias})

def portfolio_item(request):
    return render(request, "portfolio-item.html", {'provincias':provincias})

def pricing(request):
    return render(request, "pricing.html", {'provincias':provincias})

def services(request):
    return render(request, "services.html", {'provincias':provincias})

def sidebar(request):
    return render(request, "sidebar.html", {'provincias':provincias})

def portfolio_provincia(request,pk):
    provinciaSeleccionada=Provincia.objects.get(pk=pk)

    ciudades_list=Ciudad.objects.filter(cd_pais=provinciaSeleccionada.pr_pais,cd_provincia=provinciaSeleccionada.pr_slug).order_by('cd_nombre')
    if 'ciudadSlug' in request.GET:
        ciudadSlug=request.GET['ciudadSlug']
        escorts_list=Escort.objects.filter(es_pais=provinciaSeleccionada.pr_pais,es_provincia=provinciaSeleccionada.pr_slug,es_ciudad=ciudadSlug)
    else:
        escorts_list=Escort.objects.filter(es_pais=provinciaSeleccionada.pr_pais,es_provincia=provinciaSeleccionada.pr_slug)

    page = request.GET.get('page', 1)

    paginator = Paginator(escorts_list, 12)

    try:
        escorts = paginator.page(page)
    except PageNotAnInteger:
        escorts = paginator.page(1)
    except EmptyPage:
        escorts = paginator.page(paginator.num_pages)

    return render(request, "portfolio-provincia.html", {
        'provincias':provincias,
        'provinciaSeleccionada':provinciaSeleccionada,
        'escorts':escorts,
        'ciudades':ciudades_list,
    })

def ciudad(request):
    pk=request.GET['ciudadSlug'];
    ciudadSeleccionada=Ciudad.objects.get(pk=pk)
    provinciaSeleccionada=ciudadSeleccionada.cd_provincia
    escorts_list=Escort.objects.filter(es_pais=ciudadSeleccionada.cd_pais,es_provincia=ciudadSeleccionada.cd_provincia, es_ciudad=ciudadSeleccionada)

    page = request.GET.get('page', 1)

    paginator = Paginator(escorts_list, 12)

    try:
        escorts = paginator.page(page)
    except PageNotAnInteger:
        escorts = paginator.page(1)
    except EmptyPage:
        escorts = paginator.page(paginator.num_pages)

    return render (request, "portfolio-ciudad.html", {
        'provincias':provincias,
        'provinciaSeleccionada': provinciaSeleccionada,
        'ciudadSeleccionada': ciudadSeleccionada,
        'escorts':escorts,
    })



def portfolio_escort(request,pk):
    user=User.objects.get(username=pk)
    escortSeleccionada=Escort.objects.get(es_user=user)
    provinciaSeleccionada=Provincia.objects.get(pk=escortSeleccionada.es_provincia.pk)
    perfil=PerfilEscort(escortSeleccionada.id)
    return render(request, "portfolio-escort.html", {
        'provincias': provincias,
        'provinciaSeleccionada': provinciaSeleccionada,
        'escortSeleccionada':escortSeleccionada,
        'perfil':perfil,
    })

def conf_escort(request,pk):
    if pk=='registro':
        return render(request, "conf-escort.html", {'provincias':provincias})
    user=User.objects.get(username=pk)
    escortSeleccionada=Escort.objects.get(es_user=user)
    perfil=PerfilEscort(escortSeleccionada.id)
    return render(request, "conf-escort.html", {
        'provincias': provincias,
        'escortSeleccionada':escortSeleccionada,
        'perfil': perfil,
        'caracteristicas':Caracteristica.objects.all(),
        'servicios': Servicios.objects.all(),
        'duraciones':Duracion.objects.all(),
    })

def escort_update_info(request):
    escortId=request.GET['escortId']
    escort=Escort.objects.get(id=escortId)
    nombreIn=request.GET['nombre']
    apellidoIn=request.GET['apellido']
    telefonoIn = request.GET['telefono']
    telefonoIn=filter( lambda x: x in '0123456789', telefonoIn )
    emailIn = request.GET['email']
    descripcionIn = request.GET['descripcion']
    caracteristicasIn = request.GET['caracteristicas']
    caracteristicasIn=caracteristicasIn.split(',')
    caracteristicasEscort=CaracteristicasEscort.objects.filter(ce_escort=escort)
    for caracteristicaEscort in caracteristicasEscort:
        if str(caracteristicaEscort.ce_caracteristica_id) not in caracteristicasIn:
            caracteristicaEscort.delete()

    for caracteristicaIn in caracteristicasIn:
        try:
            caracteristicaEscort=CaracteristicasEscort.objects.get(ce_escort=escort,ce_caracteristica_id=caracteristicaIn)
        except:
            CaracteristicasEscort.objects.create(ce_escort=escort,ce_caracteristica_id=caracteristicaIn)

    servicios=request.GET['servicios']
    serviciosJson = json.loads(servicios)

    ServiciosEscort.objects.filter(se_escort=escort).delete()

    for servicio in serviciosJson:
        if servicio != {}:
            servicioEscort=ServiciosEscort.objects.create(se_escort=escort,se_servicio=Servicios.objects.get(sv_nombre=servicio['nombre']),se_duracion=Duracion.objects.get(du_nombre=servicio['duracion']),se_precio=servicio['precio'])

    escort.es_nombre=nombreIn
    escort.es_apellido=apellidoIn
    escort.es_telefono=telefonoIn
    escort.es_correo=emailIn
    escort.es_descripcion=descripcionIn

    escort.save()

    return JsonResponse({})

def escort_upload_images(request):
    from django.shortcuts import render
    from django.conf import settings
    from django.core.files.storage import FileSystemStorage
    ruta=''
    if request.method == 'POST' and request.POST['escortSeleccionada']:
        escortSeleccionada=Escort.objects.get(es_user__username=request.POST['escortSeleccionada'])
        ruta=escortSeleccionada.full_ruta_upload
        pass

    if request.method == 'POST' and request.FILES['myimage']:
        myimage = request.FILES['myimage']
        fs = FileSystemStorage()
        filename = fs.save(ruta+myimage.name, myimage)
        uploaded_file_url = fs.url(filename)
        return render(request, 'conf-escort.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'conf-escort.html')
