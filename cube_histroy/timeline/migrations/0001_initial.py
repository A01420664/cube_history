# Generated by Django 2.0.1 on 2018-03-09 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('idEvento', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=5000)),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('continente', models.IntegerField(choices=[(1, 'America'), (2, 'Africa'), (3, 'Asia'), (4, 'Europa'), (5, 'Oceania')])),
            ],
        ),
        migrations.CreateModel(
            name='Fuente',
            fields=[
                ('idFuente', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=5000)),
                ('link', models.CharField(max_length=5000)),
                ('año', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('fkEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('idImagen', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=5000)),
                ('fkEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Evento')),
            ],
        ),
    ]
