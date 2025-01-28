from django.urls import path
from .views import *
from .charts import *

urlpatterns = [
	path('estatistica/dashboard/index.html',DashboardEstatistica,name='DashboardEstatistica'),
	
	path('estatistica/dashboard/lista-relatorio/<str:assunto>/<str:id>/<str:genero>index.html',ListaRelatorio1,name='ListaRelatorio1'),
	
	# charts
	path('grafiku/ChartFuncionarioPivotCASEXO/',ChartFuncionarioPivotCASEXO,name='ChartFuncionarioPivotCASEXO'),
	path('grafiku/ChartFuncionarioPivotTFSEXO/',ChartFuncionarioPivotTFSEXO,name='ChartFuncionarioPivotTFSEXO'),
	path('grafiku/ChartFuncionarioPivotGISEXO/',ChartFuncionarioPivotGISEXO,name='ChartFuncionarioPivotGISEXO'),
	path('grafiku/ChartFuncionarioPivotLTSEXO/',ChartFuncionarioPivotLTSEXO,name='ChartFuncionarioPivotLTSEXO'),
]