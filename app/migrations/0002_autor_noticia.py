# Generated by Django 4.2.7 on 2023-11-16 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('data_nascimento', models.DateField(default='1980-01-01', verbose_name='Data de Nascimento')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('idade', models.PositiveSmallIntegerField(verbose_name='Idade')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Escritor',
                'verbose_name_plural': 'Escritores',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('data_pub', models.DateField(verbose_name='Data de publicação')),
                ('tags', models.CharField(choices=[('Urgente', 'Urgente'), ('Esportes', 'Esportes'), ('Política', 'Política')], max_length=100, verbose_name='Categoria')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor', verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]