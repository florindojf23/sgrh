from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from gutilizador.decorators import allowed_users
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from datetime import date

@login_required
# @allowed_users(allowed_roles=['admin','Cordenador Laboratorio','Director','Vice Director'])
def ChartFuncionarioPivotCASEXO(request):
	group = request.user.groups.all()[0].name
	funcionario_data = FuncionarioPivotCASEXO.objects.all()
	labels = []
	masculino_data = []
	feminino_data = []
	total_data = []
	for x in funcionario_data:
		labels.append(x.controlo_ativo)
		masculino_data.append(x.masculino)
		feminino_data.append(x.feminino)
		total_data.append(x.total)
	return JsonResponse(data={
		'labels':labels,
		'datasets':[
			{
                'label': 'Feminino',
                'data': feminino_data,
                'backgroundColor': 'rgba(54, 162, 235, 0.9)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Masculino',
                'data': masculino_data,
                'backgroundColor': 'rgba(255, 99, 132, 0.9)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Total',
                'data': total_data,
                'backgroundColor': 'rgba(75, 192, 192, 0.9)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }
		],
		})

@login_required
# @allowed_users(allowed_roles=['admin','Cordenador Laboratorio','Director','Vice Director'])
def ChartFuncionarioPivotTFSEXO(request):
	group = request.user.groups.all()[0].name
	funcionario_data = FuncionarioPivotTFSEXO.objects.all()
	labels = []
	masculino_data = []
	feminino_data = []
	total_data = []
	for x in funcionario_data:
		labels.append('AAP' if x.tipo_funcionario == 'Agente Administração Pública' else x.tipo_funcionario )
		masculino_data.append(x.masculino)
		feminino_data.append(x.feminino)
		total_data.append(x.total)
	return JsonResponse(data={
		'labels':labels,
		'datasets':[
			{
                'label': 'Feminino',
                'data': feminino_data,
                'backgroundColor': 'rgba(54, 162, 235, 0.8)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Masculino',
                'data': masculino_data,
                'backgroundColor': 'rgba(255, 99, 132, 0.8)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Total',
                'data': total_data,
                'backgroundColor': 'rgba(75, 192, 192, 0.8)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }
		],
		})

@login_required
# @allowed_users(allowed_roles=['admin','Cordenador Laboratorio','Director','Vice Director'])
def ChartFuncionarioPivotGISEXO(request):
    group = request.user.groups.all()[0].name
    funcionario_data = FuncionarioPivotGISEXO.objects.all()
    labels = []
    masculino_data = []
    feminino_data = []
    total_data = []
    for x in funcionario_data:
        # labels.append('AAP' if x.tipo_funcionario == 'Agente Administração Pública' else x.tipo_funcionario )
        labels.append(x.grupu_idade)
        masculino_data.append(x.masculino)
        feminino_data.append(x.feminino)
        total_data.append(x.total)
    return JsonResponse(data={
        'labels':labels,
        'datasets':[
            {
                'label': 'Feminino',
                'data': feminino_data,
                'backgroundColor': 'rgba(54, 162, 235, 0.8)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Masculino',
                'data': masculino_data,
                'backgroundColor': 'rgba(255, 99, 132, 0.8)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Total',
                'data': total_data,
                'backgroundColor': 'rgba(75, 192, 192, 0.8)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }
        ],
        })

@login_required
# @allowed_users(allowed_roles=['admin','Cordenador Laboratorio','Director','Vice Director'])
def ChartFuncionarioPivotLTSEXO(request):
    group = request.user.groups.all()[0].name
    funcionario_data = FuncionarioPivotLTSEXO.objects.all()
    labels = []
    masculino_data = []
    feminino_data = []
    total_data = []
    for x in funcionario_data:
        # labels.append('AAP' if x.tipo_funcionario == 'Agente Administração Pública' else x.tipo_funcionario )
        labels.append(x.local_trabalho)
        masculino_data.append(x.masculino)
        feminino_data.append(x.feminino)
        total_data.append(x.total)
    return JsonResponse(data={
        'labels':labels,
        'datasets':[
            {
                'label': 'Feminino',
                'data': feminino_data,
                'backgroundColor': 'rgba(54, 162, 235, 0.8)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Masculino',
                'data': masculino_data,
                'backgroundColor': 'rgba(255, 99, 132, 0.8)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Total',
                'data': total_data,
                'backgroundColor': 'rgba(75, 192, 192, 0.8)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }
        ],
        })

