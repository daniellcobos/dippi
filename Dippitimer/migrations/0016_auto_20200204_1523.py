# Generated by Django 2.2.3 on 2020-02-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dippitimer', '0015_auto_20200204_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='precioayer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='preciohoy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='tasa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='plato',
            name='precioayer',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=13),
        ),
        migrations.AlterField(
            model_name='plato',
            name='preciohoy',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=13),
        ),
        migrations.AlterField(
            model_name='plato',
            name='tasa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
