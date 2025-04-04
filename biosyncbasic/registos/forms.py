from django import forms
from .models import Registo, Atendimento

class RegistoForm(forms.ModelForm):
    """Formulário para criar/editar um registo."""
    class Meta:
        model = Registo
        fields = ['pressao_sistolica', 'pressao_diastolica', 'frequencia_cardiaca', 'observacoes', 'localizacao']



class AtendimentoForm(forms.ModelForm):
    """Formulário para criar/editar um atendimento."""
    class Meta:
        model = Atendimento
        fields = ['notas']



class UtenteLoginForm(forms.Form):
    """Formulário de login para utentes."""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class MedicoLoginForm(forms.Form):
    """Formulário de login para médicos."""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)