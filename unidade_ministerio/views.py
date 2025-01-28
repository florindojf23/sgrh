from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gutilizador.models import *
from .models import *
from gfuncionarios.models import *
from django.db import transaction
import datetime
from django.db.models import Count, Q
from django.utils import timezone
now = timezone.now()
from .forms import *

@login_required
def DashboardEstruturaOrganica(request):
	objects = Instituicao.objects.filter(controlo_ativo='Ativo',data_fim__isnull=True).all().last()
	# instituicao_report = Instituicao.objects.annotate(total_direcoes_gerais=Count('direcao_geral', filter=Q(direcao_geral__data_fim__isnull=True) | Q(direcao_geral__data_fim__gt=now), Q(direcao_geral__controlo_ativo='Ativo')))
	instituicao_report = InstituicaoReport.objects.all()
	print("instituicao_report:",instituicao_report)
	context = {
		"title":f"Dashboard Estrutura Organica",
		"legend":f"Dashboard Estrutura Organica",
		"objects":objects,
		"instituicao_report":instituicao_report,
		"page":'dashboard_report',
		"active_organica":'active',
	}
	return render(request, 'unidade_ministerio/index.html', context)


@login_required
def ListaDirecaoGeraisNacionais(request):
	objects = Direcao_geral.objects.filter(controlo_ativo='Ativo',data_fim__isnull=True).all()
	objects1 = Direcao_nacional.objects.filter(controlo_ativo='Ativo',data_fim__isnull=True).all()
	# instituicao_report = Instituicao.objects.annotate(total_direcoes_gerais=Count('direcao_geral', filter=Q(direcao_geral__data_fim__isnull=True) | Q(direcao_geral__data_fim__gt=now), Q(direcao_geral__controlo_ativo='Ativo')))
	# instituicao_report = InstituicaoReport.objects.all()
	# print("instituicao_report:",instituicao_report)
	context = {
		"title":f"Dados Direcao Geral e Nacional",
		"legend":f"Dados Direcao Geral e Nacional",
		"objects":objects,
		"objects1":objects1,
		# "instituicao_report":instituicao_report,
		"page":'lista_dir_gerais_nac',
		"active_dir_gerais_nac":'active',
	}
	return render(request, 'unidade_ministerio/lista_dir_geral_nacional.html', context)

@login_required
def ListaDepartamentoSeccoes(request):
	objects = Departamento.objects.filter(controlo_ativo='Ativo',data_fim__isnull=True).all()
	objects1 = Seccao.objects.filter(controlo_ativo='Ativo',data_fim__isnull=True).all()
	# instituicao_report = Instituicao.objects.annotate(total_direcoes_gerais=Count('direcao_geral', filter=Q(direcao_geral__data_fim__isnull=True) | Q(direcao_geral__data_fim__gt=now), Q(direcao_geral__controlo_ativo='Ativo')))
	# instituicao_report = InstituicaoReport.objects.all()
	# print("instituicao_report:",instituicao_report)
	context = {
		"title":f"Dados Departamento e Seccao",
		"legend":f"Dados Departamento e Seccao",
		"objects":objects,
		"objects1":objects1,
		# "instituicao_report":instituicao_report,
		"page":'lista_dep_sec',
		"active_dep_sec":'active',
	}
	return render(request, 'unidade_ministerio/lista_dep_sec.html', context)

@login_required
def RegistaNovoDG(request):
	if request.method == "POST":
		form = Direcao_geralForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.inserido_por = request.user
				instance.controlo_ativo = "Ativo"
				instance.save()
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				messages.success(request, f'O novo dados Direcao Geral foi inserido com sucesso!')
				return redirect('ListaDirecaoGeraisNacionais')
	else:
		form = Direcao_geralForm()
	context = {
		'link_antes': [{'link_name':"ListaDirecaoGeraisNacionais",'link_text':"Dados Direcao Geral e Nacional"}],
		"title":"Registo Novo Direcao Geral",
		"legend":"Registo Novo Direcao Geral",
		"page":'form_dg',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)

@login_required
def UpdateDirGeral(request,id):
	objects = get_object_or_404(Direcao_geral,id=id)
	if request.method == "POST":
		form = Direcao_geralForm(request.POST, request.FILES,instance=objects)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				messages.success(request, f'O dados Direcao Geral foi alterado com sucesso!')
				return redirect('ListaDirecaoGeraisNacionais')
	else:
		form = Direcao_geralForm(instance=objects)
	context = {
		'link_antes': [{'link_name':"ListaDirecaoGeraisNacionais",'link_text':"Dados Direcao Geral e Nacional"}],
		"title":"Alterar Direcao Geral",
		"legend":"Alterar Direcao Geral",
		"page":'form_dg',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)

