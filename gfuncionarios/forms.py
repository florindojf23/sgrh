from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div,HTML

from django.contrib.auth.models import User,Group
from .models import *
from unidade_ministerio.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class FuncionariosForm(forms.ModelForm):
	data_nascimento = forms.DateField(label='Data de Nascimento', widget=DateInput(), required=False)
	data_emissao_eleitoral = forms.DateField(label='Data Emissao de Cartao Eleitoral', widget=DateInput(), required=False)
	data_validade_conducao = forms.DateField(label='Data validade de Carta Conducao', widget=DateInput(), required=False)
	data_validade_bi = forms.DateField(label='Data de Validade BI ', widget=DateInput(), required=False)
	sexo = forms.ChoiceField(
		choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')],
		widget=forms.Select(attrs={'class': 'my-3 form-select '})
	)
    
	class Meta:
		model = Funcionarios
		fields = ['nome','sexo','id_sigap','id_grp','data_nascimento','lugar_nascimento',
					'nu_telemovel','email','nss','nu_eleitoral','data_emissao_eleitoral',
					'nu_bi','data_validade_bi','nu_conducao','data_validade_conducao','nome_pai',
					'nome_mae','code_vendor'
				]
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nome'].required = True
		self.fields['sexo'].required = True
		self.fields['data_nascimento'].required = True
		self.fields['nu_telemovel'].required = True
		self.fields['nome_mae'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('nome', css_class='col-md-6 my-3'),
				Column('sexo', css_class='col-md-6 my-3'),
			
				Column('id_sigap', css_class='col-md-4 my-3'),
				Column('id_grp', css_class='col-md-4 my-3'),
				Column('code_vendor', css_class='col-md-4 my-3'),
			
				Column('data_nascimento', css_class='col-md-6 my-3'),
				Column('lugar_nascimento', css_class='col-md-6 my-3'),
				Column('email', css_class='col-md-4 my-3'),
				Column('nu_telemovel', css_class='col-md-4 my-3'),
				Column('nss', css_class='col-md-4 my-3'),
				Column('nu_eleitoral', css_class='col-md-6 my-3'),
				Column('data_emissao_eleitoral', css_class='col-md-6 my-3'),
				Column('nu_bi', css_class='col-md-6 my-3'),
				Column('data_validade_bi', css_class='col-md-6 my-3'),
				Column('nu_conducao', css_class='col-md-6 my-3'),
				Column('data_validade_conducao', css_class='col-md-6 my-3'),
				Column('nome_pai', css_class='col-md-6 my-3'),
				Column('nome_mae', css_class='col-md-6 my-3'),
				
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)


class FuncionariosFormReadonly(forms.ModelForm):
	data_nascimento = forms.DateField(label='Data de Nascimento', widget=DateInput(), required=False)
	data_emissao_eleitoral = forms.DateField(label='Data validade de Cartao Eleitoral', widget=DateInput(), required=False)
	data_validade_conducao = forms.DateField(label='Data validade de Carta Conducao', widget=DateInput(), required=False)
	data_validade_bi = forms.DateField(label='Data de Validade BI ', widget=DateInput(), required=False)
    
	class Meta:
		model = Funcionarios
		fields = ['nome','sexo','id_sigap','id_grp','data_nascimento','lugar_nascimento',
					'nu_telemovel','email','nss','nu_eleitoral','data_emissao_eleitoral',
					'nu_bi','data_validade_bi','nu_conducao','data_validade_conducao','nome_pai',
					'nome_mae','code_vendor'
				]
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['readonly'] = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('nome', css_class='col-md-6 my-3'),
				Column('sexo', css_class='col-md-6 my-3'),
			
				Column('id_sigap', css_class='col-md-4 my-3'),
				Column('id_grp', css_class='col-md-4 my-3'),
				Column('code_vendor', css_class='col-md-4 my-3'),
			
				Column('data_nascimento', css_class='col-md-6 my-3'),
				Column('lugar_nascimento', css_class='col-md-6 my-3'),
				Column('email', css_class='col-md-4 my-3'),
				Column('nu_telemovel', css_class='col-md-4 my-3'),
				Column('nss', css_class='col-md-4 my-3'),
				Column('nu_eleitoral', css_class='col-md-6 my-3'),
				Column('data_emissao_eleitoral', css_class='col-md-6 my-3'),
				Column('nu_bi', css_class='col-md-6 my-3'),
				Column('data_validade_bi', css_class='col-md-6 my-3'),
				Column('nu_conducao', css_class='col-md-6 my-3'),
				Column('data_validade_conducao', css_class='col-md-6 my-3'),
				Column('nome_pai', css_class='col-md-6 my-3'),
				Column('nome_mae', css_class='col-md-6 my-3'),
			
		)




