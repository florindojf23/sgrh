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

# Create your views here.
@login_required
def ProfileUpdate(request):
	profile = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		p_form = ProfileUpdateForm(request.POST, instance=profile)
		if p_form.is_valid():
			print("tama")
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('user-profile')
	else:
		p_form = ProfileUpdateForm(instance=profile)

	context = {
		'profile': profile, 'p_form': p_form,
		'title': 'Perfil','active_profile': 'active', 'legend': 'Perfil',
	}
	return render(request, 'account/profile.html', context)

@login_required
def ProfileImageUpdate(request):
	if request.method == 'POST' or request.method == 'FILES':
		updatedImage = request.FILES.get('updatedImage')
		id = request.POST.get('id')
		if updatedImage:
			valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
			file_extension = updatedImage.name.split('.')[-1].lower()
			if file_extension not in valid_extensions:
				messages.error(request, 'Imajem tenki iha formatu JPG, PNG, ka GIF deit.')
				return redirect('user-profile')
			objects = Profile.objects.get(user=request.user)
			objects.image = updatedImage
			objects.save()
			messages.success(request, f'Dadus Imajen Atualiza ho Susesu!')
			return redirect('user-profile')
	return render(request, 'account/profile.html')


@login_required
def AccountUpdate(request):
	group = request.user.groups.all()[0].name
	profile = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		u_form = UserForm(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Ita boot nia konta altera ona!')
			return redirect('user-account')
	else:
		u_form = UserForm(instance=request.user)
	context = {
		'u_form': u_form,'profile': profile,
		'title': 'Info Konta','active_account': 'active', 'legend': 'Info Konta',
	}
	return render(request, 'account/account_settings.html', context)

class UserPasswordChangeView(PasswordChangeView):
	template_name = 'account/change_password.html'
	success_url = reverse_lazy('user-change-password-done')
	def get_success_url(self):
		messages.success(self.request, 'Password was successfully changed.')
		return super().get_success_url()
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profile'] = Profile.objects.get(user=self.request.user)
		context['active_password'] = 'active'
		return context

class UserPasswordChangeDoneView(PasswordResetDoneView):
	template_name = 'account/change_password_done.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['profile'] = Profile.objects.get(user=self.request.user)
		context['active_password'] = 'active'
		context['title'] = 'Password Change Done'
		return context

@login_required
def AccountLoginHistory(request):
	group = request.user.groups.all()[0].name
	objects = AuditLogin.objects.filter(user=request.user)
	profile = Profile.objects.get(user=request.user)
	context = {
		'group': group, 'objects': objects,'profile': profile,
		'active_loginhistory': 'active','title': 'Historia Login', 'legend': 'Historia Login'
	}
	return render(request, 'account/login_history.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def ativuUser(request,id):
	userData = get_object_or_404(User,id=id)
	userData.is_active = True
	userData.save()
	messages.success(request, f'User {userData.username} Ativu ho Susesu!')
	return redirect('userlist')

@login_required
@allowed_users(allowed_roles=['admin'])
def desativuUser(request,id):
	userData = get_object_or_404(User,id=id)
	userData.is_active = False
	userData.save()
	messages.success(request, f'User {userData.username} Desativu ho Susesu!')
	return redirect('userlist')


@login_required
@allowed_users(allowed_roles=['admin'])
def resetUserPassword(request,id):
	userData = get_object_or_404(User,id=id)
	password = make_password('password')
	userData.password = password
	userData.save()
	messages.success(request, f'Password ba {userData.username} Reset ho Susesu!')
	return redirect('userlist')

from django.contrib.auth.hashers import check_password
from gdivisao_administrativa.models import *
from gfuncionarios.models import Funcionarios
@login_required
@allowed_users(allowed_roles=['admin'])
def UserList(request):
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
		'active_userlist': 'active','title': 'Lista Utilizador', 'legend': 'Lista Utilizador','total_users':total_users,
	}
	return render(request, 'users/userlist.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def user_with_group(request,id):
	group = request.user.groups.all()[0].name
	groupData = get_object_or_404(Group,id=id)
	objects = []
	total_users = User.objects.all().count()
	objects1 = User.objects.filter(groups=groupData)
	allGroup = Group.objects.all().exclude(name='admin')
	grouplist = Group.objects.annotate(user_count=Count('user')).order_by('name')
	# for x in objects1:
	# 	stored_password = x.password
	# 	is_valid_match = check_password('password', stored_password)
	# 	if is_valid_match:
	# 		objects.append([x,"password"])
	# 	else:
	# 		objects.append([x,"alteradu"])

	
	context = {
		'group': group,'allGroup': allGroup, 'objects': objects1,'grouplist': grouplist,
		'accountListActive': 'active','title': 'Lista Utilizador', 'legend': 'Lista Utilizador','total_users':total_users,
	}
	return render(request, 'users/userlist.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def createUser(request):
	group = request.user.groups.all()[0].name
	objects = User.objects.all()
	allGroup = Group.objects.all().exclude(name='admin')
	grouplist = Group.objects.annotate(user_count=Count('user')).order_by('name')
	if request.method == 'POST':
		userGoup = request.POST.get("user_group")
		username = request.POST.get("username")
		apelido = request.POST.get("apelido")
		dob = request.POST.get("dob")
		password = make_password('password')
		username = split_string(username) + split_string(apelido)
		obj2 = User(username=username, password=password,is_active=False)
		obj2.save()
		group_user = Group.objects.get(id=str(userGoup))
		user = User.objects.get(id=obj2.id)
		user.groups.add(group_user)
		messages.success(request, f'Dadus Utilizador Rejistu ho Susesu!')
		return redirect('userlist')
	context = {
		'group': group,'allGroup': allGroup, 'objects': objects,'grouplist': grouplist,
		'accountListActive': 'active','title': 'Lista Utilizador', 'legend': 'Lista Utilizador'
	}
	return render(request, 'users/userlist.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def createUserFuncionario(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		userGoup = request.POST.get("user_group")
		id_funcionario = request.POST.get("funcionario_id")
		if id_funcionario:
			dataF = get_object_or_404(Funcionarios,id=id_funcionario)
		else:
			messages.warning(request, f'Por Favor escolha o Funcionario!')
			return redirect('userlist')
		dataUser = User.objects.filter(username=dataF.id_sigap,is_active=True).last()
		if dataUser:
			messages.success(request, f'Ja existe o Usuario com ID {dataF.id_sigap}!')
			return redirect('userlist')
		else:	
			username = dataF.id_sigap
			password = make_password('password')
			obj2 = User(username=username, password=password,is_active=False)
			obj2.save()
			group_user = Group.objects.get(id=str(userGoup))
			user = User.objects.get(id=obj2.id)
			Funcionario_user.objects.create(user=user,funcionario=dataF)
			user.groups.add(group_user)
			messages.success(request, f'Dadus Utilizador ao Funcionario {dataF.nome} ({dataF.id_sigap}) foi rejistado com Sucesso!')
			return redirect('userlist')
	context = {
		'group': group,'allGroup': allGroup, 'objects': objects,'grouplist': grouplist,
		'accountListActive': 'active','title': 'Lista Utilizador', 'legend': 'Lista Utilizador'
	}
	return render(request, 'users/userlist.html', context)

from django.http import JsonResponse
def search_funcionario(request):
	query = request.GET.get('q', '')
	if query:
		funcionarios = Funcionarios.objects.filter(nome__icontains=query)[:10]
		results = [{'id': f.id, 'nome': f.nome, 'id_sigap': f.id_sigap} for f in funcionarios]
		return JsonResponse(results, safe=False)
	return JsonResponse([], safe=False)
