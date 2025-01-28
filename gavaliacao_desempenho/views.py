from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gutilizador.models import *
from .models import *
from .forms import *
from django.db import transaction
from django.utils import timezone
now = timezone.now()

@login_required
def index(request):
	# objects = Funcionarios.objects.all()
	groups = request.user.groups.all()
	group_names = [group.name for group in groups]
	context = {
		"title":"Dashboard Avaliacao Desempenho",
		"legend":"Dashboard Avaliacao Desempenho",
		"active_dash_ad":'active',
		"page":'dash_ad',
		# "objects":objects,
	}
	return render(request,'desempenho/index.html',context)

@login_required
def ListaAnoAD(request):
	groups = request.user.groups.all()
	group_names = [group.name for group in groups]
	objects = Anos_AD.objects.all()
	context = {
		"title":"Dados Ano de Avaliação",
		"legend":"Dados Ano de Avaliação",
		"active_anos_ad":'active',
		"page":'anos_ad',
		"objects":objects,
	}
	return render(request,'desempenho/parametro/anos_ad_list.html',context)

@login_required
def RegistaAnoAD(request):
	groups = request.user.groups.all()
	group_names = [group.name for group in groups]
	
	if request.method == "POST":
		form = Anos_ADForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.inserido_por = request.user
				instance.save()
				messages.success(request, f'Ano de Avaliação foi inserido com sucesso!')
				return redirect('ListaAnoAD')
	else:
		form = Anos_ADForm()

	context = {
		"title":"Registar Ano de Avaliação",
		"legend":"Registar Ano de Avaliação",
		"active_anos_ad":'active',
		"page":'anos_ad',
		"form":form,
		# "objects":objects,
	}
	return render(request,'desempenho/forms.html',context)

@login_required
def AlteraAnoAD(request,id):
	groups = request.user.groups.all()
	group_names = [group.name for group in groups]
	objects = get_object_or_404(Anos_AD,id_anos=id)
	if request.method == "POST":
		form = Anos_ADForm(request.POST, request.FILES,instance=objects)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				messages.success(request, f'Ano de Avaliação foi inserido com sucesso!')
				return redirect('ListaAnoAD')
	else:
		form = Anos_ADForm(instance=objects)

	context = {
		"title":"Alterar Ano de Avaliação",
		"legend":"Alterar Ano de Avaliação",
		"active_anos_ad":'active',
		"page":'anos_ad',
		"form":form,
		# "objects":objects,
	}
	return render(request,'desempenho/forms.html',context)

@login_required
def DetalhoFuncionarioListaAD(request,id):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Gad_ficha_avaliacao_desempenho.objects.filter(controlo_estado__isnull=True).filter(funcionario=objects).order_by('-ano_ad')
	context = {
	'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":f"Dados Avaliação Desempenho {objects.nome}",
		"legend":f"Dados Avaliação Desempenho {objects.nome}",
		"objects":objects,
		"objects1":objects1,
		"page":'detalho_funcionario_lista_ad',
		"active_det_fun_list_ad":'active',
	}
	return render(request, 'gad/detalho_ad_funcionario.html', context)


@login_required
def RegistaNovoAD(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Gad_ficha_avaliacao_desempenhoForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.inserido_por = request.user
				instance.save()
				messages.success(request, f'Nova Ficha de Avaliação Desempenho foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaAD',objects.id)
	else:
		form = Gad_ficha_avaliacao_desempenhoForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha de Avaliação Desempenho",
		"legend":"Inserir Ficha de Avaliação Desempenho",
		"page":"form_ad_fun",
		"active_inserir_ad_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def AlterarAD(request,id):
	objects1 = get_object_or_404(Gad_ficha_avaliacao_desempenho,id_avaliacao_desempenho=id)
	objects = Funcionarios.objects.get(id=objects1.funcionario.id)
	if request.method == "POST":
		form = Gad_ficha_avaliacao_desempenhoForm(request.POST, request.FILES,instance=objects1)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				messages.success(request, f'Ficha de Avaliação Desempenho foi alterado com sucesso!')
				return redirect('DetalhoFuncionarioListaAD',objects.id)
	else:
		form = Gad_ficha_avaliacao_desempenhoForm(instance=objects1)
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetalhoFuncionarioListaAD",'link_param':f"{objects.id}",'link_text':f"Dados Avaliação Desempenho {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Alterar Ficha de Avaliação Desempenho",
		"legend":"Alterar Ficha de Avaliação Desempenho",
		"page":"form_ad_fun",
		"active_alterar_ad_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def DesabilitarAD(request,id):
	objects1 = get_object_or_404(Gad_ficha_avaliacao_desempenho,id_avaliacao_desempenho=id)
	objects = Funcionarios.objects.get(id=objects1.funcionario.id)
	objects1.controlo_estado = 'Desabilitar'
	objects1.save()
	messages.error(request, f'Dados Avaliação Desempenho do Ano {objects1.ano_ad} foi Desabilitado com sucesso!')
	return redirect('DetalhoFuncionarioListaAD',objects.id)
	