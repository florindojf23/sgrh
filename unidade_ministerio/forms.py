from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div,HTML

from django.contrib.auth.models import User,Group
from .models import *
from gdivisao_administrativa.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class Direcao_geralForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=True)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	instituicao = forms.ModelChoiceField(label='Instituicao',queryset=Instituicao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	# se = forms.ModelChoiceField(label='Secretariado',queryset=Secretario_estado.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	municipio = forms.ModelChoiceField(label='Municipio',queryset=Gdivisao_administrativa_municipio.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Direcao_geral
		fields = ['nome','data_inicio','data_fim','instituicao','municipio']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nome'].required = True
		self.fields['data_inicio'].required = True
		self.fields['instituicao'].required = True
		# self.fields['se'].required = False
		self.fields['municipio'].required = False
		default_instituicao = Instituicao.objects.filter(nome='Ministério da Educação').last()
		self.fields['instituicao'].initial = default_instituicao
		default_municipio = Gdivisao_administrativa_municipio.objects.filter(municipio='Dili').last()
		self.fields['municipio'].initial = default_municipio
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('instituicao', css_class='col-md-4 my-3'),
				Column('se', css_class='col-md-4 my-3'),
				Column('municipio', css_class='col-md-4 my-3'),
				Column('nome', css_class='col-md-12 my-3'),
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'>Guardar</button>
				</div> """)
		)

class Direcao_nacionalForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=True)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	instituicao = forms.ModelChoiceField(label='Instituicao',queryset=Instituicao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	# se = forms.ModelChoiceField(label='Secretariado',queryset=Secretario_estado.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	dg = forms.ModelChoiceField(label='Direcao geral',queryset=Direcao_geral.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	municipio = forms.ModelChoiceField(label='Municipio',queryset=Gdivisao_administrativa_municipio.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	equiparacao = forms.BooleanField(
        label="Equiparação", 
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})  # Custom class for Bootstrap, for example
    )
    
	class Meta:
		model = Direcao_nacional
		fields = ['nome','data_inicio','data_fim','instituicao','dg','municipio','equiparacao']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nome'].required = True
		self.fields['data_inicio'].required = True
		self.fields['instituicao'].required = True
		# self.fields['se'].required = False
		self.fields['dg'].required = False
		self.fields['municipio'].required = False
		default_instituicao = Instituicao.objects.filter(nome='Ministério da Educação').last()
		self.fields['instituicao'].initial = default_instituicao
		default_municipio = Gdivisao_administrativa_municipio.objects.filter(municipio='Dili').last()
		self.fields['municipio'].initial = default_municipio
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('instituicao', css_class='col-md-6 my-3'),
				Column('se', css_class='col-md-6 my-3'),
				Column('dg', css_class='col-md-6 my-3'),
				Column('municipio', css_class='col-md-6 my-3'),
				Column('nome', css_class='col-md-9 my-3'),
				Column('equiparacao', css_class='col-md-3 mt-5'),
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'>Guardar</button>
				</div> """)
		)


class DepartamentoForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=True)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	instituicao = forms.ModelChoiceField(label='Instituicao',queryset=Instituicao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	# se = forms.ModelChoiceField(label='Secretariado',queryset=Secretario_estado.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	dg = forms.ModelChoiceField(label='Direcao Geral',queryset=Direcao_geral.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	dn = forms.ModelChoiceField(label='DIrecao Nacional',queryset=Direcao_nacional.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	municipio = forms.ModelChoiceField(label='Municipio',queryset=Gdivisao_administrativa_municipio.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Departamento
		fields = ['nome','data_inicio','data_fim','instituicao','dg','municipio','dn']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['instituicao'].queryset = Instituicao.objects.all()
		# self.fields['se'].queryset = Secretario_estado.objects.none()
		self.fields['dg'].queryset = Direcao_geral.objects.none()
		self.fields['dn'].queryset = Direcao_nacional.objects.none()
		if self.instance.pk:
			# if 'instituicao' in self.data:
			# 	try:
			# 		ins_id = self.data.get('instituicao')
			# 		self.fields['se'].queryset = Secretario_estado.objects.filter(instituicao__id=ins_id).order_by('nome')
			# 	except (ValueError, TypeError):
			# 		pass
			# elif self.instance.instituicao_id:
			# 	self.fields['se'].queryset = self.instance.instituicao.se_inst.order_by('nome')

			if 'instituicao' in self.data:
				try:
					ins_id = self.data.get('instituicao')
					self.fields['dg'].queryset = Direcao_geral.objects.filter(instituicao__id=ins_id).order_by('nome')
					print("dg queryset set based on ins:", self.fields['dg'].queryset)
				except (ValueError, TypeError):
					pass
			elif self.instance.instituicao_id:
				self.fields['dg'].queryset = self.instance.instituicao.dg_inst.order_by('nome')

			if 'instituicao' in self.data:
				try:
					ins_id = self.data.get('instituicao')
					self.fields['dn'].queryset = Direcao_nacional.objects.filter(instituicao__id=ins_id).order_by('nome')
					print("dn queryset set based on ins:", self.fields['dn'].queryset)
					print("dn queryset set based on ins:", self.fields['dn'].queryset)
				except (ValueError, TypeError):
					pass
			elif self.instance.instituicao_id:
				self.fields['dn'].queryset = self.instance.instituicao.dn_inst.order_by('nome')

			if 'dg' in self.data:
				try:
					dg_id = self.data.get('dg')
					if dg_id:
						self.fields['dn'].queryset = Direcao_nacional.objects.filter(dg__id=dg_id).order_by('nome')
				except (ValueError, TypeError):
					pass
			elif self.instance.dg:
				print("tamtattajtrljtlajl_dg:",self.instance.dg)
				self.fields['dn'].queryset = self.instance.dg.dn_dg.order_by('nome')

		self.fields['nome'].required = True
		self.fields['data_inicio'].required = True
		self.fields['instituicao'].required = True
		# self.fields['se'].required = False
		self.fields['dg'].required = False
		self.fields['dn'].required = True
		self.fields['municipio'].required = False
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('instituicao', css_class='col-md-4 my-3'),
				Column('se', css_class='col-md-4 my-3'),
				Column('dg', css_class='col-md-4 my-3'),
				Column('dn', css_class='col-md-6 my-3'),
				Column('municipio', css_class='col-md-6 my-3'),
				Column('nome', css_class='col-md-12 my-3'),
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'>Guardar</button>
				</div> """)
		)


class SeccaoForm(forms.ModelForm):
	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=True)
	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
	instituicao = forms.ModelChoiceField(label='Instituicao',queryset=Instituicao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
	# se = forms.ModelChoiceField(label='Secretariado',queryset=Secretario_estado.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	dg = forms.ModelChoiceField(label='Direcao Geral',queryset=Direcao_geral.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	dn = forms.ModelChoiceField(label='Direcao Nacional',queryset=Direcao_nacional.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	dep = forms.ModelChoiceField(label='Departamento',queryset=Departamento.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
	municipio = forms.ModelChoiceField(label='Municipio',queryset=Gdivisao_administrativa_municipio.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
    
	class Meta:
		model = Seccao
		fields = ['nome','data_inicio','data_fim','instituicao','dg','municipio','dn','dep']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['instituicao'].queryset = Instituicao.objects.all()
		# self.fields['se'].queryset = Secretario_estado.objects.none()
		self.fields['dg'].queryset = Direcao_geral.objects.none()
		self.fields['dn'].queryset = Direcao_nacional.objects.none()
		self.fields['dep'].queryset = Departamento.objects.none()
		if self.instance.pk:
			# if 'instituicao' in self.data:
			# 	try:
			# 		ins_id = self.data.get('instituicao')
			# 		self.fields['se'].queryset = Secretario_estado.objects.filter(instituicao__id=ins_id).order_by('nome')
			# 	except (ValueError, TypeError):
			# 		pass
			# elif self.instance.instituicao_id:
			# 	self.fields['se'].queryset = self.instance.instituicao.se_inst.order_by('nome')

			if 'instituicao' in self.data:
				try:
					ins_id = self.data.get('instituicao')
					self.fields['dg'].queryset = Direcao_geral.objects.filter(instituicao__id=ins_id).order_by('nome')
					print("dg queryset set based on ins:", self.fields['dg'].queryset)
				except (ValueError, TypeError):
					pass
			elif self.instance.instituicao_id:
				self.fields['dg'].queryset = self.instance.instituicao.dg_inst.order_by('nome')

			if 'instituicao' in self.data:
				try:
					ins_id = self.data.get('instituicao')
					self.fields['dn'].queryset = Direcao_nacional.objects.filter(instituicao__id=ins_id).order_by('nome')
					print("dn queryset set based on ins:", self.fields['dn'].queryset)
					print("dn queryset set based on ins:", self.fields['dn'].queryset)
				except (ValueError, TypeError):
					pass
			elif self.instance.instituicao_id:
				self.fields['dn'].queryset = self.instance.instituicao.dn_inst.order_by('nome')

			if 'dg' in self.data:
				try:
					dg_id = self.data.get('dg')
					if dg_id:
						self.fields['dn'].queryset = Direcao_nacional.objects.filter(dg__id=dg_id).order_by('nome')
				except (ValueError, TypeError):
					pass
			elif self.instance.dg:
				print("tamtattajtrljtlajl_dg:",self.instance.dg)
				self.fields['dn'].queryset = self.instance.dg.dn_dg.order_by('nome')

			if 'dn' in self.data:
				print("tamaqqqqqqqqqqqqqqqqqqqqqq:",self.data.get('dn'))
				try:
					dn_id = self.data.get('dn')
					self.fields['dep'].queryset = Departamento.objects.filter(dn__id=dn_id).order_by('nome')
				except (ValueError, TypeError):
					pass
			elif self.instance.dn:
				print("tama:",self.instance.dn)
				self.fields['dep'].queryset = self.instance.dn.dep_dn.order_by('nome')

			

		self.fields['nome'].required = True
		self.fields['data_inicio'].required = True
		self.fields['instituicao'].required = True
		# self.fields['se'].required = False
		self.fields['dg'].required = False
		self.fields['dn'].required = True
		self.fields['dep'].required = True
		self.fields['municipio'].required = False
		default_instituicao = Instituicao.objects.filter(nome='Ministério da Educação').last()
		default_municipio = Gdivisao_administrativa_municipio.objects.filter(municipio='Dili').last()
		self.fields['municipio'].initial = default_municipio

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'row mt-4'
		self.helper.layout = Layout(
			
				Column('instituicao', css_class='col-md-4 my-3'),
				Column('se', css_class='col-md-4 my-3'),
				Column('dg', css_class='col-md-4 my-3'),
				Column('dn', css_class='col-md-4 my-3'),
				Column('dep', css_class='col-md-4 my-3'),
				Column('municipio', css_class='col-md-4 my-3'),
				Column('nome', css_class='col-md-12 my-3'),
				Column('data_inicio', css_class='col-md-6 my-3'),
				Column('data_fim', css_class='col-md-6 my-3'),
			
			
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'>Guardar</button>
				</div> """)
		)




