from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField

# Create your models here.
class Diario (models.Model):
    conteudo=TextField(max_length=500)
    criado=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.conteudo