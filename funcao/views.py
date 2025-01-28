from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gutilizador.models import *
from .models import *
from .forms import *
from django.db import transaction
import datetime
from django.utils import timezone
from django.http import JsonResponse
now = timezone.now()
from gfuncionarios.models import ListaFuncionarioCompleto1


@login_required
def DashboardFuncao(request):
	permanente = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Permanente').count()
	aap = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Agente Administração Pública').count()
	nulo = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Não tem ficha Função').count()
	casuais = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Casuais').count()
	context = {
		"title":f"Dashboard Gestão Função",
		"legend":f"Dashboard Gestão Função",
		'permanente':permanente,'aap':aap,'nulo':nulo,'casuais':casuais,
		"page":'dashboard-funcao',
	}
	return render(request, 'gestao_funcao/dash.html', context)
	

@login_required
def load_form_progressao(request):
    id_tipo_alteracao_ficha = request.GET.get('id_tipo_alteracao_ficha')
    id_fun = request.GET.get('id_fun')
    ultima_ficha_permanente = Ficha_permanente.objects.filter(funcionario__id=id_fun)
    relacao_juridica = Relacao_juridica_emprego.objects.filter(id_rje='8d69cc30-b04c-44e7-a18c-6e2de566a221').values('id_rje', 'relacao_juridica_emprego')
    return JsonResponse(list(relacao_juridica), safe=False)

@login_required
def load_categorias(request):
    regime_id = request.GET.get('regime_id')
    categorias = Gcarreira_categoria.objects.filter(regime__id_regime=regime_id).values('id_categoria', 'categoria')
    return JsonResponse(list(categorias), safe=False)

@login_required
def load_escalaos(request):
    categoria_id = request.GET.get('categoria_id')
    escalaos = Gcarreira_escalao.objects.filter(categoria__id_categoria=categoria_id).values('id_escalao', 'escalao')
    return JsonResponse(list(escalaos), safe=False)

@login_required
def load_indices(request):
    escalao_id = request.GET.get('escalao_id')
    indices = Gcarreira_indice.objects.filter(escalao__id_escalao=escalao_id,data_fim__isnull=True).values('id_indice', 'indice')
    return JsonResponse(list(indices), safe=False)


def controlo_ativo_funcionario(id_funcionario):
	print("id_funcionario:",id_funcionario)
	objects = Funcionarios.objects.get(id=id_funcionario)
	contratacao = objects.getContratacao()
	permanente = objects.getPermanente()
	fne = objects.getFNE()
	fsd = objects.getFSD()
	print("contratacao:",contratacao)
	if contratacao and not fne:
		print("tama:",fsd)
		if fsd:
			if fsd.data_saida > contratacao.data_inicio:
				objects.controlo_ativo = 'Saída Definitiva'
			else:
				objects.controlo_ativo = 'Ativo'
		else:
			objects.controlo_ativo = 'Ativo'
	elif permanente and not fne:
		print("tama1:",fsd)
		if fsd:
			if fsd.data_saida > permanente.data_inicio:
				objects.controlo_ativo = 'Saída Definitiva'
			else:
				objects.controlo_ativo = 'Ativo'
		else:
			objects.controlo_ativo = 'Ativo'
	elif fne:
		objects.controlo_ativo = 'Não Exercício'
	elif fsd:
		objects.controlo_ativo = 'Saída Definitiva'
	else:
		objects.controlo_ativo = objects.controlo_ativo
	objects.save()
	return objects


@login_required
def DetalhoFuncionarioListaFuncao(request,id):
	objects = Funcionarios.objects.get(id=id)
	objects = controlo_ativo_funcionario(id)
	objects1 = Ficha_contratacao.objects.filter(controlo_estado__isnull=True).filter(funcionario=objects).order_by('-data_inicio')
	objects2 = Ficha_permanente.objects.filter(controlo_estado__isnull=True).filter(funcionario=objects).order_by('-data_inicio')
	objects3 = Ficha_comissao_servico.objects.filter(controlo_estado__isnull=True).filter(funcionario=objects).order_by('-data_inicio')
	objects4 = Ficha_casual.objects.filter(controlo_estado__isnull=True).filter(funcionario=objects).order_by('-data_inicio')
	context = {
	'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":f"Dados Função {objects.nome}",
		"legend":f"Dados Função {objects.nome}",
		"objects":objects,
		"objects1":objects1,
		"objects2":objects2,
		"objects3":objects3,
		"objects4":objects4,
		"page":'detalho_funcionario_lista_funcao',
		"active_det_fun_list_fun":'active',
	}
	return render(request, 'gfuncao/detalho_funcao_funcionario.html', context)


