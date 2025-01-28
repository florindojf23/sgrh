from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gutilizador.models import *
from .models import *
from .forms import *
from django.db import transaction
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q

@login_required
def index(request):
	# objects = Gdivisao_administrativa_aldeia.objects.all().filter(data_fim__isnull=True,suco__data_fim__isnull=True,suco__posto__data_fim__isnull=True,suco__posto__municipio__data_fim__isnull=True)
	objects = Gdivisao_administrativa_municipio.objects.all()
	# print(objects)/
	context = {
		"title":"Dados Divisao Administrativa",
		"legend":"Dados Divisao Administrativa",
		"objects":objects,
		"page":'municipio',
		"active_mun":'active',
	}
	return render(request,'divisao_administrativa/index.html',context)

@login_required
def monitor_divisao_administrativa_data(request):
	start = int(request.GET.get('start', 0))
	length = int(request.GET.get('length', 10))
	search_value = request.GET.get('search[value]', '')
	draw = int(request.GET.get('draw', 1))
	municipio = request.GET.get('municipio', '')
	posto = request.GET.get('posto', '')
	suco = request.GET.get('suco', '')
	aldeia = request.GET.get('aldeia', '')

	# Handle ordering
	order_column_index = int(request.GET.get('order[0][column]', 0))
	order_direction = request.GET.get('order[0][dir]', 'asc')

	column_mapping = {
		0: 'id_municipio',  # Assuming first column is a combination, you can use 'id' or another field
		1: 'municipio',  # Corresponds to 'nome_do_funcionario'
		3: 'posto',
		2: 'suco',
		4: 'aldeia',
	}
	order_column = column_mapping.get(order_column_index, 'id')
	if order_direction == 'desc':
		order_column = f'-{order_column}'
	# Query the database
	data_objects = ViewDivisaoAdministrativa.objects.all()
	allTotal = data_objects.count()
	if municipio:
		data_objects = data_objects.filter(municipio__icontains=municipio)
	if posto:
		data_objects = data_objects.filter(posto__icontains=posto)
	if suco:
		data_objects = data_objects.filter(suco__icontains=suco)
	if aldeia:
		data_objects = data_objects.filter(aldeia__icontains=aldeia)
	# Apply ordering
	data_objects = data_objects.order_by(order_column)
	# Pagination
	paginator = Paginator(data_objects, length)
	page = paginator.get_page(start // length + 1)
	totalFiltered = data_objects.count()
	# Prepare data for DataTables
	data = []
	for idx, dados in enumerate(page.object_list, start=1):
		data.append({
        	'id': dados.id_municipio,
        	'municipio': dados.municipio,
        	'posto': dados.posto,
        	'suco': dados.suco,
        	'aldeia': dados.aldeia,
    	})
	response = {
		"draw": draw,
		"recordsTotal": paginator.count,
		"recordsFiltered": paginator.count,
		"totalFiltered": totalFiltered,
		"allTotal": allTotal,
		"data": data,
	}
	return JsonResponse(response)



