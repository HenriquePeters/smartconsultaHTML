from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.utils.dateparse import parse_datetime

class AppointmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        # se for médico, ver somente consultas do médico; se paciente, só as suas
        if hasattr(user, 'doctor_profile'):
            return Appointment.objects.filter(doctor__user=user).order_by('start')
        return Appointment.objects.filter(patient=user).order_by('start')

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)
