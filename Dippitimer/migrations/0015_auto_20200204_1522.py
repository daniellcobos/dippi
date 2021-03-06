# Generated by Django 2.2.3 on 2020-02-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dippitimer', '0014_auto_20200203_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='precio',
            new_name='precioayer',
        ),
        migrations.RenameField(
            model_name='plato',
            old_name='precioaprox',
            new_name='precioayer',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='preciohoy',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='tasa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plato',
            name='preciohoy',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plato',
            name='tasa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
