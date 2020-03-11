# Generated by Django 3.0.3 on 2020-02-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-Created'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
        migrations.AlterField(
            model_name='service',
            name='Content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='Updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizacion'),
        ),
    ]