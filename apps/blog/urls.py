from django.urls import path
from .views import home, detallePost, generales, programacion, videojuegos, tecnologia, tutoriales

urlpatterns = [
    path('', home, name = 'index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('vedeosjuegos/', videojuegos, name='videojuegos'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    path('<slug>/',detallePost, name = 'detalle_post'),
]