# class EscolaForm(forms.ModelForm):
# 	data_inicio = forms.DateField(label='Data Inicio', widget=DateInput(), required=True)
# 	data_fim = forms.DateField(label='Data Fim', widget=DateInput(), required=False)
# 	# instituicao = forms.ModelChoiceField(label='Instituicao',queryset=Instituicao.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	# se = forms.ModelChoiceField(label='Secretariado',queryset=Secretario_estado.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	dg = forms.ModelChoiceField(label='Direcao Geral',queryset=Direcao_geral.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	dn = forms.ModelChoiceField(label='Direcao Nacional',queryset=Direcao_nacional.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	# dep = forms.ModelChoiceField(label='Departamento',queryset=Departamento.objects.filter(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	municipio = forms.ModelChoiceField(label='Municipio',queryset=Gdivisao_administrativa_municipio.objects.all(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	posto = forms.ModelChoiceField(label='Posto Administrativo',queryset=Gdivisao_administrativa_posto.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	suco = forms.ModelChoiceField(label='Suco',queryset=Gdivisao_administrativa_suco.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	aldeia = forms.ModelChoiceField(label='Aldeia',queryset=Gdivisao_administrativa_aldeia.objects.none(),widget=forms.Select(attrs={'class': 'form-select '}))
# 	tipo_escola = forms.ModelChoiceField(label='Nivel Escola',queryset=Tipo_escola.objects.filter(controlo_estado__isnull=True),widget=forms.Select(attrs={'class': 'form-select '}))
    
