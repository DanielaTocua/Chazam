# Generated by Django 4.0.4 on 2022-05-29 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='chaza',
            fields=[
                ('IdChaza', models.AutoField(primary_key=True, serialize=False)),
                ('NombreChaza', models.CharField(max_length=40)),
                ('Puntuacion', models.FloatField()),
                ('Descripcion', models.TextField()),
                ('Ubicacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='comensales',
            fields=[
                ('IdComensal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('NombreUsuario', models.CharField(default='Superusuario', max_length=20, verbose_name='Nombre a Mostrar')),
                ('RegistroFinal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('IdTipoUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('NombreTipoUsuario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DuenoChaza',
            fields=[
                ('IdDuenoChaza', models.AutoField(primary_key=True, serialize=False)),
                ('IdChaza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.chaza')),
                ('IdComensal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.comensales')),
            ],
        ),
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('IdComentario', models.AutoField(primary_key=True, serialize=False)),
                ('DescripcionComentario', models.TextField(max_length=400)),
                ('IdChaza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.chaza')),
                ('IdComensal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.comensales')),
            ],
        ),
        migrations.AddField(
            model_name='comensales',
            name='IdTipoUsuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.tipousuario', verbose_name='Tipo de Usuario'),
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('IdCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('NombreCategoria', models.CharField(max_length=20)),
                ('IdChaza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.chaza')),
            ],
        ),
    ]
