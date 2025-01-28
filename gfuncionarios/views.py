from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gutilizador.models import *
from .models import *
from .forms import *
from funcao.forms import *
from django.db import transaction
import datetime
from datetime import date
from django.utils import timezone
now = timezone.now()
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
import base64

@login_required
def index(request):
	local_trabalho = Gdivisao_administrativa_municipio.objects.filter().all()
	tipo_funcionario = ListaFuncionarioCompleto1.objects.values_list('tipo_funcionario', flat=True).distinct()
	print("tipo_funcionario:",tipo_funcionario)
	context = {
		"title":"Lista Funcionarios",
		"legend":"Lista Funcionarios",
		"local_trabalho":local_trabalho,
		"tipo_funcionario":tipo_funcionario,
	}
	return render(request, 'funcionario/index.html', context)


@login_required
def funcionarios_data(request):
	start = int(request.GET.get('start', 0))
	length = int(request.GET.get('length', 10))
	search_value = request.GET.get('search[value]', '')
	draw = int(request.GET.get('draw', 1))
	nome_fun = request.GET.get('nome_fun', '')
	id_sigap = request.GET.get('id_sigap', '')
	# controlo_ativo = request.GET.get('controlo_ativo', '')
	controlo_ativo = request.GET.getlist('controlo_ativo', [])
	print("Received values for controlo_ativo:", controlo_ativo)
	sexo = request.GET.get('sexo', '')
	id_grp = request.GET.get('id_grp', '')
	unidade = request.GET.get('unidade', '')
	local_trabalho = request.GET.get('local_trabalho', '')
	tipo_funcionario = request.GET.get('tipo_funcionario', '')

	# Handle ordering
	order_column_index = int(request.GET.get('order[0][column]', 0))
	order_direction = request.GET.get('order[0][dir]', 'asc')

	column_mapping = {
		0: 'id',  # Assuming first column is a combination, you can use 'id' or another field
		1: 'nome',  # Corresponds to 'nome_do_funcionario'
		2: 'sexo',
		3: 'id_sigap',
		4: 'id_grp',
		5: 'data_nascimento',
		6: 'unidade',
		7: 'local_trabalho',
		8: 'tipo_funcionario',  # Assuming 'quadro' maps to this
		9: 'categoria_cargo',  # Assuming 'cargo' maps to this
		10: 'idade'
	}
	order_column = column_mapping.get(order_column_index, 'id')
	if order_direction == 'desc':
		order_column = f'-{order_column}'

	# Query the database
	funcionarios = ListaFuncionarioCompleto1.objects.exclude(controlo_ativo='Desabilitar')
	print("funcionarios:",funcionarios)
	allTotal = funcionarios.count()
	if nome_fun:
		funcionarios = funcionarios.filter(nome__icontains=nome_fun)
	if id_sigap:
		funcionarios = funcionarios.filter(id_sigap__icontains=id_sigap)
	if controlo_ativo:
		funcionarios = funcionarios.filter(controlo_ativo__in=controlo_ativo)
	if sexo:
		funcionarios = funcionarios.filter(sexo=sexo)
	if id_grp:
		funcionarios = funcionarios.filter(id_grp__icontains=id_grp)
	if unidade:
		funcionarios = funcionarios.filter(unidade__icontains=unidade)
	if local_trabalho:
		funcionarios = funcionarios.filter(local_trabalho=local_trabalho)
	if tipo_funcionario:
		funcionarios = funcionarios.filter(tipo_funcionario=tipo_funcionario)

	# Apply ordering
	funcionarios = funcionarios.order_by(order_column)

	# Pagination
	paginator = Paginator(funcionarios, length)
	page = paginator.get_page(start // length + 1)
	totalFiltered = funcionarios.count()


	# Prepare data for DataTables
	data = []
	for idx, funcionario in enumerate(page.object_list, start=1):
		# image_base64 = ""
		# if funcionario.dados_imajen:
			# image_base64 = base64.b64encode(funcionario.dados_imajen).decode('utf-8')
		data.append({
        	'id': funcionario.id,
        	'estado': funcionario.controlo_ativo,
        	'nome_do_funcionario': funcionario.nome,
        	'sexo': funcionario.sexo,
        	'id_sigap': funcionario.id_sigap,
        	'id_grp': funcionario.id_grp,
        	'data_nascimento': funcionario.data_nascimento.strftime('%d/%m/%Y') if funcionario.data_nascimento else "",
        	'unidade': funcionario.unidade,
        	'local_trabalho': funcionario.local_trabalho,
        	'quadro': funcionario.tipo_funcionario,
        	'cargo': funcionario.categoria_cargo,
        	'idade': funcionario.idade,
        	'image_base64': funcionario.dados_imajen if funcionario.dados_imajen else "",
    	})# for idx, funcionario in enumerate(page.object_list, start=1)]

	response = {
		"draw": draw,
		"recordsTotal": paginator.count,
		"recordsFiltered": paginator.count,
		"totalFiltered": totalFiltered,
		"allTotal": allTotal,
		"data": data,
	}
	return JsonResponse(response)

@login_required
def DetailFuncionario(request,idf):
	print("idf:",idf)
	objects = Funcionarios.objects.get(id=idf)
	context = {
		'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":f"Detalho Funcionario {objects.nome}",
		"legend":f"Detalho Funcionario {objects.nome}",
		"objects":objects,
		"page":"detalho_fun",
		"activeDadosPessoais":'active',
	}
	return render(request, 'funcionario/detalho_identificacao.html', context)

import base64

@login_required
def RegistaNovoFuncionario(request):
	if request.method == "POST":
		form = FuncionariosForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				# image_file = request.FILES['imagem']
				# print("tama")
				# print(image_file)
				# image_data = image_file.read()
				# base64_encoded_image = base64.b64encode(image_data).decode('utf-8')
				# input_dados = base64_encoded_image
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				instance.inserido_por = request.user
				instance.save()
				messages.success(request, f'O novo Funcionario foi inserido com sucesso!')
				return redirect('lista-funcionarios')
	else:
		form = FuncionariosForm()
	context = {
		'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":"Registo Novo Funcionario",
		"legend":"Registo Novo Funcionario",
		"form":form,
	}
	return render(request, 'funcionario/form.html', context)

@login_required
def AtualizarFuncionario(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = FuncionariosForm(request.POST, request.FILES,instance=objects)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = datetime.datetime.now()
				instance.save()
				messages.success(request, f'O Funcionario foi alterado com sucesso!')
				return redirect('DetailFuncionario',objects.id)
	else:
		form = FuncionariosForm(instance=objects)
	context = {
		'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":f"Alterar Funcionario {objects.nome}",
		"legend":f"Alterar Funcionario {objects.nome}",
		"form":form,
		"objects":objects,
		"activeDadosPessoais":"active",
		"page":'alterar_fun',
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def DesabilitarFuncionario(request,id):
	objects = Funcionarios.objects.get(id=id)
	objects.controlo_ativo = 'Desabilitar'
	objects.save()
	messages.error(request, f'O Funcionario {objects.nome} ({objects.id_sigap}) foi desabilitar com sucesso!')
	return redirect('lista-funcionarios')
	
# colocacao


@login_required
def DetalhoFuncionarioListaColocacao(request,id):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_colocacao.objects.exclude(controlo_estado='Desabilitar').filter(funcionario=objects).all().order_by('-data_inicio')
	# objects2 = Ficha_permanente.objects.filter(controlo_estado__isnull=True).order_by('-data_inicio')
	context = {
	'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":f"Dados Colocação {objects.nome}",
		"legend":f"Dados Colocação {objects.nome}",
		"objects":objects,
		"objects1":objects1,
		# "objects2":objects2,
		"page":'detalho_funcionario_lista_colocacao',
		"active_det_col_list_fun":'active',
	}
	return render(request, 'colocacao/detalho_colocacao_funcionario.html', context)




@login_required
def DetalhoFuncionarioRegistarColocacao(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Ficha_colocacaoForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				data_inicio = instance.data_inicio
				data_fim = instance.data_fim
				if not data_fim:
					ficha_colocacao = Ficha_colocacao.objects.filter(funcionario=objects,controlo_estado__isnull=True).order_by('-data_inicio').first()
					if ficha_colocacao:
						ficha_colocacao.data_fim = data_inicio
						ficha_colocacao.save()
				elif data_fim > date.today():
					ficha_colocacao = Ficha_colocacao.objects.filter(funcionario=objects,controlo_estado__isnull=True).order_by('-data_inicio').first()
					if ficha_colocacao:
						ficha_colocacao.data_fim = data_inicio
						ficha_colocacao.save()
				instance.inserido_por = request.user.username
				instance.save()
				messages.success(request, f'Nova Ficha Colocação foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaColocacao',objects.id)
	else:
		form = Ficha_colocacaoForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha Colocação",
		"legend":"Inserir Ficha Colocação",
		"page":"form_colocacao_fun",
		"active_inserir_colocacao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def UpdateColocacao(request,id,idfc):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_colocacao.objects.get(id_colocacao=idfc)
	if request.method == "POST":
		form = Ficha_colocacaoForm(request.POST, request.FILES,instance=objects1)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				messages.success(request, f'Ficha Colocação foi alterado com sucesso!')
				return redirect('DetalhoFuncionarioListaColocacao',objects.id)
	else:
		form = Ficha_colocacaoForm(instance=objects1)
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Alterar Ficha Colocação",
		"legend":"Alterar Ficha Colocação",
		"page":"form_colocacao_fun",
		"active_alterar_colocacao_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def DesabilitarColocacao(request,id,idfc):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_colocacao.objects.get(id_colocacao=idfc)
	objects1.controlo_estado = 'Desabilitar'
	objects1.alterado_por = request.user.username
	objects1.alterado_em = now
	objects1.save()
	messages.error(request, f'Ficha Colocação foi desabilitar com sucesso!')
	return redirect('DetalhoFuncionarioListaColocacao',objects.id)


# nao exercicio
@login_required
def DetalhoFuncionarioListaNaoExercicio(request,id):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_nao_exercicio.objects.exclude(controlo_estado='Desabilitar').filter(funcionario=objects).all().order_by('-data_inicio')
	# objects1 = Ficha_nao_exercicio.objects.exclude(controlo_estado='Desabilitar').filter(funcionario=objects).all().order_by('-data_inicio')
	if objects.getFNE():
		objects.controlo_ativo = 'Não Exercício'
		objects.save()
	else:
		objects.controlo_ativo = objects.controlo_ativo
		objects.save()


	# objects2 = Ficha_permanente.objects.filter(controlo_estado__isnull=True).order_by('-data_inicio')
	context = {
	'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":f"Dados Não Exercício {objects.nome}",
		"legend":f"Dados Não Exercício {objects.nome}",
		"objects":objects,
		"objects1":objects1,
		# "objects2":objects2,
		"page":'detalho_funcionario_lista_nao_exercicio',
		"active_det_nexer_list_fun":'active',
	}
	return render(request, 'estado_funcionario/detalho_nao_exercicio.html', context)

@login_required
def DetalhoFuncionarioRegistarFNExercicio(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Ficha_nao_exercicioForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				instance.inserido_por = request.user.username
				data_fim = instance.data_fim
				if data_fim and data_fim > date.today():
					objects.controlo_ativo = 'Não Exercício'
				else:
					objects.controlo_ativo = 'Ativo'
				instance.save()
				objects.save()
				messages.success(request, f'Nova Ficha Não Exercício foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaNaoExercicio',objects.id)
	else:
		form = Ficha_nao_exercicioForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha Não Exercício",
		"legend":"Inserir Ficha Não Exercício",
		"page":"form_nao_exercicio_fun",
		"active_inserir_fne_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def UpdateFNExercicio(request,id,idfne):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_nao_exercicio.objects.get(id_nao_exercicio=idfne)
	if request.method == "POST":
		form = Ficha_nao_exercicioForm(request.POST, request.FILES,instance=objects1)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				data_fim = instance.data_fim
				if data_fim and data_fim > date.today():
					print("data_fim:",data_fim)
					objects.controlo_ativo = 'Não Exercício'
				else:
					print("data_fim1:",data_fim)
					objects.controlo_ativo = 'Ativo'
				instance.save()
				objects.save()
				messages.success(request, f'Ficha Não Exercício foi alterado com sucesso!')
				return redirect('DetalhoFuncionarioListaNaoExercicio',objects.id)
	else:
		form = Ficha_nao_exercicioForm(instance=objects1)
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Alterar Ficha Não Exercício",
		"legend":"Alterar Ficha Não Exercício",
		"page":"form_nao_exercicio_fun",
		"active_alterar_fne_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def DesabilitarFNExercicio(request,id,idfne):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_nao_exercicio.objects.get(id_nao_exercicio=idfne)
	objects1.controlo_estado = 'Desabilitar'
	objects1.alterado_por = request.user.username
	objects1.alterado_em = now
	objects1.save()
	messages.error(request, f'Ficha Não Exercício foi desabilitar com sucesso!')
	return redirect('DetalhoFuncionarioListaNaoExercicio',objects.id)


# dados saida definitiva
@login_required
def DetalhoFuncionarioListaSaida(request,id):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_saida_definitiva.objects.exclude(controlo_estado='Desabilitar').filter(funcionario=objects).all().order_by('-data_saida')
	
	context = {
	'link_antes': [{'link_name':"lista-funcionarios",'link_text':"Lista Funcionarios"}],
		"title":f"Dados Saída Definitiva {objects.nome}",
		"legend":f"Dados Saída Definitiva {objects.nome}",
		"objects":objects,
		"objects1":objects1,
		"page":'detalho_funcionario_lista_saida',
		"active_det_saida_list_fun":'active',
	}
	return render(request, 'estado_funcionario/detalho_saida_definitiva.html', context)

@login_required
def DetalhoFuncionarioRegistarFSaida(request,id):
	objects = Funcionarios.objects.get(id=id)
	if request.method == "POST":
		form = Ficha_saida_definitivaForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.funcionario = objects
				data_de_saida = instance.data_saida
				instance.inserido_por = request.user.username
				instance.save()
				contratacao = objects.getContratacao()
				permanente = objects.getPermanente()
				if contratacao:
					if data_de_saida > contratacao.data_inicio:
						objects.controlo_ativo = 'Saída Definitiva'
						contratacao.data_fim =  data_de_saida-datetime.timedelta(days=1)
						contratacao.save()
					else:
						objects.controlo_ativo = 'Ativo'
				else:
					objects.controlo_ativo = 'Saída Definitiva'


				if permanente:
					print("permanente:",permanente.data_inicio)
					print("data_de_saida:",data_de_saida)
					if data_de_saida > permanente.data_inicio:
						objects.controlo_ativo = 'Saída Definitiva'
						permanente.data_fim =  data_de_saida-datetime.timedelta(days=1)
						permanente.save()
					else:
						objects.controlo_ativo = 'Ativo'
				else:
					objects.controlo_ativo = 'Saída Definitiva'
				objects.save()

				messages.success(request, f'Nova Ficha Saída foi inserido com sucesso!')
				return redirect('DetalhoFuncionarioListaSaida',objects.id)
	else:
		form = Ficha_saida_definitivaForm()
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Inserir Ficha Saída",
		"legend":"Inserir Ficha Saída",
		"page":"form_saida_fun",
		"active_inserir_fsd_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def DetalhoFuncionarioAlterarFSaida(request,id,idfsd):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_saida_definitiva.objects.get(id_saida=idfsd)
	if request.method == "POST":
		form = Ficha_saida_definitivaForm(request.POST, request.FILES,instance=objects1)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				data_de_saida = instance.data_saida
				instance.save()
				contratacao = objects.getContratacao()
				permanente = objects.getPermanente()
				if contratacao:
					if data_de_saida > contratacao.data_inicio:
						objects.controlo_ativo = 'Saída Definitiva'
						contratacao.data_fim =  data_de_saida-datetime.timedelta(days=1)
						contratacao.save()
					else:
						objects.controlo_ativo = 'Ativo'
				else:
					objects.controlo_ativo = 'Saída Definitiva'


				if permanente:
					print("permanente:",permanente.data_inicio)
					print("data_de_saida:",data_de_saida)
					if data_de_saida > permanente.data_inicio:
						objects.controlo_ativo = 'Saída Definitiva'
						permanente.data_fim =  data_de_saida-datetime.timedelta(days=1)
						permanente.save()
					else:
						objects.controlo_ativo = 'Ativo'
				else:
					objects.controlo_ativo = 'Saída Definitiva'
				objects.save()
				messages.success(request, f'Ficha Saída foi alterado com sucesso!')
				return redirect('DetalhoFuncionarioListaSaida',objects.id)
	else:
		form = Ficha_saida_definitivaForm(instance=objects1)
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
	]
	context = {
		'link_antes':link_antes,
		"title":"Alterar Ficha Saída",
		"legend":"Alterar Ficha Saída",
		"page":"form_saida_fun",
		"active_alterar_fsd_fun":"active",
		"objects":objects,
		"form":form,
	}
	return render(request, 'funcionario/form_tab.html', context)

@login_required
def DesabilitarFSaida(request,id,idfsd):
	objects = Funcionarios.objects.get(id=id)
	objects1 = Ficha_saida_definitiva.objects.get(id_saida=idfsd)
	objects1.controlo_estado = 'Desabilitar'
	objects1.alterado_por = request.user.username
	objects1.alterado_em = now
	objects1.save()
	# contratacao = objects.getContratacao()
	# permanente = objects.getPermanente()
	# if contratacao:
	# 	objects.controlo_ativo = 'Ativo'
	# 	objects.save()
	# if permanente:
	# 	objects.controlo_ativo = 'Ativo'
	# 	objects.save()
	messages.error(request, f'Ficha Saída Definitiva foi desabilitar com sucesso!')
	return redirect('DetalhoFuncionarioListaSaida',objects.id)


@login_required
def updatedImageFun(request, fid):
	objects = Funcionarios.objects.get(id=fid)
	link_antes = [
		{'link_name':"lista-funcionarios",'link_param':"",'link_text':f"Lista Funcionarios"},
		{'link_name':"DetailFuncionario",'link_param':f"{objects.id}",'link_text':f"Detalho Funcionario {objects.nome}"}
		]
	context = {
		'link_antes':link_antes,
		"title":"Atualizar Fotograria",
		"legend":"Atualizar Fotograria",
		"page":"detalho_fun",
		"activeDadosPessoais":"active",
		"objects":objects,
		}
	return render(request, 'funcionario/load_image_camera.html', context)

from django.views.decorators.csrf import csrf_exempt
import base64

@login_required
@csrf_exempt
def updatedImageFun1(request, fid):
	objects = Funcionarios.objects.get(id=fid)
	if request.method == 'POST':
		try:
			image_data = request.POST.get('image')
			if not image_data:
				return JsonResponse({'error': 'No image data received'}, status=400)
			print("image_data:",image_data)
			image_data = image_data.split(",")[1]  # Remove the data:image/png;base64, prefix
			image_data = base64.b64decode(image_data)
			base64_encoded_image = base64.b64encode(image_data).decode('utf-8')
			input_dados = base64_encoded_image
			imageObjects = ImagemPessoal.objects.filter(pessoa=objects).last()
			if imageObjects:
				ImagemPessoal.objects.filter(pessoa=objects).update(dados=input_dados)
			else:
				ImagemPessoal.objects.create(pessoa=objects,dados=input_dados)
			return JsonResponse({'success': True})
		except Funcionarios.DoesNotExist:
			return JsonResponse({'error': 'Funcionario not found'}, status=404)
		except Exception as e:
			return JsonResponse({'error': str(e)}, status=500)
	return JsonResponse({'error': 'Invalid request method'}, status=405)


@login_required
def BuscaFuncionario(request):
    query = request.GET.get('id_sigap_search', '').strip()
    
    if query:
        search_terms = query.split()
        filters = Q()
        for term in search_terms:
            filters &= Q(nome__icontains=term) | Q(id_sigap__icontains=term)
        
        funcionarios = ListaFuncionarioCompleto1.objects.filter(filters)[:5]
        
        results = [
            {
                'id': func.id,
                'nome': func.nome,
                'id_sigap': func.id_sigap,
                'sexo': func.sexo,
                'unidade': func.unidade,
                'tipo_funcionario': func.tipo_funcionario,
                'data_nascimento': func.data_nascimento.strftime('%Y-%m-%d') if func.data_nascimento else '',
                'dados_imajen': func.dados_imajen if func.dados_imajen else None,
            }
            for func in funcionarios
        ]
    else:
        results = []

    return JsonResponse({'results': results})
