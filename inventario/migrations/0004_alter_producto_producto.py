# Generated by Django 4.2.7 on 2023-11-04 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_producto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='producto',
            field=models.CharField(default='PEPELMA', max_length=100),
        ),
    ]
