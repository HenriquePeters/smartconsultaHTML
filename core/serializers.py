from rest_framework import serializers
from .models import Appointment, Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user','crm','specialty']

class AppointmentSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    class Meta:
        model = Appointment
        fields = ['id','patient','doctor','start','end','status','reason','title']

    def get_title(self, obj):
        return f"{obj.patient.get_full_name() or obj.patient.username} — {obj.status}"
