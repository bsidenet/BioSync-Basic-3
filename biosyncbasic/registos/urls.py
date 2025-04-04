from django.urls import path
from . import views

urlpatterns = [

    # URLs de Listagem
    path('', views.index, name='index'), # Certifique-se de que a raiz da aplicação aponta para views.index
    path('utente/list/', views.utente_list, name='utente_list'),  # Listagem de utentes
    path('medico/list/', views.medico_list, name='medico_list'),  # Listagem de médicos
    path('registo/list/', views.registo_list, name='registo_list'),  # Listagem de registos
    path('atendimento/list/', views.atendimento_list, name='atendimento_list'),  # Listagem de atendimentos

    # URLs de Autenticação
    path('utente/login/', views.utente_login, name='utente_login'),
    path('medico/login/', views.medico_login, name='medico_login'),
    path('utente/logout/', views.utente_logout, name='utente_logout'),
    path('medico/logout/', views.medico_logout, name='medico_logout'),

    # URLs de Registo
    path('registo/create/', views.registo_create, name='registo_create'),
    # path('registo/list/', views.registo_list, name='registo_list'),

    # URLs de Atendimento
    path('atendimento/create/<int:utente_id>/', views.atendimento_create, name='atendimento_create'),
    path('atendimento/list/<int:utente_id>/', views.atendimento_list, name='atendimento_list'),

    # URLs de Visualização de Dados
    path('utente/<int:utente_id>/registos/', views.utente_registos, name='utente_registos'),

    # URLs de Gráficos e Relatórios
    path('utente/<int:utente_id>/registos/grafico/', views.registos_grafico, name='registos_grafico'),
    path('utente/<int:utente_id>/registos/relatorio/', views.registos_relatorio, name='registos_relatorio'),
]