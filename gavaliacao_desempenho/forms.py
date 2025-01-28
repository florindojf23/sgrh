
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div,HTML

from django.contrib.auth.models import User,Group
from .models import *
from unidade_ministerio.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class Gad_ficha_avaliacao_desempenhoForm(forms.ModelForm):
	data_ad = forms.DateField(label='Data de Avaliação', widget=DateInput(), required=False)
	tipo_ad = forms.ModelChoiceField(label='Tipo de Avaliação',queryset=Gad_tipo_ad.objects.exclude(controlo_estado='Desabilitar'),widget=forms.Select(attrs={'class': 'form-select '}))
	ano_ad = forms.ModelChoiceField(label='Ano de Avaliação',queryset=Anos_AD.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Gad_ficha_avaliacao_desempenho
		fields = ['tipo_ad','ano_ad','quantitativa','qualitativa','data_ad','avaliador']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['tipo_ad'].required = True
		self.fields['ano_ad'].required = True
		self.fields['qualitativa'].required = True
		self.fields['quantitativa'].required = True
		self.fields['avaliador'].required = True
		self.fields['data_ad'].required = False
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('tipo_ad', css_class='col-md-4 my-3'),
				Column('ano_ad', css_class='col-md-4 my-3'),
				Column('data_ad', css_class='col-md-4 my-3'),
			
				Column('quantitativa', css_class='col-md-4 my-3'),
				Column('qualitativa', css_class='col-md-4 my-3'),
				Column('avaliador', css_class='col-md-4 my-3'),
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Anos_ADForm(forms.ModelForm):
	class Meta:
		model = Anos_AD
		fields = ['anos_de_avaliacao']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['anos_de_avaliacao'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('anos_de_avaliacao', css_class='col-md-4 my-3'),
			
			HTML(""" <br><div class='card-footer d-flex justify-content-begin py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

