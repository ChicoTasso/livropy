from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Autor


@receiver(post_save, sender=get_user_model)
def criar_autor(sender, instance, created, **kwargs):
    if created:
        autor = Autor.objects.create(instance.get_full_name(), email=instance.email, user=instance)