@login_required
def RegistaNovoFuncionarioDN(request):
	if request.method == "POST":
		form = Direcao_nacionalForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.inserido_por = request.user
				instance.controlo_ativo = "Ativo"
				instance.save()
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				messages.success(request, f'O novo dados Direcao Nacional foi inserido com sucesso!')
				return redirect('ListaDirecaoGeraisNacionais')
	else:
		form = Direcao_nacionalForm()
	context = {
		'link_antes': [{'link_name':"ListaDirecaoGeraisNacionais",'link_text':"Dados Direcao Geral e Nacional"}],
		"title":"Registo Novo Direcao Nacional",
		"legend":"Registo Novo Direcao Nacional",
		"page":'form_dn',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)

@login_required
def UpdateDirNacional(request,id):
	objects = get_object_or_404(Direcao_nacional,id=id)
	if request.method == "POST":
		form = Direcao_nacionalForm(request.POST, request.FILES,instance=objects)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				messages.success(request, f'O dados Direcao Nacional foi alterado com sucesso!')
				return redirect('ListaDirecaoGeraisNacionais')
	else:
		form = Direcao_nacionalForm(instance=objects)
	context = {
		'link_antes': [{'link_name':"ListaDirecaoGeraisNacionais",'link_text':"Dados Direcao Geral e Nacional"}],
		"title":"Alterar Direcao Nacional",
		"legend":"Alterar Direcao Nacional",
		"page":'form_dn',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)

@login_required
def RegistaNovoDepartamento(request):
	if request.method == "POST":
		form = DepartamentoForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.inserido_por = request.user
				instance.controlo_ativo = "Ativo"
				instance.save()
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				messages.success(request, f'O novo dados Departamento foi inserido com sucesso!')
				return redirect('ListaDepartamentoSeccoes')
	else:
		form = DepartamentoForm()
	context = {
		'link_antes': [{'link_name':"ListaDepartamentoSeccoes",'link_text':"Dados Departamento e Seccao"}],
		"title":"Registo Novo Departamento",
		"legend":"Registo Novo Departamento",
		"page":'form_dep',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)

@login_required
def UpdateDepartamento(request,id):
	objects = get_object_or_404(Departamento,id=id)
	if request.method == "POST":
		form = DepartamentoForm(request.POST, request.FILES,instance=objects)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				messages.success(request, f'O dados Departamento foi alterado com sucesso!')
				return redirect('ListaDepartamentoSeccoes')
	else:
		form = DepartamentoForm(instance=objects)
	context = {
		'link_antes': [{'link_name':"ListaDepartamentoSeccoes",'link_text':"Dados Departamento e Seccao"}],
		"title":"Alterar Novo Departamento",
		"legend":"Alterar Novo Departamento",
		"page":'form_dep_update',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)

@login_required
def RegistaNovoSeccao(request):
	if request.method == "POST":
		form = SeccaoForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.inserido_por = request.user
				instance.controlo_ativo = "Ativo"
				instance.save()
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				messages.success(request, f'O novo dados Seccao foi inserido com sucesso!')
				return redirect('ListaDepartamentoSeccoes')
	else:
		form = SeccaoForm()
	context = {
		'link_antes': [{'link_name':"ListaDepartamentoSeccoes",'link_text':"Dados Departamento e Seccao"}],
		"title":"Registo Novo Seccao",
		"legend":"Registo Novo Seccao",
		"page":'form_sec',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)

@login_required
def UpdateSeccao(request,id):
	objects = get_object_or_404(Seccao,id=id)
	if request.method == "POST":
		form = SeccaoForm(request.POST, request.FILES,instance=objects)
		if form.is_valid():
			with transaction.atomic():
				instance = form.save(commit=False)
				instance.alterado_por = request.user.username
				instance.alterado_em = now
				instance.save()
				# ImagemPessoal.objects.create(pessoa=instance,dados=input_dados)
				messages.success(request, f'O dados Seccao foi alterado com sucesso!')
				return redirect('ListaDepartamentoSeccoes')
	else:
		form = SeccaoForm(instance=objects)
	context = {
		'link_antes': [{'link_name':"ListaDepartamentoSeccoes",'link_text':"Dados Departamento e Seccao"}],
		"title":"Alterar Novo Seccao",
		"legend":"Alterar Novo Seccao",
		"page":'form_sec_update',
		"form":form,
	}
	return render(request, 'unidade_ministerio/form.html', context)


from django.http import JsonResponse

