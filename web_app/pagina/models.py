from django.db import models

class Rol(models.Model):
  nombre = models.CharField(max_length=50)
  def __str__(self):
    return self.nombre

class Usuario(models.Model):
  id_rol = models.CharField(max_length=50)
  def __str__(self):
    return self.nombre

# Carga de Documentos (PDFs)
class DocumentoPDF(models.Model):
  titulo = models.CharField(max_length=100)
  texto = models.TextField(default="")
  archivo = models.FileField(upload_to='pdfs/')
  fecha_carga = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo
