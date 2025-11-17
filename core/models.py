from django.db import models
from django.contrib.auth.models import User

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    especialidade = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.usuario.username} - {self.especialidade} - {self.data} {self.horario}'
