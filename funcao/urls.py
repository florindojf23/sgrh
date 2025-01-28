from django.urls import path
from .views import *

urlpatterns = [
	path('funcionario/lista-funcao/index.html?idf=<str:id>',DetalhoFuncionarioListaFuncao,name='DetalhoFuncionarioListaFuncao'),
	path('funcionario/lista-funcao/index.html?fid=<str:id>&registar_contratacao=True',RegistaNovoContratacao,name='RegistaNovoContratacao'),
	path('funcionario/lista-funcao/index.html?fid=<str:id>&ffid=<str:ffid>&update_contratacao=True',UpdateContratacao,name='UpdateContratacao'),
	path('funcionario/lista-funcao/index.html?fid=<str:id>&ffid=<str:ffid>&desabilitar_contratacao=True',DesabilitarContratacao,name='DesabilitarContratacao'),

	path('funcionario/lista-funcao/index.html?fid=<str:id>&registar_permanente=True',RegistaNovoPermanente,name='RegistaNovoPermanente'),
	path('funcionario/lista-funcao/index.html?fid=<str:id>&ffid=<str:ffid>&update_permanente=True',UpdatePermanente,name='UpdatePermanente'),
	path('funcionario/lista-funcao/index.html?fid=<str:id>&ffid=<str:ffid>&desabilitar_permanente=True',DesabilitarPermanente,name='DesabilitarPermanente'),
	
	path('funcionario/lista-funcao/index.html?fid=<str:id>&registar_comissao_servico=True',RegistaComissao_servico,name='RegistaComissao_servico'),
	path('funcionario/lista-funcao/index.html?fid=<str:id>&idfcs=<str:idfcs>&alterar_comissao_servico=True',UpdateComissao_servico,name='UpdateComissao_servico'),
	path('funcionario/lista-funcao/index.html?fid=<str:id>&idfcs=<str:idfcs>&desabilitar_comissao_servico=True',DesabilitarComissao_servico,name='DesabilitarComissao_servico'),
	

	path('funcionario/lista-funcao/index.html?fid=<str:id>&registar_casual=True',RegistaNovoFichaCasual,name='RegistaNovoFichaCasual'),

	path('ajax/load-categorias/', load_categorias, name='ajax_load_categorias'),
    path('ajax/load-escalaos/', load_escalaos, name='ajax_load_escalaos'),
    path('ajax/load-indices/', load_indices, name='ajax_load_indices'),
	
	path('funcao/dashboard/index.html',DashboardFuncao,name='DashboardFuncao'),

	path('ajax/load-form-progrssao/', load_form_progressao, name='ajax_load_form_progressao'),

]