# Generated by Django 2.2.3 on 2020-02-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dippitimer', '0019_auto_20200204_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='tasa',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
        ),
    ]