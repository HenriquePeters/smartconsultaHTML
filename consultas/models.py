from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=120)
    data = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"
