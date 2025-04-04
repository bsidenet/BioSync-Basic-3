from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.db import models

class Utente(models.Model):
    """Modelo para representar um utente."""
    id = models.AutoField(primary_key=True)
    num_utente_saude = models.CharField(max_length=20, unique=True)  # Número de utente de saúde
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    email = models.EmailField(unique=True)
    contacto = models.CharField(max_length=15, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    # Adicione outros campos relevantes para o utente, se necessário

    def __str__(self):
        return self.user.username

class Medico(models.Model):
    """Modelo para representar um médico."""
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True, null=True)
    # Adicione outros campos relevantes para o médico, se necessário

    def __str__(self):
        return self.user.username

class Registo(models.Model):
    """Modelo para representar um registo de pressão arterial e frequência cardíaca."""
    id = models.AutoField(primary_key=True) # ID do registo
    utente_id = models.ForeignKey(Utente, on_delete=models.CASCADE) # ID do utente
    data_hora = models.DateTimeField(auto_now_add=True)
    pressao_sistolica = models.IntegerField(validators=[MinValueValidator(60), MaxValueValidator(200)])
    pressao_diastolica = models.IntegerField(validators=[MinValueValidator(40), MaxValueValidator(140)])
    frequencia_cardiaca = models.IntegerField(validators=[MinValueValidator(40), MaxValueValidator(200)])
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Registo de {self.utente_id.user.username} em {self.data_hora}"

'''

class Atendimento(models.Model):
    """Modelo para representar um atendimento médico a um utente."""
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    notas = models.TextField()

    def __str__(self):
        return f"Atendimento de {self.utente.user.username} por {self.medico.user.username} em {self.data_hora}"

'''