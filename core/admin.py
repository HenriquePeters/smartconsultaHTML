from django.contrib import admin
from .models import Doctor, ScheduleSlot, Appointment
from django.utils.html import format_html

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('__str__','specialty','crm','appointments_count')
    search_fields = ('user__username','user__first_name','user__last_name','specialty','crm')
    list_filter = ('specialty',)

    def appointments_count(self, obj):
        return obj.appointments.count()
    appointments_count.short_description = 'Agendamentos'

@admin.register(ScheduleSlot)
class ScheduleSlotAdmin(admin.ModelAdmin):
    list_display = ('doctor','weekday','start_time','end_time','duration_minutes','active')
    list_filter = ('doctor','weekday','active')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient','doctor','start','end','status','created_at')
    list_filter = ('status','doctor')
    search_fields = ('patient__username','doctor__user__first_name','doctor__user__last_name')
    actions = ['mark_confirmed','mark_cancelled']

    def mark_confirmed(self, request, queryset):
        queryset.update(status='confirmado')
    mark_confirmed.short_description = 'Marcar como confirmado'

    def mark_cancelled(self, request, queryset):
        queryset.update(status='cancelado')
    mark_cancelled.short_description = 'Marcar como cancelado'
