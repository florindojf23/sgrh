from django.urls import path
from .views import *
from .colocacao import *

urlpatterns = [
	path('unidade_organica/dashboard/index.html',DashboardEstruturaOrganica,name='DashboardEstruturaOrganica'),
	path('unidade_organica/direcao-gerais-nacionais/index.html',ListaDirecaoGeraisNacionais,name='ListaDirecaoGeraisNacionais'),
	path('unidade_organica/departamentos-seccoes/index.html',ListaDepartamentoSeccoes,name='ListaDepartamentoSeccoes'),
	
	path('unidade_organica/dados-insert-dg/index.html',RegistaNovoDG,name='RegistaNovoFuncionarioDG'),
	path('unidade_organica/dados-update-dg/idDG=<str:id>/index.html',UpdateDirGeral,name='UpdateDirGeral'),

	path('unidade_organica/dados-insert-dn/index.html',RegistaNovoFuncionarioDN,name='RegistaNovoFuncionarioDN'),
	path('unidade_organica/dados-update-dn/id_dir_nac=<str:id>/index.html',UpdateDirNacional,name='UpdateDirNacional'),
	
	path('unidade_organica/dados-insert-departamento/index.html',RegistaNovoDepartamento,name='RegistaNovoDepartamento'),
	path('unidade_organica/dados-update-departamento/iddep=<str:id>/index.html',UpdateDepartamento,name='UpdateDepartamento'),
	
	path('unidade_organica/dados-insert-seccao/index.html',RegistaNovoSeccao,name='RegistaNovoSeccao'),
	path('unidade_organica/dados-update-seccao/id_sec=<str:id>/index.html',UpdateSeccao,name='UpdateSeccao'),
	
	path('get_data/', get_data, name='get_data'),
	path('ajax_load_lista_funcionario_dashboard_organica/', load_lista_funcionario_dashboard_organica, name='ajax_load_lista_funcionario_dashboard_organica'),

	# colocacao
	path('colocacao/dashboard/index.html',DashboardColocacao,name='DashboardColocacao'),


]