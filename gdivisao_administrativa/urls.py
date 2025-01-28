from django.urls import path
from .views import *

urlpatterns = [
	path('index.html',index,name='lista-divisao-administrativa'),
	
	path('ajax/dash/index.html',monitor_divisao_administrativa_data,name='monitor_divisao_administrativa_data'),
]