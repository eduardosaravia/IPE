# Generated by Django 4.2.7 on 2023-11-04 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_producto_imagen_instalada_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='unidad',
            field=models.CharField(default='M2', max_length=10),
        ),
    ]