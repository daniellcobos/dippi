# Generated by Django 2.2.3 on 2020-02-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dippitimer', '0010_auto_20200130_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
                ('precio', models.IntegerField()),
                ('unidad', models.CharField(max_length=55)),
            ],
        ),
    ]
