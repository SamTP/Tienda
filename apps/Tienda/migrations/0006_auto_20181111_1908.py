# Generated by Django 2.1.1 on 2018-11-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0005_ventas_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='producto',
            field=models.CharField(default=' ', max_length=75),
        ),
    ]