class Ficha_colocacaoForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=True)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	dg = forms.ModelChoiceField(label='Direcao Geral',queryset=Direcao_geral.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	dn = forms.ModelChoiceField(label='Direcao Nacional',queryset=Direcao_nacional.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	dep = forms.ModelChoiceField(label='Departamento',queryset=Departamento.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	sec = forms.ModelChoiceField(label='Seccao',queryset=Seccao.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	local_trabalho = forms.ModelChoiceField(label='Local de trabalho',queryset=Gdivisao_administrativa_municipio.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	tipo_colocacao = forms.ModelChoiceField(label='Tipo de Colocação',queryset=Tipo_colocacao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Ficha_colocacao
		fields = ['data_inicio','data_fim','tipo_colocacao','dg','local_trabalho','dn','dep','sec']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['dg'].queryset = Direcao_geral.objects.filter(controlo_ativo='Ativo')
		self.fields['dn'].queryset = Direcao_nacional.objects.none()
		self.fields['dep'].queryset = Departamento.objects.none()
		self.fields['sec'].queryset = Seccao.objects.none()
		if self.instance.pk:
			if 'dg' in self.data:
				try:
					dg_id = self.data.get('dg')
					self.fields['dn'].queryset = Direcao_nacional.objects.filter(dg__id=dg_id).order_by('nome')
				except (ValueError, TypeError):
					pass
			elif self.instance.dg_id:
				self.fields['dn'].queryset = self.instance.dg.dn_dg.order_by('nome')

			if 'dn' in self.data:
				try:
					dn_id = self.data.get('dn')
					self.fields['dep'].queryset = Departamento.objects.filter(dn__id=dn_id).order_by('nome')
					print("dn queryset set based on ins:", self.fields['dep'].queryset)
				except (ValueError, TypeError):
					pass
			elif self.instance.dn_id:
				self.fields['dep'].queryset = self.instance.dn.dep_dn.order_by('nome')

			if 'dep' in self.data:
				try:
					dep_id = self.data.get('dep')
					if dep_id:
						self.fields['sec'].queryset = Seccao.objects.filter(dep__id=dep_id).order_by('nome')
				except (ValueError, TypeError):
					pass
			elif self.instance.dep:
				print("tamtattajtrljtlajl_dg:",self.instance.dg)
				self.fields['sec'].queryset = self.instance.dep.sec_dep.order_by('nome')

		self.fields['data_inicio'].required = True
		self.fields['dg'].required = False
		self.fields['dn'].required = True
		self.fields['dep'].required = False
		self.fields['sec'].required = False
		self.fields['local_trabalho'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				# Column('instituicao', css_class='col-md-4 my-3'),
				Column('tipo_colocacao', css_class='col-md-4 my-3'),
				Column('dg', css_class='col-md-4 my-3'),
				Column('dn', css_class='col-md-6 my-3'),
				Column('dep', css_class='col-md-4 my-3'),
				Column('sec', css_class='col-md-4 my-3'),
				Column('local_trabalho', css_class='col-md-6 my-3'),
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
				<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'> <i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