@login_required
def RegistaNovoContratacao(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Ficha_contratacaoForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.inserido_por = request.user
				instance.save()
				messages.success(request, f'Nova Contratação foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaFuncao',objects.id)
	else:
		form = Ficha_contratacaoForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha de Contratação",
		"legend":"Inserir Ficha de Contratação",
		"page":"form_funcao_fun",
		"active_inserir_funcao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def UpdateContratacao(request,id,ffid):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_contratacao.objects.get(id_contratacao=ffid)
	if request.method == "POST":
		form = Ficha_contratacaoForm(request.POST, request.FILES,instance=objects1)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				messages.success(request, f'Dados Ficha Contratação foi alterado com sucesso!')
				return redirect('DetalhoFuncionarioListaFuncao',objects.id)
	else:
		form = Ficha_contratacaoForm(instance=objects1)
	link_antes = [
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"},
		{'link_name':"DetalhoFuncionarioListaFuncao",'link_param':f"{objects.id}",'link_text':f"Ficha Função"},
	]
	context = {
		'link_antes':link_antes,
		"title":"Alterar Ficha de Contratação",
		"legend":"Alterar Ficha de Contratação",
		"page":"form_funcao_fun",
		"active_alterar_funcao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)


@login_required
def DesabilitarContratacao(request,id,ffid):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_contratacao.objects.get(id_contratacao=ffid)
	objects1.controlo_estado = 'Desabilitar'
	objects1.alterado_por = request.user.username
	objects1.alterado_em = now
	objects1.save()
	messages.error(request, f'Dados Ficha Contratação foi desabilitar com sucesso!')
	return redirect('DetalhoFuncionarioListaFuncao',objects.id)

@login_required
def RegistaNovoPermanente(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Ficha_permanenteForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.inserido_por = request.user.username
				instance.save()
				messages.success(request, f'Nova Ficha Permanente foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaFuncao',objects.id)
	else:
		form = Ficha_permanenteForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha Permanente",
		"legend":"Inserir Ficha Permanente",
		"page":"form_funcao_fun",
		"active_inserir_funcao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def UpdatePermanente(request,id,ffid):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_permanente.objects.get(id_permanente=ffid)
	if request.method == "POST":
		form = Ficha_permanenteForm(request.POST, request.FILES,instance=objects1)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				messages.success(request, f'Dados Ficha Permanente foi alterado com sucesso!')
				return redirect('DetalhoFuncionarioListaFuncao',objects.id)
	else:
		form = Ficha_permanenteForm(instance=objects1)
	link_antes = [
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"},
		{'link_name':"DetalhoFuncionarioListaFuncao",'link_param':f"{objects.id}",'link_text':f"Ficha Função"},
	]
	context = {
		'link_antes':link_antes,
		"title":"Alterar Ficha de Permanente",
		"legend":"Alterar Ficha de Permanente",
		"page":"form_funcao_fun",
		"active_alterar_funcao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)


@login_required
def DesabilitarPermanente(request,id,ffid):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_permanente.objects.get(id_permanente=ffid)
	objects1.controlo_estado = 'Desabilitar'
	objects1.alterado_por = request.user.username
	objects1.alterado_em = now
	objects1.save()
	messages.error(request, f'Dados Ficha Permanente foi desabilitar com sucesso!')
	return redirect('DetalhoFuncionarioListaFuncao',objects.id)

@login_required
def RegistaComissao_servico(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Ficha_comissao_servicoForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.inserido_por = request.user.username
				instance.save()
				messages.success(request, f'Nova Ficha Comissão de Serviço foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaFuncao',objects.id)
	else:
		form = Ficha_comissao_servicoForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha Comissão de Serviço",
		"legend":"Inserir Ficha Comissão de Serviço",
		"page":"form_funcao_fun",
		"active_inserir_funcao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def UpdateComissao_servico(request,id,idfcs):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_comissao_servico.objects.get(id_comissao_servico=idfcs)
	if request.method == "POST":
		form = Ficha_comissao_servicoForm(request.POST, request.FILES,instance=objects1)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				messages.success(request, f'Dados Ficha Comissão Serviço foi alterado com sucesso!')
				return redirect('DetalhoFuncionarioListaFuncao',objects.id)
	else:
		form = Ficha_comissao_servicoForm(instance=objects1)
	link_antes = [
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"},
		{'link_name':"DetalhoFuncionarioListaFuncao",'link_param':f"{objects.id}",'link_text':f"Ficha Função"},
	]
	context = {
		'link_antes':link_antes,
		"title":"Alterar Ficha de Contratação Serviço",
		"legend":"Alterar Ficha de Contratação Serviço",
		"page":"form_funcao_fun",
		"active_alterar_funcao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)


@login_required
def DesabilitarComissao_servico(request,id,idfcs):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_comissao_servico.objects.get(id_comissao_servico=idfcs)
	objects1.controlo_estado = 'Desabilitar'
	objects1.alterado_por = request.user.username
	objects1.alterado_em = now
	objects1.save()
	messages.error(request, f'Dados Ficha Contratação de Serviço foi desabilitar com sucesso!')
	return redirect('DetalhoFuncionarioListaFuncao',objects.id)

@login_required
def RegistaNovoFichaCasual(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Ficha_casualForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.inserido_por = request.user.username
				instance.save()
				messages.success(request, f'Nova Ficha Casuais foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaFuncao',objects.id)
	else:
		form = Ficha_casualForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha Casual",
		"legend":"Inserir Ficha Casual",
		"page":"form_funcao_fun_casual",
		"active_inserir_funcao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)