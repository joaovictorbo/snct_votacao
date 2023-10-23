from django.db import models
from django.utils import timezone

class turmas(models.Model):
    imagem = models.ImageField(upload_to='grupimg/%Y/%m/%d')
    data_incricao = models.DateTimeField( default=timezone.now,editable=False)
    titulo = models.CharField(max_length=180)
    descricaoshort = models.TextField()
    descricao = models.TextField()
    escola = models.CharField(max_length=180)
    tutor = models.CharField(max_length=180)
    integrantes =models.TextField()

