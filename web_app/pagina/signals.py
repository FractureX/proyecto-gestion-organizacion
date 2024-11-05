from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import DocumentoPDF

@receiver(post_migrate)
def populate_initial_data(sender, **kwargs):
    # Verifica si los datos ya existen para evitar duplicados
    if not DocumentoPDF.objects.exists():
        DocumentoPDF.objects.create(field1="value1", field2="value2")
        DocumentoPDF.objects.create(field1="value3", field2="value4")
        print("Datos iniciales insertados correctamente.")