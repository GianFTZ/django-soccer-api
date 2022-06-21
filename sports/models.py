from django.db import models

# Create your models here.
class Local(models.Model):
    nome = models.CharField(max_length=30)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
        