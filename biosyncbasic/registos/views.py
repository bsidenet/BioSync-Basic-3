from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Registo, Atendimento, Utente
from .forms import RegistoForm, AtendimentoForm, UtenteLoginForm, MedicoLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    """View para a página inicial."""
    return render(request, 'index.html')

# Views de Autenticação
def utente_login(request):
    """View para o login de utentes."""
    if request.method == 'POST':
        form = UtenteLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login efetuado com sucesso.")
                return redirect('utente_registos', utente_id=user.utente.id) # Redireciona para a página inicial do utente
            else:
                form.add_error(None, "Nome de utilizador ou palavra-passe inválidos.")
    else:
        form = UtenteLoginForm()
    return render(request, 'registos/utente_login.html', {'form': form})

def medico_login(request):
    """View para o login de médicos."""
    if request.method == 'POST':
        form = MedicoLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login efetuado com sucesso.")
                return redirect('medico_list') # Redireciona para a página inicial do médico
            else:
                form.add_error(None, "Nome de utilizador ou palavra-passe inválidos.")
    else:
        form = MedicoLoginForm()
    return render(request, 'registos/medico_login.html', {'form': form})

def utente_logout(request):
    """View para o logout de utentes."""
    logout(request)
    messages.success(request, "Logout efetuado com sucesso.")
    return redirect('index')

def medico_logout(request):
    """View para o logout de médicos."""
    logout(request)
    messages.success(request, "Logout efetuado com sucesso.")
    return redirect('index')

# Views de Registo
@login_required
def registo_create(request):
    """View para criar um novo registo."""
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            registo = form.save(commit=False)
            registo.utente_id = request.user.utente
            registo.save()
            messages.success(request, "Registo criado com sucesso.")
            return redirect('registo_list')
    else:
        form = RegistoForm()
    return render(request, 'registos/registo_form.html', {'form': form})

@login_required
def registo_list(request):
    """View para listar os registos de um utente."""
    utente = get_object_or_404(Utente, user=request.user)
    registos = Registo.objects.filter(utente_id=utente)
    return render(request, 'registos/registo_list.html', {'registos': registos})

# Views de Atendimento
@login_required
def atendimento_create(request, utente_id):
    """View para criar um novo atendimento."""
    utente = get_object_or_404(Utente, pk=utente_id)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.medico = request.user.medico
            atendimento.utente = utente
            atendimento.save()
            messages.success(request, "Atendimento criado com sucesso.")
            return redirect('atendimento_list', utente_id=utente_id)
    else:
        form = AtendimentoForm()
    return render(request, 'registos/atendimento_form.html', {'form': form, 'utente': utente})

@login_required
def atendimento_list(request, utente_id):
    """View para listar os atendimentos de um utente."""
    utente = get_object_or_404(Utente, pk=utente_id)
    atendimentos = Atendimento.objects.filter(utente=utente)
    return render(request, 'registos/atendimento_list.html', {'atendimentos': atendimentos, 'utente': utente})

# Views de Visualização de Dados
@login_required
def utente_registos(request, utente_id):
    """View para visualizar os registos de um utente."""
    utente = get_object_or_404(Utente, pk=utente_id)
    registos = Registo.objects.filter(utente=utente)
    return render(request, 'registos/utente_registos.html', {'registos': registos, 'utente': utente})

# Views de Gráficos e Relatórios
@login_required
def registos_grafico(request, utente_id):
    """View para gerar um gráfico dos registos de um utente."""
    utente = get_object_or_404(Utente, pk=utente_id)
    registos = Registo.objects.filter(utente=utente)
    # Implemente a lógica para gerar o gráfico
    return render(request, 'registos/registos_grafico.html', {'registos': registos, 'utente': utente})

@login_required
def registos_relatorio(request, utente_id):
    """View para gerar um relatório dos registos de um utente."""
    utente = get_object_or_404(Utente, pk=utente_id)
    registos = Registo.objects.filter(utente=utente)
    # Implemente a lógica para gerar o relatório
    return render(request, 'registos/registos_relatorio.html', {'registos': registos, 'utente': utente})