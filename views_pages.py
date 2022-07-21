from django.shortcuts import render
from .models import About, Noticia, Servicio, Proyecto, Tramite
#from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.


def index(request):
    queryset = request.GET.get("buscar")
    news = Noticia.objects.filter(estado = True)
    dnews = Noticia.objects.filter(
        estado = True,
        destacada = True
    )
    servs = Servicio.objects.filter(estado = True)
    trams = Tramite.objects.filter(estado= True)
    projs = Proyecto.objects.filter(estado= True)
    if queryset:
        news = Noticia.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains= queryset)
        ).distinct()
    return render(request, 'index.html', {'news': news, 'dnews': dnews, 'servs': servs, 'trams': trams, 'projs': projs})



def about(request):
    epts = About.objects.filter(estado = True)
    return render(request, 'about.html', {'epts': epts})



def contact(request):
    queryset = request.GET.get("buscar")
    news = Noticia.objects.filter(estado=True)
    dnews = Noticia.objects.filter(
        estado=True,
        destacada=True
    )
    servs = Servicio.objects.filter(estado=True)
    trams = Tramite.objects.filter(estado=True)
    projs = Proyecto.objects.filter(estado=True)

    return render(request, 'contact.html', {'news': news, 'dnews': dnews, 'servs': servs, 'trams': trams, 'projs': projs})




def noticias(request):
    queryset = request.GET.get("buscar")
    news = Noticia.objects.filter(estado = True)
    dnews = Noticia.objects.filter(
        estado= True,
        destacada = True
    )
    if queryset:
        news = Noticia.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains= queryset)
        ).distinct()
    return render(request, 'noticias.html', {'news': news, 'dnews': dnews})




def detalleNew(resquest, slug_new):
    #news = get_object.or_404(Noticia, slug = slug)
    news = Noticia.objects.get(
        slug_new = slug_new
    )
    return render(resquest, 'detail_new.html', {'detalle_new': news})



def detalleDNew(resquest, slug_new):
    #news = get_object.or_404(Noticia, slug = slug)
    dnews = Noticia.objects.get(
        slug_new = slug_new
    )
    return render(resquest, 'detail_dnew.html', {'detalle_new': dnews})


def proyectos(request):
    queryset = request.GET.get("buscar")
    projs = Proyecto.objects.filter(estado=True)
    if queryset:
        projs = Proyecto.objects.filter(
            Q(proyecto__icontains= queryset) |
            Q(descripcion__icontains= queryset)
        ).distinct()
    return render(request, 'proyectos.html', {'projs': projs})



def detalleProject(resquest, slug_proj):
    #projs = get_object.or_404(Proyecto, slug = slug)
    projs = Proyecto.objects.get(
        slug_proj = slug_proj
    )
    return render(resquest, 'detail_project.html', {'detalle_proj': projs})




def servicios(request):
    queryset = request.GET.get("buscar")
    servs = Servicio.objects.filter(estado=True)
    if queryset:
        servs = Servicio.objects.filter(
            Q(servicio__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()
    return render(request, 'servicios.html', {'servs': servs})





def detalleServ(resquest, slug_serv):
    #servs = get_object.or_404(Servicio, slug = slug)
    servs = Servicio.objects.get(
        slug_serv = slug_serv
    )
    return render(resquest, 'detail_serv.html', {'detalle_serv': servs})



def tramites(request):
    queryset = request.GET.get("buscar")
    trams = Tramite.objects.filter(estado = True)
    if queryset:
        trams = Tramite.objects.filter(
            Q(tramite__icontains= queryset) |
            Q(descripcion__icontains= queryset)
        ).distinct()
    return render(request, 'tramites.html', {'trams': trams})




def detalleTramit(resquest, slug_tram):
    #trams = get_object.or_404(Tramite, slug = slug)
    trams = Tramite.objects.get(
        slug_tram = slug_tram
    )
    return render(resquest, 'detail_tram.html', {'detalle_tram': trams})













