from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def detallePost(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html',{'detalle_post':post})


def home(request):
    posts = Post.objects.filter(estado = True)
    qryset = request.GET.get('buscar') #obteniendo lo ingresado en buscar
    if qryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = qryset) | Q(descripcion__icontains = qryset)
        ).distinct()
    #paginacion
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts':posts})


def generales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='General')
    )
    qryset = request.GET.get('buscar')
    if qryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = qryset) | Q(descripcion__icontains = qryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='General'),
        ).distinct()
    #paginacion
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generales.html',{'posts':posts})


def programacion(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Programacion')
    )
    qryset = request.GET.get('buscar')
    if qryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = qryset) | Q(descripcion__icontains = qryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='Programacion'),
        ).distinct()
    #paginacion
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'programacion.html',{'posts':posts})


def videojuegos(request):
    posts = Post.objects.filter(
        estado =True,
        categoria = Categoria.objects.get(nombre__iexact='Videojuegos') #__iexact no distingue mayusculas con minusclas
    )
    qryset = request.GET.get('buscar')
    if qryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = qryset) | Q(descripcion__icontains = qryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='Videojuegos'),
        ).distinct()
    #paginacion
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'videojuegos.html',{'posts':posts})


def tecnologia(request):
    posts = Post.objects.filter(
        estado =True,
        categoria = Categoria.objects.get(nombre__iexact='Tecnologia')
    )
    qryset = request.GET.get('buscar')
    if qryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = qryset) | Q(descripcion__icontains = qryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='Tecnologia'),
        ).distinct()
    #paginacion
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnologia.html',{'posts':posts})


def tutoriales(request):
    posts = Post.objects.filter(
        estado =True,
        categoria = Categoria.objects.get(nombre__iexact='Tutoriales')
    )
    qryset = request.GET.get('buscar')
    if qryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = qryset) | Q(descripcion__icontains = qryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='Tutoriales'),
        ).distinct()
    #paginacion
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tutoriales.html',{'posts':posts})
