# Generated by Django 2.2.3 on 2020-02-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dippitimer', '0023_auto_20200204_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plato',
            name='descuento',
        ),
        migrations.AddField(
            model_name='plato',
            name='tasa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
