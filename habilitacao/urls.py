from django.urls import path
from .views import *

urlpatterns = [
	path('dashboard/index.html',index,name='dashboard-habilitacao'),
	path('dashboard/registar/habilitacao/index.html',RegistaNovoHabFuncionario,name='RegistaNovoHabFuncionario'),
	
	path('nivel-habilitacao/index.html',nivelHabilitacao,name='nivelHabilitacao'),
	path('nivel-habilitacao/register/index.html',nivelHabilitacaoAdd,name='nivelHabilitacaoAdd'),
	path('nivel-habilitacao/altera/index.html?id=<str:id>',nivelHabilitacaoAltera,name='nivelHabilitacaoAltera'),

	path('entidade/index.html',EntidadeHabilitacao,name='EntidadeHabilitacao'),
	path('entidade/register/index.html',EntidadeHabilitacaoAdd,name='EntidadeHabilitacaoAdd'),
	path('entidade/altera/index.html?id=<str:id>',EntidadeHabilitacaoAltera,name='EntidadeHabilitacaoAltera'),

	path('curso/index.html',CursoHabilitacao,name='CursoHabilitacao'),
	path('curso/register/index.html',CursoHabilitacaoAdd,name='CursoHabilitacaoAdd'),
	path('curso/altera/index.html?id=<str:id>',CursoHabilitacaoAltera,name='CursoHabilitacaoAltera'),

	path('funcionario/lista-habilitacao/index.html?idf=<str:id>',DetalhoFuncionarioListaHab,name='DetalhoFuncionarioListaHab'),
	path('funcionario/regista-habilitacao/index.html?idf=<str:id>',DetalhoFuncionarioRegistaHab,name='DetalhoFuncionarioRegistaHab'),
	path('funcionario/altera-habilitacao/index.html?idf=<str:id>',DetalhoFuncionarioAlteraHab,name='DetalhoFuncionarioAlteraHab'),
	path('funcionario/desabilitar-habilitacao/index.html?idf=<str:id>',DetalhoFuncionarioDesabilitarHab,name='DetalhoFuncionarioDesabilitarHab'),
	
	path('dashboard/monitor-habilitacao-data/habilitacao/index.html',monitor_habilitacao_data,name='monitor_habilitacao_data'),
	path('export-monitor-habilitacao/', export_monitor_habilitacao_to_excel, name='export_monitor_habilitacao_to_excel'),
	
]