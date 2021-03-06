# Generated by Django 2.1.1 on 2018-11-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0006_auto_20181111_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costo',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
