# Generated by Django 4.2.7 on 2023-11-21 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_anopublicacao_livro_ano_remove_livro_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.TextField(default='Título do Livro', max_length=90),
        ),
    ]
