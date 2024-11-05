# Generated by Django 5.1.2 on 2024-10-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('archivo', models.FileField(upload_to='pdfs/')),
                ('fecha_carga', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
