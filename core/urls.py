from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.home, name='home'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # API
    path('api/appointments/', api_views.AppointmentListCreateView.as_view(), name='api_appointments'),
]
