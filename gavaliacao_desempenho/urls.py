from django.urls import path
from .views import *

urlpatterns = [
	path('index.html',index,name='dash-avaliacao-desempenho'),
	
	path('anos-ad/index.html',ListaAnoAD,name='ListaAnoAD'),
	path('anos-ad/index.html?register=True',RegistaAnoAD,name='RegistaAnoAD'),
	path('anos-ad/index.html?id_ano=<str:id>update=True',AlteraAnoAD,name='AlteraAnoAD'),

	path('funcionario/lista-desempenho/index.html?idf=<str:id>',DetalhoFuncionarioListaAD,name='DetalhoFuncionarioListaAD'),
	path('funcionario/lista-desempenho/index.html?fid=<str:id>&registar_ad=True',RegistaNovoAD,name='RegistaNovoAD'),
	path('funcionario/lista-desempenho/index.html?fid=<str:id>&alterar_ad=True',AlterarAD,name='AlterarAD'),
	path('funcionario/lista-desempenho/index.html?fid=<str:id>&desabilitar_ad=True',DesabilitarAD,name='DesabilitarAD'),

]