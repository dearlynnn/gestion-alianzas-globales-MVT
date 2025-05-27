from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    correo_verificado = models.BooleanField(default=False)

class CorreoAutorizado(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email