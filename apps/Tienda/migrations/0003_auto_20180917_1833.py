# Generated by Django 2.1.1 on 2018-09-17 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_categoria_fechacracion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='fechaCracion',
            new_name='fechaCreacion',
        ),
    ]
