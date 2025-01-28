
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div,HTML

from django.contrib.auth.models import User,Group
from .models import *
from unidade_ministerio.models import *
from master.models import Pais
from gfuncionarios.models import Funcionarios


class DateInput(forms.DateInput):
	input_type = 'date'



class Habilitacao_academicaForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data de Inicio do Curso', widget=DateInput(), required=False)
	data_habilitacao = forms.DateField(label='Data de Habilitação', widget=DateInput(), required=False)
	nivel_habilitacao = forms.ModelChoiceField(label='Nivel de Habilitação',queryset=Nivel_habilitacao.objects.exclude(controlo_estado='Desabilitar'),widget=forms.Select(attrs={'class': 'form-select '}))
	entidade = forms.ModelChoiceField(label='Entidade',queryset=Entidade_habilitacao.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
	curso = forms.ModelChoiceField(label='Curso',queryset=Curso_habilitacao.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Habilitacao_academica
		fields = ['nivel_habilitacao','curso','entidade','data_inicio','data_habilitacao']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nivel_habilitacao'].required = True
		self.fields['curso'].required = True
		self.fields['entidade'].required = True
		self.fields['data_inicio'].required = True
		self.fields['data_habilitacao'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('nivel_habilitacao', css_class='col-md-4 my-3'),
				Column('data_inicio', css_class='col-md-4 my-3'),
				Column('data_habilitacao', css_class='col-md-4 my-3'),
			
				Column('curso', css_class='col-md-4 my-3'),
				Column('entidade', css_class='col-md-4 my-3'),
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Habilitacao_academicaFunForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data de Inicio do Curso', widget=DateInput(), required=False)
	data_habilitacao = forms.DateField(label='Data de Habilitação', widget=DateInput(), required=False)
	nivel_habilitacao = forms.ModelChoiceField(label='Nivel de Habilitação',queryset=Nivel_habilitacao.objects.exclude(controlo_estado='Desabilitar'),widget=forms.Select(attrs={'class': 'form-select '}))
	entidade = forms.ModelChoiceField(label='Entidade',queryset=Entidade_habilitacao.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
	curso = forms.ModelChoiceField(label='Curso',queryset=Curso_habilitacao.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
	funcionario = forms.ModelChoiceField(label='Seleciona Funcionario',queryset=Funcionarios.objects.exclude(controlo_ativo='Desabilitar')[:10],widget=forms.Select(attrs={'class': 'form-select select2'}))
    
	class Meta:
		model = Habilitacao_academica
		fields = ['funcionario','nivel_habilitacao','curso','entidade','data_inicio','data_habilitacao']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nivel_habilitacao'].required = True
		self.fields['funcionario'].required = True
		self.fields['curso'].required = True
		self.fields['entidade'].required = True
		self.fields['data_inicio'].required = True
		self.fields['data_habilitacao'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('funcionario', css_class='col-md-6 my-3'),
				Column('nivel_habilitacao', css_class='col-md-4 my-3'),
				Column('data_inicio', css_class='col-md-4 my-3'),
				Column('data_habilitacao', css_class='col-md-4 my-3'),
			
				Column('curso', css_class='col-md-4 my-3'),
				Column('entidade', css_class='col-md-4 my-3'),
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Nivel_habilitacaoForm(forms.ModelForm):
	# data_inicio = forms.DateField(label='Data de Inicio do Curso', widget=DateInput(), required=False)
	# data_habilitacao = forms.DateField(label='Data de Habilitação', widget=DateInput(), required=False)
	# nivel_habilitacao = forms.ModelChoiceField(label='Nivel de Habilitação',queryset=Nivel_habilitacao.objects.exclude(controlo_estado='Desabilitar'),widget=forms.Select(attrs={'class': 'form-select '}))
	# entidade = forms.ModelChoiceField(label='Entidade',queryset=Entidade_habilitacao.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
	# curso = forms.ModelChoiceField(label='Curso',queryset=Curso_habilitacao.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Nivel_habilitacao
		fields = ['nivel_habilitacao','ordem','pontos_promocao_rg']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nivel_habilitacao'].required = True
		self.fields['ordem'].required = True
		self.fields['pontos_promocao_rg'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('nivel_habilitacao', css_class='col-md-7 my-3'),
				Column('pontos_promocao_rg', css_class='col-md-6 my-3'),
				Column('ordem', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Entidade_habilitacaoForm(forms.ModelForm):
	# data_inicio = forms.DateField(label='Data de Inicio do Curso', widget=DateInput(), required=False)
	# data_habilitacao = forms.DateField(label='Data de Habilitação', widget=DateInput(), required=False)
	# nivel_habilitacao = forms.ModelChoiceField(label='Nivel de Habilitação',queryset=Nivel_habilitacao.objects.exclude(controlo_estado='Desabilitar'),widget=forms.Select(attrs={'class': 'form-select '}))
	# entidade = forms.ModelChoiceField(label='Entidade',queryset=Entidade_habilitacao.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
	pais = forms.ModelChoiceField(label='Pais',queryset=Pais.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Entidade_habilitacao
		fields = ['entidade','tipo_entidade','pais']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['entidade'].required = True
		self.fields['tipo_entidade'].required = True
		self.fields['pais'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('entidade', css_class='col-md-7 my-3'),
				Column('tipo_entidade', css_class='col-md-6 my-3'),
				Column('pais', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Curso_habilitacaoForm(forms.ModelForm):
	# pais = forms.ModelChoiceField(label='Pais',queryset=Pais.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Curso_habilitacao
		fields = ['nome_curso','sigla']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nome_curso'].required = True
		self.fields['sigla'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('nome_curso', css_class='col-md-7 my-3'),
				Column('sigla', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)