from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return render(request, 'auth/500.html')
		return wrapper_func
	return decorator

def allowed_users1(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if request.user.groups.exists():
				user_groups = request.user.groups.values_list('name', flat=True)
				if any(group in allowed_roles for group in user_groups):
					return view_func(request, *args, **kwargs)
				else:
					return render(request, 'auth/500.html') 
			else:
				return render(request, 'auth/500.html') 
		return wrapper_func
	return decorator