from django.contrib import admin
from .models import Utente, Medico, Registo, Atendimento

admin.site.register(Utente)
admin.site.register(Medico)
admin.site.register(Registo)
admin.site.register(Atendimento)