from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gutilizador.models import *
from gdivisao_administrativa.models import *
from unidade_ministerio.models import *
from gutilizador.decorators import allowed_users

@login_required
def index(request):
	context = {
		"title":"HOME",
		"legend":"HOME",
	}
	return render(request, 'main/index.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			AuditLogin.objects.create(user=request.user)
			return redirect('home')
		else:
			messages.error(request,'Username ou Password la loos! Favor Prense fali!')
	context = {
		"title":"Pajina Login",
	}
	return render(request,'auth/login.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

from .forms import CoreForm
from .models import Core

@login_required
@allowed_users(allowed_roles=['admin'])
def Configuracaosystema(request):
	objects = Core.objects.filter(is_active=True).last()
	if request.method == "POST":
		p_form = CoreForm(request.POST,request.FILES,instance=objects)
		print("Tama1")
		if p_form.is_valid():
			print("Tama")
			instance = p_form.save(commit=False)
			instance.is_active = True
			instance.save()
			messages.success(request, f'A sua Configuracao atualizado com sucesso!')
			return redirect('configuracao-sistema')
		else:
			print("Form errors:", p_form.errors)

	else:
		p_form = CoreForm(instance=objects)
	context = {
		"title":"Pajina Configuracao de Sistema",
		"p_form":p_form,
	}
	return render(request,'syssettings/index.html',context)


@login_required
def load_posts(request):
	mun_id = request.GET.get('municipality')
	if mun_id:
		posts = Gdivisao_administrativa_posto.objects.filter(municipio_id=mun_id).order_by('posto')
	else:
		posts = []

	return render(request, 'ajax/ajax_load_divisao_administrativa.html', {'posts': posts,'page':'load_posto'})

@login_required
def load_villages(request):
	post_id = request.GET.get('post')
	if post_id:
		villages = Gdivisao_administrativa_suco.objects.filter(posto_id=post_id).order_by('suco')
	else:
		villages = []
	print("villages:",villages)
	return render(request, 'ajax/ajax_load_divisao_administrativa.html', {'villages': villages,'page':'load_suco'})

@login_required
def load_aldeias(request):
	id = request.GET.get('suco')
	if id:
		aldeias = Gdivisao_administrativa_aldeia.objects.filter(suco=id).order_by('aldeia')
	else:
		aldeias = []
	return render(request, 'ajax/ajax_load_divisao_administrativa.html', {'aldeias': aldeias,'page':'load_aldeias'})

@login_required
def load_dir_nac(request):
	id = request.GET.get('dg')
	if id:
		dir_nac = Direcao_nacional.objects.filter(dg=id).order_by('nome')
	else:
		dir_nac = []
	return render(request, 'ajax/ajax_load_divisao_administrativa.html', {'dir_nac': dir_nac,'page':'load_dir_nac'})

@login_required
def load_escola_dg(request):
	id = request.GET.get('dg')
	if id:
		escola = Escola.objects.filter(dg=id).order_by('nome')
	else:
		escola = []
	return render(request, 'ajax/ajax_load_divisao_administrativa.html', {'escola': escola,'page':'load_escola_dg'})


@login_required
def load_dir_geral(request):
	id = request.GET.get('id')
	if id:
		dir_geral = Direcao_geral.objects.filter(instituicao=id).values('id', 'nome')
		dir_nac = Direcao_nacional.objects.filter(instituicao=id).values('id', 'nome')
	else:
		dir_nac = []
		dir_geral = []
	# return render(request, 'ajax/ajax_load_divisao_administrativa.html', 
		# {
		# 'dir_nac': dir_nac,
		# 'dir_geral': dir_geral,
		# 'page':'load_dir_geral'
		# })
	return JsonResponse({
		'dir_geral': list(dir_geral),
		'dir_nac': list(dir_nac),
		})



@login_required
def load_departamento(request):
	id = request.GET.get('id')
	if id:
		departamento = Departamento.objects.filter(dn=id).order_by('nome')
	else:
		departamento = []
	return render(request, 'ajax/ajax_load_divisao_administrativa.html', {'departamento': departamento,'page':'load_dep'})

@login_required
def load_seccao(request):
	id = request.GET.get('id')
	if id:
		seccao = Seccao.objects.filter(dep=id).order_by('nome')
	else:
		seccao = []
	return render(request, 'ajax/ajax_load_divisao_administrativa.html', {'seccao': seccao,'page':'load_sec'})