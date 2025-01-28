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
def DashboardColocacao(request):
	# permanente = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Permanente').count()
	# aap = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Agente Administração Pública').count()
	# nulo = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Não tem ficha Função').count()
	# casuais = ListaFuncionarioCompleto1.objects.filter(tipo_funcionario='Casuais').count()
	context = {
		"title":f"Dashboard Gestão Função",
		"legend":f"Dashboard Gestão Função",
		# 'permanente':permanente,'aap':aap,'nulo':nulo,'casuais':casuais,
		"page":'dashboard-colocacao',
	}
	return render(request, 'colocacao/dash.html', context)