# Generated by Django 4.2.7 on 2023-11-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_livro_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(default='Sinopse do Livro', max_length=255),
        ),
    ]