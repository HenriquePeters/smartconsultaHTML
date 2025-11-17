from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test

@login_required
def change_status(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appt.status = request.POST['status']
        appt.save()
    return redirect('dashboard')

@login_required
def manage_slots(request):
    doctor = request.user.doctor_profile
    slots = doctor.slots.all()
    if request.method == 'POST':
        # criar slot rápido
        weekday = int(request.POST['weekday'])
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        duration = int(request.POST.get('duration_minutes',30))
        ScheduleSlot.objects.create(doctor=doctor, weekday=weekday,
            start_time=start_time, end_time=end_time, duration_minutes=duration)
        return redirect('manage_slots')
    return render(request,'manage_slots.html', {'slots':slots})
