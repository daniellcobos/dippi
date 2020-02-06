# Generated by Django 2.2.3 on 2020-02-03 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dippitimer', '0011_ingrediente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
                ('precioaprox', models.DecimalField(decimal_places=6, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ListaIngredientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=3, max_digits=3)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platos', to='Dippitimer.Ingrediente')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listaing', to='Dippitimer.Plato')),
            ],
        ),
    ]