@login_required
def get_data(request):
    data_type = request.GET.get('type')
    
    # Example data fetching logic based on data_type
    if data_type == 'direcao_geral':
        # data = list(Direcao_geral.objects.values('nome', 'id','Totalfuncionario'))
        dados = Direcao_geral.objects.filter()
        data = list()
        for x in dados:
        	col = Ficha_colocacao.objects.filter(dg=x).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colm = Ficha_colocacao.objects.filter(dg=x,funcionario__sexo='Masculino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colf = Ficha_colocacao.objects.filter(dg=x,funcionario__sexo='Feminino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	data.append({'id':x.id,'nome':x.nome,'totalfun':col,'totalfunm':colm,'totalfunf':colf})
    elif data_type == 'direcao_nacional':
        dados = Direcao_nacional.objects.filter()
        data = list()
        for x in dados:
        	col = Ficha_colocacao.objects.filter(dn=x).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colm = Ficha_colocacao.objects.filter(dn=x,funcionario__sexo='Masculino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colf = Ficha_colocacao.objects.filter(dn=x,funcionario__sexo='Feminino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	data.append({'id':x.id,'nome':x.nome,'totalfun':col,'totalfunm':colm,'totalfunf':colf})
    elif data_type == 'departamento':
        dados = Departamento.objects.filter()
        data = list()
        for x in dados:
        	col = Ficha_colocacao.objects.filter(dep=x).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colm = Ficha_colocacao.objects.filter(dep=x,funcionario__sexo='Masculino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colf = Ficha_colocacao.objects.filter(dep=x,funcionario__sexo='Feminino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	data.append({'id':x.id,'nome':x.nome,'totalfun':col,'totalfunm':colm,'totalfunf':colf})
    elif data_type == 'seccao':
        dados = Seccao.objects.filter()
        data = list()
        for x in dados:
        	col = Ficha_colocacao.objects.filter(sec=x).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colm = Ficha_colocacao.objects.filter(sec=x,funcionario__sexo='Masculino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colf = Ficha_colocacao.objects.filter(sec=x,funcionario__sexo='Feminino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	data.append({'id':x.id,'nome':x.nome,'totalfun':col,'totalfunm':colm,'totalfunf':colf})
    elif data_type == 'escola':
        dados = Escola.objects.filter()
        data = list()
        for x in dados:
        	col = Ficha_colocacao.objects.filter(escola=x).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colm = Ficha_colocacao.objects.filter(escola=x,funcionario__sexo='Masculino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	colf = Ficha_colocacao.objects.filter(escola=x,funcionario__sexo='Feminino').filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).count()
        	data.append({'id':x.id,'nome':x.nome,'totalfun':col,'totalfunm':colm,'totalfunf':colf})
    else:
        data = []

    return JsonResponse(data, safe=False)


@login_required
def load_lista_funcionario_dashboard_organica(request):
    id = request.GET.get('id')
    tipo = request.GET.get('tipo')
    coluna = request.GET.get('coluna')
    if coluna == 'direcao_geral':
    	getData = get_object_or_404(Direcao_geral,id=id)
    	if tipo:
    		objects = Ficha_colocacao.objects.filter(dg__id=id,funcionario__sexo=tipo).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	else:
    		objects = Ficha_colocacao.objects.filter(dg__id=id).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	page = 'lista_dg'

    if coluna == 'direcao_nacional':
    	getData = get_object_or_404(Direcao_nacional,id=id)
    	if tipo:
    		objects = Ficha_colocacao.objects.filter(dn__id=id,funcionario__sexo=tipo).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	else:
    		objects = Ficha_colocacao.objects.filter(dn__id=id).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	page = 'lista_dn'
    if coluna == 'departamento':
    	getData = get_object_or_404(Departamento,id=id)
    	if tipo:
    		objects = Ficha_colocacao.objects.filter(dep__id=id,funcionario__sexo=tipo).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	else:
    		objects = Ficha_colocacao.objects.filter(dep__id=id).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	page = 'lista_dep'
    if coluna == 'seccao':
    	getData = get_object_or_404(Seccao,id=id)
    	if tipo:
    		objects = Ficha_colocacao.objects.filter(sec__id=id,funcionario__sexo=tipo).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	else:
    		objects = Ficha_colocacao.objects.filter(sec__id=id).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	page = 'lista_sec'
    if coluna == 'escola':
    	getData = get_object_or_404(Escola,id=id)
    	if tipo:
    		objects = Ficha_colocacao.objects.filter(escola__id=id,funcionario__sexo=tipo).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	else:
    		objects = Ficha_colocacao.objects.filter(escola__id=id).filter(Q(data_fim__isnull=True) | Q(data_fim__gte=now)).filter(controlo_estado__isnull=True).order_by('funcionario__nome')
    	page = 'lista_escola'
    return render(request, 'unidade_ministerio/ajax_load_lista_funcionario.html', {'getData': getData,'objects': objects,'page':page})

	

