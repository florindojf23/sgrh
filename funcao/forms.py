from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div,HTML

from django.contrib.auth.models import User,Group
from .models import *

class DateInput(forms.DateInput):
	input_type = 'date'


class Ficha_contratacaoForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=False)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	tipo_alteracao_ficha = forms.ModelChoiceField(label='Tipo de Alteração de Ficha',queryset=Tipo_alteracao_ficha.objects.filter(tipo_alteracao_ficha = 'Contratação'),widget=forms.Select(attrs={'class': 'form-select ', 'id': 'tipo-alteracao-ficha-select'}))
	uuid_list = ['693b72aa-ddaf-48ae-84af-408a7b86a435', '9bafa3d0-8f3b-496a-a3c2-1aa9786b7a5a']
	relacao_juridica_emprego = forms.ModelChoiceField(label='Relação Juridica de Emprego',queryset=Relacao_juridica_emprego.objects.filter(id_rje__in = uuid_list),widget=forms.Select(attrs={'class': 'form-select '}))
	regime = forms.ModelChoiceField(label='Regime',queryset=Gcarreira_regime.objects.all(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'regime-select'}))
	categoria = forms.ModelChoiceField(label='Categoria',queryset=Gcarreira_categoria.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'categoria-select'}))
	escalao = forms.ModelChoiceField(label='Escalão',queryset=Gcarreira_escalao.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'escalao-select'}))
	indice = forms.ModelChoiceField(label='Índice',queryset=Gcarreira_indice.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'indice-select'}))
    
	class Meta:
		model = Ficha_contratacao
		fields = ['data_inicio','data_fim','regime','categoria','escalao','indice','tipo_alteracao_ficha','relacao_juridica_emprego',
				]
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if self.instance.pk:

			if 'regime' in self.data:
				try:
					regime_id = self.data.get('regime')
					self.fields['categoria'].queryset = Gcarreira_categoria.objects.filter(regime_id=regime_id)
				except (ValueError, TypeError):
					pass  # Invalid input; keep empty queryset
			elif self.instance.regime:
				self.fields['categoria'].queryset = self.instance.regime.cat_regime.order_by('categoria')

			if 'categoria' in self.data:
				try:
					categoria_id = self.data.get('categoria')
					self.fields['escalao'].queryset = Gcarreira_escalao.objects.filter(categoria_id=categoria_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.categoria:
				self.fields['escalao'].queryset = self.instance.categoria.esc_categoria.order_by('escalao')

			if 'escalao' in self.data:
				try:
					escalao_id = self.data.get('escalao')
					self.fields['indice'].queryset = Gcarreira_indice.objects.filter(escalao_id=escalao_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.escalao_id:
				self.fields['indice'].queryset = self.instance.escalao.ind_escalao.filter(data_fim__isnull=True).order_by('indice')


		self.fields['data_inicio'].required = True
		self.fields['data_fim'].required = True
		self.fields['tipo_alteracao_ficha'].required = True
		self.fields['relacao_juridica_emprego'].required = True
		self.fields['regime'].required = True
		self.fields['categoria'].required = True
		self.fields['escalao'].required = True
		self.fields['indice'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('tipo_alteracao_ficha', css_class='col-md-4 my-3'),
				Column('relacao_juridica_emprego', css_class='col-md-4 my-3'),
			
				Column('regime', css_class='col-md-6 my-3'),
				Column('categoria', css_class='col-md-6 my-3'),
				Column('escalao', css_class='col-md-6 my-3'),
				Column('indice', css_class='col-md-6 my-3'),
			
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
				
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
				<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'><i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Ficha_permanenteForm(forms.ModelForm):
	data_inicio_categoria = forms.DateField(label='Data Inicio Categoria', widget=DateInput(), required=False)
	data_inicio = forms.DateField(label='Data Inicio Situação', widget=DateInput(), required=False)
	data_fim = forms.DateField(label='Data Fim Situação', widget=DateInput(), required=False)
	tipo_alteracao_ficha = forms.ModelChoiceField(label='Tipo de Alteração de Ficha',queryset=Tipo_alteracao_ficha.objects.exclude(tipo_alteracao_ficha__in= ('Contratação','Não Exercício','Regresso a Situação')),widget=forms.Select(attrs={'class': 'form-select ', 'id': 'tipo-alteracao-ficha-select'}))
	uuid_list = ['693b72aa-ddaf-48ae-84af-408a7b86a435', '9bafa3d0-8f3b-496a-a3c2-1aa9786b7a5a']
	relacao_juridica_emprego = forms.ModelChoiceField(label='Relação Juridica de Emprego',queryset=Relacao_juridica_emprego.objects.exclude(id_rje__in = uuid_list).exclude(relacao_juridica_emprego='Nomeação em Comissão de Serviço'),widget=forms.Select(attrs={'class': 'form-select ', 'id': 'relacao-juridica-select'}))
	regime = forms.ModelChoiceField(label='Regime',queryset=Gcarreira_regime.objects.all(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'regime-select'}))
	categoria = forms.ModelChoiceField(label='Categoria',queryset=Gcarreira_categoria.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'categoria-select'}))
	escalao = forms.ModelChoiceField(label='Escalão',queryset=Gcarreira_escalao.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'escalao-select'}))
	indice = forms.ModelChoiceField(label='Índice',queryset=Gcarreira_indice.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'indice-select'}))
    
	class Meta:
		model = Ficha_permanente
		fields = ['data_inicio_categoria','data_inicio','data_fim','regime','categoria','escalao','indice','tipo_alteracao_ficha','relacao_juridica_emprego',
				]
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if self.instance.pk:

			if 'regime' in self.data:
				try:
					regime_id = self.data.get('regime')
					self.fields['categoria'].queryset = Gcarreira_categoria.objects.filter(regime_id=regime_id)
				except (ValueError, TypeError):
					pass  # Invalid input; keep empty queryset
			elif self.instance.regime:
				self.fields['categoria'].queryset = self.instance.regime.cat_regime.order_by('categoria')

			if 'categoria' in self.data:
				try:
					categoria_id = self.data.get('categoria')
					self.fields['escalao'].queryset = Gcarreira_escalao.objects.filter(categoria_id=categoria_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.categoria:
				self.fields['escalao'].queryset = self.instance.categoria.esc_categoria.order_by('escalao')

			if 'escalao' in self.data:
				try:
					escalao_id = self.data.get('escalao')
					self.fields['indice'].queryset = Gcarreira_indice.objects.filter(escalao_id=escalao_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.escalao_id:
				self.fields['indice'].queryset = self.instance.escalao.ind_escalao.filter(data_fim__isnull=True).order_by('indice')


		self.fields['data_inicio'].required = True
		self.fields['data_fim'].required = False
		self.fields['tipo_alteracao_ficha'].required = True
		self.fields['relacao_juridica_emprego'].required = False
		self.fields['regime'].required = True
		self.fields['categoria'].required = True
		self.fields['escalao'].required = True
		self.fields['indice'].required = True
		self.fields['data_inicio_categoria'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('tipo_alteracao_ficha', css_class='col-md-4 my-3'),
				Column('relacao_juridica_emprego', css_class='col-md-4 my-3'),
			
				Column('regime', css_class='col-md-6 my-3'),
				Column('categoria', css_class='col-md-6 my-3'),
				Column('escalao', css_class='col-md-6 my-3'),
				Column('indice', css_class='col-md-6 my-3'),
			
				Column('data_inicio_categoria', css_class='col-md-6 my-3'),
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
				
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
				<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'><i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Ficha_comissao_servicoForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=False)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	tipo_alteracao_ficha = forms.ModelChoiceField(label='Tipo de Alteração de Ficha',queryset=Tipo_alteracao_ficha.objects.filter(id__in= ['41cb0d8e-9cc1-428c-ac4d-5979d6c01a6e']),widget=forms.Select(attrs={'class': 'form-select '}))
	uuid_list = ['d88ee1db-acfd-4f70-a941-e6739544b44a']
	relacao_juridica_emprego = forms.ModelChoiceField(label='Relação Juridica de Emprego',queryset=Relacao_juridica_emprego.objects.filter(id_rje__in = uuid_list),widget=forms.Select(attrs={'class': 'form-select '}))
	uuid_regime = ['fd269f0b-f01f-4862-ad21-b6c07b95fc79', 'a5a890b3-04f3-4a93-9ba7-7d0eaa031c5b','cc1e53b5-3142-408c-a573-9c4e886b1e35','a8788f5c-9407-4c93-a9da-0920e5a40f10']
	regime = forms.ModelChoiceField(label='Regime',queryset=Gcarreira_regime.objects.filter(id_regime__in=uuid_regime),widget=forms.Select(attrs={'class': 'form-select', 'id': 'regime-select'}))
	categoria = forms.ModelChoiceField(label='Categoria',queryset=Gcarreira_categoria.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'categoria-select'}))
	escalao = forms.ModelChoiceField(label='Escalão',queryset=Gcarreira_escalao.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'escalao-select'}))
	indice = forms.ModelChoiceField(label='Índice',queryset=Gcarreira_indice.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'indice-select'}))
	tipo_nomeacao = forms.ModelChoiceField(label='Tipo Nomeação',queryset=Tipo_nomeacao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select'}))
    
	class Meta:
		model = Ficha_comissao_servico
		fields = ['data_inicio','data_fim','regime','categoria','tipo_nomeacao','escalao','indice','tipo_alteracao_ficha','relacao_juridica_emprego',
				]
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if self.instance.pk:

			if 'regime' in self.data:
				try:
					regime_id = self.data.get('regime')
					self.fields['categoria'].queryset = Gcarreira_categoria.objects.filter(regime_id=regime_id)
				except (ValueError, TypeError):
					pass  # Invalid input; keep empty queryset
			elif self.instance.regime:
				self.fields['categoria'].queryset = self.instance.regime.cat_regime.order_by('categoria')

			if 'categoria' in self.data:
				try:
					categoria_id = self.data.get('categoria')
					self.fields['escalao'].queryset = Gcarreira_escalao.objects.filter(categoria_id=categoria_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.categoria:
				self.fields['escalao'].queryset = self.instance.categoria.esc_categoria.order_by('escalao')

			if 'escalao' in self.data:
				try:
					escalao_id = self.data.get('escalao')
					self.fields['indice'].queryset = Gcarreira_indice.objects.filter(escalao_id=escalao_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.escalao_id:
				self.fields['indice'].queryset = self.instance.escalao.ind_escalao.filter(data_fim__isnull=True).order_by('indice')


		self.fields['data_inicio'].required = True
		self.fields['data_fim'].required = False
		self.fields['tipo_alteracao_ficha'].required = True
		self.fields['tipo_nomeacao'].required = True
		self.fields['relacao_juridica_emprego'].required = True
		self.fields['regime'].required = True
		self.fields['categoria'].required = True
		self.fields['escalao'].required = True
		self.fields['indice'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('tipo_alteracao_ficha', css_class='col-md-4 my-3'),
				Column('relacao_juridica_emprego', css_class='col-md-4 my-3'),
				Column('tipo_nomeacao', css_class='col-md-4 my-3'),
			
				Column('regime', css_class='col-md-6 my-3'),
				Column('categoria', css_class='col-md-6 my-3'),
				Column('escalao', css_class='col-md-6 my-3'),
				Column('indice', css_class='col-md-6 my-3'),
			
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
				
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
				<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'><i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Ficha_nao_exercicioForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=False)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	motivo_nao_exercicio = forms.ModelChoiceField(label='Motivo Não Exercício',queryset=Motivo_nao_exercicio.objects.filter(),widget=forms.Select(attrs={'class': 'form-select'}))
    
	class Meta:
		model = Ficha_nao_exercicio
		fields = ['data_inicio','data_fim','motivo_nao_exercicio']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['data_inicio'].required = True
		self.fields['data_fim'].required = False
		self.fields['motivo_nao_exercicio'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('motivo_nao_exercicio', css_class='col-md-4 my-3'),
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
				
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
				<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'><i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)

class Ficha_saida_definitivaForm(forms.ModelForm):
	data_saida = forms.DateField(label='Data Saída', widget=DateInput(), required=False)
	motivo_saida = forms.ModelChoiceField(label='Motivo Saída',queryset=Motivo_saida.objects.filter(),widget=forms.Select(attrs={'class': 'form-select'}))
    
	class Meta:
		model = Ficha_saida_definitiva
		fields = ['data_saida','motivo_saida']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['data_saida'].required = False
		self.fields['motivo_saida'].required = True
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('motivo_saida', css_class='col-md-4 my-3'),
				Column('data_saida', css_class='col-md-6 my-3'),
				
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
				<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'><i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)


class Ficha_casualForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=False)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	tipo_casual = forms.ModelChoiceField(label='Tipo de Casuais',queryset=Tipo_casual.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	# uuid_list = ['d88ee1db-acfd-4f70-a941-e6739544b44a']
	categoria_casual = forms.ModelChoiceField(label='Categoria Casuais',queryset=Categoria_casual.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	uuid_regime = ['fd269f0b-f01f-4862-ad21-b6c07b95fc79', 'a5a890b3-04f3-4a93-9ba7-7d0eaa031c5b','cc1e53b5-3142-408c-a573-9c4e886b1e35','a8788f5c-9407-4c93-a9da-0920e5a40f10']
	regime = forms.ModelChoiceField(label='Regime',queryset=Gcarreira_regime.objects.exclude(id_regime__in=uuid_regime),widget=forms.Select(attrs={'class': 'form-select', 'id': 'regime-select'}))
	categoria = forms.ModelChoiceField(label='Categoria',queryset=Gcarreira_categoria.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'categoria-select'}))
	escalao = forms.ModelChoiceField(label='Escalão',queryset=Gcarreira_escalao.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'escalao-select'}))
	indice = forms.ModelChoiceField(label='Índice',queryset=Gcarreira_indice.objects.none(),widget=forms.Select(attrs={'class': 'form-select', 'id': 'indice-select'}))
	tipo_nomeacao = forms.ModelChoiceField(label='Tipo Nomeação',queryset=Tipo_nomeacao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select'}))
    
	class Meta:
		model = Ficha_casual
		fields = ['data_inicio','data_fim','regime','categoria','tipo_casual','escalao',
				'indice','categoria_casual','indice_casual'
				]
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if self.instance.pk:

			if 'regime' in self.data:
				try:
					regime_id = self.data.get('regime')
					self.fields['categoria'].queryset = Gcarreira_categoria.objects.filter(regime_id=regime_id)
				except (ValueError, TypeError):
					pass  # Invalid input; keep empty queryset
			elif self.instance.regime:
				self.fields['categoria'].queryset = self.instance.regime.cat_regime.order_by('categoria')

			if 'categoria' in self.data:
				try:
					categoria_id = self.data.get('categoria')
					self.fields['escalao'].queryset = Gcarreira_escalao.objects.filter(categoria_id=categoria_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.categoria:
				self.fields['escalao'].queryset = self.instance.categoria.esc_categoria.order_by('escalao')

			if 'escalao' in self.data:
				try:
					escalao_id = self.data.get('escalao')
					self.fields['indice'].queryset = Gcarreira_indice.objects.filter(escalao_id=escalao_id)
				except (ValueError, TypeError):
					pass
			elif self.instance.escalao_id:
				self.fields['indice'].queryset = self.instance.escalao.ind_escalao.filter(data_fim__isnull=True).order_by('indice')


		self.fields['data_inicio'].required = True
		self.fields['data_fim'].required = False
		self.fields['indice_casual'].required = False
		self.fields['tipo_casual'].required = True
		self.fields['categoria_casual'].required = True
		self.fields['regime'].required = False
		self.fields['categoria'].required = False
		self.fields['escalao'].required = False
		self.fields['indice'].required = False
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('tipo_casual', css_class='col-md-4 my-3'),
				Column('categoria_casual', css_class='col-md-4 my-3'),
			
				Column('regime', css_class='col-md-6 my-3'),
				Column('categoria', css_class='col-md-6 my-3'),
				Column('escalao', css_class='col-md-6 my-3'),
				Column('indice', css_class='col-md-6 my-3'),
				Column('indice_casual', css_class='col-md-6 my-3'),
			
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
				
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
				<a href='#' class='btn btn-warning mx-2' onclick=self.history.back()><i class='bi bi-arrow-left-square'></i> Cancelar</a>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'><i class="bi bi-save"></i> Guardar</button>
				</div> """)
		)