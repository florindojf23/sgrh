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

@login_required
def index(request):
	# objects = Gcarreira_indice.objects.all()
	regime = Gcarreira_regime.objects.all()
	context = {
		"title":"Dados Carreiras",
		"legend":"Dados Carreiras",
		"regime":regime,
	}
	return render(request,'carreira/index.html',context)

@login_required
def carreira_data(request):
	start = int(request.GET.get('start', 0))
	length = int(request.GET.get('length', 10))
	search_value = request.GET.get('search[value]', '')
	draw = int(request.GET.get('draw', 1))
	regime = request.GET.get('regime', '')
	categoria = request.GET.get('categoria', '')
	# controlo_ativo = request.GET.get('controlo_ativo', '')
	# sexo = request.GET.get('sexo', '')

	# Query the database
	# objects = Gcarreira_indice.objects.filter(data_fim__isnull=True)
	objects = Gcarreira_indice.objects.filter()
	if regime:
		print("----------------------id_regime----------------------",regime)
		objects = objects.filter(escalao__categoria__regime__id_regime=regime).order_by('escalao__escalao')
	if categoria:
		objects = objects.filter(escalao__categoria__id_categoria=categoria).order_by('escalao__escalao')
	# if controlo_ativo:
	# 	objects = objects.filter(controlo_ativo=controlo_ativo)
	# if sexo:
	# 	objects = objects.filter(sexo=sexo)

	# Pagination
	paginator = Paginator(objects, length)
	page = paginator.get_page(start // length + 1)

	# Prepare data for DataTables
	data = []
	for idx, obj in enumerate(page.object_list, start=1):
		if obj.data_fim:
			estado = 'Não Ativo'
		else:
			estado = 'Ativo'

		data.append({
        	'id_indice': obj.id_indice,
        	'indice': obj.indice,
        	'estado': estado,
        	'escalao': obj.escalao.escalao,
        	'categoria': obj.escalao.categoria.categoria,
        	'regime': obj.escalao.categoria.regime.regime,
    	})

	response = {
		"draw": draw,
		"recordsTotal": paginator.count,
		"recordsFiltered": paginator.count,
		"data": data,
	}
	return JsonResponse(response)


