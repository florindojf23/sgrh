from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gutilizador.models import *
from django.db import transaction
import datetime
from .models import *
from gfuncionarios.models import *

@login_required
def DashboardEstatistica(request):
	totalFuncionario = Funcionarios.objects.exclude(controlo_ativo='Desabilitar').all().count()
	totalFuncionarioM = Funcionarios.objects.exclude(controlo_ativo='Desabilitar').filter(sexo='Masculino').all().count()
	totalFuncionarioF = Funcionarios.objects.exclude(controlo_ativo='Desabilitar').filter(sexo='Feminino').all().count()

	contrlo_ativo_sexo = FuncionarioPivotCASEXO.objects.all() 
	tipo_funcionario_sexo = FuncionarioPivotTFSEXO.objects.all() 
	grupo_idade_sexo = FuncionarioPivotGISEXO.objects.all() 
	local_trabalho_sexo = FuncionarioPivotLTSEXO.objects.all() 
	context = {
		"title":f"Dashboard Dados Gerais",
		"legend":f"Dashboard Dados Gerais",
		"totalFuncionario":totalFuncionario,
		"totalFuncionarioM":totalFuncionarioM,
		"totalFuncionarioF":totalFuncionarioF,
		"contrlo_ativo_sexo":contrlo_ativo_sexo,
		"tipo_funcionario_sexo":tipo_funcionario_sexo,
		"grupo_idade_sexo":grupo_idade_sexo,
		"local_trabalho_sexo":local_trabalho_sexo,
		"page":'dashboard_report',
		"active_reports":'active',
	}
	return render(request, 'reports/dashboard.html', context)

@login_required
def ListaRelatorio1(request,assunto,id,genero):
	assunto = assunto
	if genero != 'Total':
		mgenero = str("com Genero ")+genero
	else:
		mgenero = str("")

	if assunto == 'controlo_ativo':
		if id=='Total' and genero != 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter(sexo=genero).exclude(controlo_ativo='Desabilitar')
		elif id=='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter().exclude(controlo_ativo='Desabilitar')
		elif id!='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter(controlo_ativo=id).exclude(controlo_ativo='Desabilitar')
		else:
			objects = ListaFuncionarioCompleto1.objects.filter(controlo_ativo=id,sexo=genero).exclude(controlo_ativo='Desabilitar')
	if assunto == 'tipo_funcionario':
		if id=='Total':
			objects = ListaFuncionarioCompleto1.objects.filter(sexo=genero).exclude(controlo_ativo='Desabilitar')
		elif id=='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter().exclude(controlo_ativo='Desabilitar')
		elif id!='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario=id).exclude(controlo_ativo='Desabilitar')
		else:
			objects = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario=id,sexo=genero).exclude(controlo_ativo='Desabilitar')
	if assunto == 'grupu_idade':
		idade = id.split('-')
		if id=='Total' and genero != 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter(sexo=genero).exclude(controlo_ativo='Desabilitar')
		elif id=='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter().exclude(controlo_ativo='Desabilitar')
		elif id!='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter(idade__gte=idade[0],idade__lte=idade[1]).exclude(controlo_ativo='Desabilitar')
		else:
			if idade[0] == '65+':
				objects = ListaFuncionarioCompleto1.objects.filter(idade__gte=65,sexo=genero).exclude(controlo_ativo='Desabilitar')
			else:
				objects = ListaFuncionarioCompleto1.objects.filter(idade__gte=idade[0],idade__lte=idade[1],sexo=genero).exclude(controlo_ativo='Desabilitar')
	if assunto == 'local_trabalho':
		if id=='Total' and genero != 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter(sexo=genero).exclude(controlo_ativo='Desabilitar')
		elif id=='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter().exclude(controlo_ativo='Desabilitar')
		elif id!='Total' and genero == 'Total':
			objects = ListaFuncionarioCompleto1.objects.filter(local_trabalho=id).exclude(controlo_ativo='Desabilitar')
		else:
			objects = ListaFuncionarioCompleto1.objects.filter(local_trabalho=id,sexo=genero).exclude(controlo_ativo='Desabilitar')
	
	context = {
		'link_antes': [{'link_name':"DashboardEstatistica",'link_text':"Dashboard Dados Gerais"}],
		"title":f"Lista Funcionarios {id}  {mgenero}",
		"legend":f"Lista Funcionarios {id}  {mgenero}",
		"objects":objects,
		"page":'dashboard_report',
		"active_reports":'active',
	}
	return render(request, 'reports/reportlistafuncionario.html', context)