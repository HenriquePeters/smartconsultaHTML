from django.shortcuts import render, redirect
from .models import Agendamento

def home(request):
    return render(request, 'home.html')

def agendar(request):
    if request.method == "POST":
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        especialidade = request.POST['especialidade']
        data = request.POST['data']

        Agendamento.objects.create(
            nome=nome,
            telefone=telefone,
            especialidade=especialidade,
            data=data
        )
        return redirect('/')
    
    return render(request, 'agendar.html')

def admin_agendamentos(request):
    lista = Agendamento.objects.all().order_by('-criado_em')
    return render(request, 'admin_agendamentos.html', {'lista': lista})
