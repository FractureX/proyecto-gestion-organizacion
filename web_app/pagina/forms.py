from django import forms
from .models import DocumentoPDF
from django.core.exceptions import ValidationError

# Carga de Documentos (PDFs)
class DocumentoPDFForm(forms.ModelForm):
  class Meta:
    model = DocumentoPDF
    fields = ['titulo', 'archivo']

  def clean_archivo(self):
    archivo = self.cleaned_data.get('archivo')
    if archivo:
      if not archivo.name.endswith('.pdf'):
        raise ValidationError("Solo se permiten archivos PDF.")
      if archivo.size > 5 * 1024 * 1024:  # Limite de 5MB
        raise ValidationError("El archivo no debe superar los 5 MB.")
    return archivo