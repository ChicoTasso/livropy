# Generated by Django 4.2.7 on 2023-11-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=150, verbose_name='Nome')),
                ('anoPublicacao', models.SmallIntegerField(default=2000, verbose_name='Ano de Publicação')),
                ('ilustrador', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=50)),
            ],
        ),
    ]
