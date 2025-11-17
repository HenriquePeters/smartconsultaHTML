from django.urls import path
from . import views
from .views_registration import register

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('api/appointments/', views.AppointmentListCreateView.as_view(), name='api_appointments'),
    path('accounts/register/', register, name='register'),
]
