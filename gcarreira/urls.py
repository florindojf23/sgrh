from django.urls import path
from .views import *

urlpatterns = [
	path('index.html',index,name='lista-carreira'),
	
	path('carreira_data',carreira_data,name='carreira_data'),
]