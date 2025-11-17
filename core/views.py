from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, Doctor, ScheduleSlot
from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from .serializers import AppointmentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import dateutil.parser as dp

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    if hasattr(request.user, 'doctor_profile'):
        doctor = request.user.doctor_profile
        upcoming = Appointment.objects.filter(doctor=doctor, start__gte=timezone.now()).order_by('start')[:20]
        return render(request,'dashboard_doctor.html', {'doctor':doctor, 'upcoming': upcoming})
    else:
        appts = Appointment.objects.filter(patient=request.user).order_by('start')[:20]
        return render(request,'dashboard_patient.html', {'appts': appts})

@login_required
def agendamentos(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        if not doctor_id:
            return HttpResponseBadRequest('Médico não informado')
        doctor = get_object_or_404(Doctor, id=doctor_id)
        start = request.POST.get('start')
        end = request.POST.get('end')
        start_dt = dp.parse(start)
        end_dt = dp.parse(end) if end else (start_dt + timezone.timedelta(minutes=30))
        Appointment.objects.create(patient=request.user, doctor=doctor, start=start_dt, end=end_dt)
        return redirect('agendamentos')
    doctors = Doctor.objects.all()
    return render(request,'agendamentos.html', {'doctors':doctors})

# API views
from rest_framework import generics, permissions
from .serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'doctor_profile'):
            return Appointment.objects.filter(doctor__user=user).order_by('start')
        return Appointment.objects.filter(patient=user).order_by('start')

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)
