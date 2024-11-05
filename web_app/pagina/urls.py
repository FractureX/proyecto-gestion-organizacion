from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('cargar_pdf', views.cargar_pdf, name='cargar_pdf'),
  path('lista_documentos', views.lista_documentos, name='lista_documentos'),
]