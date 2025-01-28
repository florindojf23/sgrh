from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gutilizador.decorators import allowed_users
from django.contrib.auth.models import User, Group
from django.db.models import Count
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from gutilizador.models import Profile,AuditLogin,Funcionario_user
from gutilizador.forms import ProfileUpdateForm,UserForm
from django.contrib.auth.hashers import check_password
from gdivisao_administrativa.models import *
from gfuncionarios.models import Funcionarios

@login_required
@allowed_users(allowed_roles=['admin'])
def controlo_gestoes(request):
	group = request.user.groups.all()[0].name
	objects = []
	objects1 = User.objects.all()
	total_users = User.objects.all().count()
	allGroup = Group.objects.all().exclude(name='admin')
	grouplist = Group.objects.annotate(user_count=Count('user')).order_by('name')
	allMunicipio = Gdivisao_administrativa_municipio.objects.exclude(municipio='Fora de Timor') 
	lista_funcionario_ativos = Funcionarios.objects.filter(controlo_ativo = 'Ativo')
	# for x in objects1:
	# 	stored_password = x.password
	# 	is_valid_match = check_password('password', stored_password)
	# 	if is_valid_match:
	# 		objects.append([x,"password"])
	# 	else:
	# 		objects.append([x,"alteradu"])
	context = {
		'group': group,'lista_funcionario_ativos': lista_funcionario_ativos,'allGroup': allGroup,'allMunicipio': allMunicipio, 'objects': objects1,'grouplist': grouplist,
		'active_userlist': 'active','title': 'Lista Gestão', 'legend': 'Lista Gestão','total_users':total_users,
	}
	return render(request, 'controlo_gestoes/list.html', context)
