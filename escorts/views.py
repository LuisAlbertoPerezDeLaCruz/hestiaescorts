# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


provincias = Provincia.objects.all().order_by('pr_nombre')

def index(request):
    return render(request, "index.html", {'provincias':provincias})

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

def conf_escort(request):
    return render(request, "conf-escort.html", {'provincias':provincias})

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

def portfolio_3_col(request,pk):
    provinciaSeleccionada=Provincia.objects.get(pk=pk)

    escorts_list=Escort.objects.filter(es_pais=provinciaSeleccionada.pr_pais,es_provincia=provinciaSeleccionada.pr_slug)

    page = request.GET.get('page', 1)

    paginator = Paginator(escorts_list, 2)

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
    })

def portfolio_escort(request,pk):
    escortSeleccionada=Escort.objects.get(es_slug=pk)
    provinciaSeleccionada=Provincia.objects.get(pk=escortSeleccionada.es_provincia.pk)
    return render(request, "portfolio-escort.html", {
        'provincias': provincias,
        'provinciaSeleccionada': provinciaSeleccionada,
        'escortSeleccionada':escortSeleccionada,
    })

