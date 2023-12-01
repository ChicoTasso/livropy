from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Autor(models.Model):
    
    nome = models.CharField("Nome", max_length=200)
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
    email = models.EmailField("Email")
    idade = models.PositiveSmallIntegerField("Idade", null=True, blank=True)
    avatar = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)
    user = models.OneToOneField(get_user_model(), verbose_name='Usuário', on_delete=models.CASCADE, null=True, blank=True, related_name='livros')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Escritor"
        verbose_name_plural = "Escritores"
        permissions = [
            ('pode_publicar', 'Pode publicar um Livro'),
        ]


class Livro(models.Model):
    
    EDITORA = (
        ('Ática', 'Ática'),
        ('Objetiva', 'Objetiva'),
        ('Atlas', 'Atlas'),
        ('FTD', 'FTD'),

    )
    
    titulo = models.TextField(max_length=90)
    sinopse = models.TextField(max_length=255)
    ilustrador =  models.CharField('Ilustrador', max_length=70)
    ano = models.SmallIntegerField('Ano de Publicação', default=2000)
    escritor = models.ForeignKey(Autor,verbose_name='Autor', on_delete=models.CASCADE)
    editora = models.CharField(
        max_length=20,
        choices=EDITORA,
    )

    def __str__(self):
        return self.titulo 