# 	class Meta:
# 		model = Escola
# 		fields = ['nome','data_inicio','data_fim','dg','municipio','dn','posto','suco','aldeia','tipo_escola']

		
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.fields['dg'].queryset = Direcao_geral.objects.all()
# 		self.fields['dn'].queryset = Direcao_nacional.objects.none()
# 		self.fields['municipio'].queryset = Gdivisao_administrativa_municipio.objects.all()
# 		self.fields['posto'].queryset = Gdivisao_administrativa_posto.objects.none()
# 		self.fields['suco'].queryset = Gdivisao_administrativa_suco.objects.none()
# 		self.fields['aldeia'].queryset = Gdivisao_administrativa_aldeia.objects.none()
# 		if self.instance.pk:
# 			if 'dg' in self.data:
# 				try:
# 					dg_id = self.data.get('dg')
# 					self.fields['dn'].queryset = Direcao_nacional.objects.filter(dg__id=dg_id).order_by('nome')
# 					print("dn queryset set based on dg:", self.fields['dn'].queryset)
# 				except (ValueError, TypeError):
# 					pass
# 			elif self.instance.dg:
# 				print("tamtattajtrljtlajl_dg:",self.instance.dg)
# 				self.fields['dn'].queryset = self.instance.dg.dn_dg.order_by('nome')

# 			if 'municipio' in self.data:
# 				print('municipio:',self.data)
# 				try:
# 					municipio_id = self.data.get('municipio')
# 					self.fields['posto'].queryset = Gdivisao_administrativa_posto.objects.filter(municipio__id_municipio=municipio_id).order_by('posto')
# 					print("Posto queryset set based on municipio:", self.fields['posto'].queryset)
# 				except (ValueError, TypeError):
# 					pass
# 			elif self.instance.municipio:
# 				print("tamtattajtrljtlajl_mun:",self.instance.municipio)
# 				self.fields['posto'].queryset = self.instance.municipio.postos.order_by('posto')

# 			if 'posto' in self.data:
# 				print("posto:",self.instance.pk)
# 				print("posto2:",self.data.get('posto'))
# 				try:
# 					posto_id = self.data.get('posto')
# 					self.fields['suco'].queryset = Gdivisao_administrativa_suco.objects.filter(posto__id_posto=posto_id).order_by('suco')
# 					print("Suco queryset set based on posto:", self.fields['suco'].queryset)
# 				except (ValueError, TypeError):
# 					pass
# 			elif self.instance.posto:
# 				self.fields['suco'].queryset = self.instance.posto.sucos.order_by('suco')

# 			if 'suco' in self.data:
# 				try:
# 					suco_id = self.data.get('suco')
# 					self.fields['aldeia'].queryset = Gdivisao_administrativa_aldeia.objects.filter(suco__id_suco=suco_id).order_by('aldeia')
# 					print("Aldeia queryset set based on suco:", self.fields['aldeia'].queryset)
# 				except (ValueError, TypeError):
# 					pass
# 			elif self.instance.suco:
# 				self.fields['aldeia'].queryset = self.instance.suco.aldeias.order_by('aldeia')

# 		self.fields['nome'].required = True
# 		self.fields['data_inicio'].required = True
# 		# self.fields['instituicao'].required = True
# 		# self.fields['se'].required = False
# 		self.fields['dg'].required = False
# 		self.fields['dn'].required = False
# 		# self.fields['dep'].required = False
# 		self.fields['municipio'].required = True
# 		self.fields['aldeia'].required = False
# 		self.helper = FormHelper()
# 		self.helper.form_method = 'post'
# 		self.helper.form_class = 'row mt-4'
# 		self.helper.layout = Layout(
			
# 				# Column('instituicao', css_class='col-md-4 my-3'),
# 				# Column('se', css_class='col-md-4 my-3'),
# 				Column('dg', css_class='col-md-6 my-3'),
# 				Column('dn', css_class='col-md-6 my-3'),
# 				# Column('dep', css_class='col-md-4 my-3'),
# 				Column('municipio', css_class='col-md-3 my-3'),
# 				Column('posto', css_class='col-md-3 my-3'),
# 				Column('suco', css_class='col-md-3 my-3'),
# 				Column('aldeia', css_class='col-md-3 my-3'),
# 				Column('nome', css_class='col-md-6 my-3'),
# 				Column('tipo_escola', css_class='col-md-6 my-3'),
# 				Column('data_inicio', css_class='col-md-6 my-3'),
# 				Column('data_fim', css_class='col-md-6 my-3'),
			
			
# 			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
# 					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'>Guardar</button>
# 				</div> """)
# 		)


