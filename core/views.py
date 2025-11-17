from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Agendamento

def home(request):
    return render(request, 'home.html')

@login_required
def agendamentos(request):
    if request.method == 'POST':
        Agendamento.objects.create(
            usuario=request.user,
            data=request.POST['data'],
            horario=request.POST['horario'],
            especialidade=request.POST['especialidade'],
            medico=request.POST['medico']
        )
        return redirect('agendamentos')

    agenda = Agendamento.objects.filter(usuario=request.user)

    return render(request, 'agendamentos.html', {'agenda': agenda})
