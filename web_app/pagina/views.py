import os
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import DocumentoPDFForm
from .utils import (
  extraer_texto_pdf
)
from .models import DocumentoPDF

# Create your views here.
def index(request):
  return render(request, 'pagina/index.html')

# Carga de Documentos (PDFs)
def cargar_pdf(request):
  if request.method == 'POST':
    form = DocumentoPDFForm(request.POST, request.FILES)
    if form.is_valid():
      documento = form.save()  # Crear el objeto pero no guardarlo aún en la base de datos
      archivo_path = os.path.join(settings.MEDIA_ROOT, documento.archivo.name)
      
      # Guardar el texto extraído en el campo 'texto' del documento
      documento.texto = extraer_texto_pdf(archivo_path)
      documento.save()  # Guardar el documento con el texto extraído
      
      return redirect('lista_documentos')
  else:
        form = DocumentoPDFForm()
    
  return render(request, 'pagina/cargar_pdf.html', {'form': form})

def lista_documentos(request):
  documentos = DocumentoPDF.objects.all()
  return render(request, 'pagina/lista_documentos.html', {'documentos': documentos})