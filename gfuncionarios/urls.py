from django.urls import path
from .views import *

urlpatterns = [
	path('lista/funcionario/index.html',index,name='lista-funcionarios'),

	path('funcionarios-data/', funcionarios_data, name='funcionarios_data'),  # New data URL

	path('registar/funcionario/index.html?register=True',RegistaNovoFuncionario,name='RegistaNovoFuncionario'),
	path('detalho/funcionario/index.html?fid=<str:idf>',DetailFuncionario,name='DetailFuncionario'),
	path('alterar/funcionario/index.html?fid=<str:id>&atualizar=True',AtualizarFuncionario,name='AtualizarFuncionario'),
	path('desabilitar/funcionario/index.html?fid=<str:id>&desabilitar=True',DesabilitarFuncionario,name='DesabilitarFuncionario'),
	

	path('lista/colocacao/funcionario/index.html?fid=<str:id>&lista=True',DetalhoFuncionarioListaColocacao,name='DetalhoFuncionarioListaColocacao'),
	path('registar/colocacao/funcionario/index.html?fid=<str:id>&register=True',DetalhoFuncionarioRegistarColocacao,name='DetalhoFuncionarioRegistarColocacao'),
	path('alterar/colocacao/funcionario/index.html?fid=<str:id>&idfc=<str:idfc>&alterar=True',UpdateColocacao,name='UpdateColocacao'),
	path('desabilitar/colocacao/funcionario/index.html?fid=<str:id>&idfc=<str:idfc>&desabilitar=True',DesabilitarColocacao,name='DesabilitarColocacao'),
	
	path('lista/nao-exercicio/funcionario/index.html?fid=<str:id>&lista=True',DetalhoFuncionarioListaNaoExercicio,name='DetalhoFuncionarioListaNaoExercicio'),
	path('registar/nao-exercicio/funcionario/index.html?fid=<str:id>&registar=True',DetalhoFuncionarioRegistarFNExercicio,name='DetalhoFuncionarioRegistarFNExercicio'),
	path('registar/nao-exercicio/funcionario/index.html?fid=<str:id>&idfne=<str:idfne>&alterar=True',UpdateFNExercicio,name='UpdateFNExercicio'),
	path('desabilitar/nao-exercicio/funcionario/index.html?fid=<str:id>&idfne=<str:idfne>&desabilitar=True',DesabilitarFNExercicio,name='DesabilitarFNExercicio'),
	
	path('lista/saida/funcionario/index.html?fid=<str:id>&lista=True',DetalhoFuncionarioListaSaida,name='DetalhoFuncionarioListaSaida'),
	path('registar/saida/funcionario/index.html?fid=<str:id>&registar=True',DetalhoFuncionarioRegistarFSaida,name='DetalhoFuncionarioRegistarFSaida'),
	path('alterar/saida/funcionario/index.html?fid=<str:id>&idfsd=<str:idfsd>&alterar=True',DetalhoFuncionarioAlterarFSaida,name='DetalhoFuncionarioAlterarFSaida'),
	path('desabilitar/saida/funcionario/index.html?fid=<str:id>&idfsd=<str:idfsd>&desabilitar=True',DesabilitarFSaida,name='DesabilitarFSaida'),
	

	path('busca-funcionario/', BuscaFuncionario, name='BuscaFuncionario'),

	# path('imajen/upload/funcionario/index.html?fid=<str:fid>&upload-image=True',updatedImageFun,name='updatedImageFun'),
	path('imajen/upload/funcionario/index.html/fid=<str:fid>',updatedImageFun1,name='updatedImageFun1'),
]