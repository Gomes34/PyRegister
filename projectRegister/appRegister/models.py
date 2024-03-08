from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.TextField(max_length=255)
    email_usuario = models.TextField(max_length=255)
