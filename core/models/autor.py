from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
