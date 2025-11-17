from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    crm = models.CharField(max_length=50, blank=True)
    specialty = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} — {self.specialty}"

class ScheduleSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='slots')
    weekday = models.IntegerField(choices=[(i, i) for i in range(0,7)])  # 0=segunda? escolha sua convenção
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor} ({self.weekday}) {self.start_time}-{self.end_time}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('agendado','Agendado'),
        ('confirmado','Confirmado'),
        ('cancelado','Cancelado'),
        ('concluido','Concluído'),
    ]
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendado')
    reason = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} - {self.doctor} - {self.start}"
