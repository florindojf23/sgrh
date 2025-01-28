from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div,HTML

from django.contrib.auth.models import User,Group
from .models import Core


class CoreForm(forms.ModelForm):
	# dob = forms.DateField(label='Data Moris', widget=DateInput(), required=False)
	# sex = forms.ChoiceField(
	# 	choices=[('Mane', 'Mane'), ('Feto', 'Feto')],
	# 	widget=forms.Select(attrs={'class': 'my-3 form-select '})
	# )
	logo = forms.FileField(
		widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
	)
    
	class Meta:
		model = Core
		fields = ['sysname','syssigla','owner','nu_kontaktu','enderesu','logo','about']
		excluded = ['is_active']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-10'
		self.helper.layout = Layout(
			Row(
				Column('sysname', css_class='my-3'),
				Column('syssigla', css_class='my-3'),
				css_class='form-row'
			),
			Row(
				Column('owner', css_class='my-3'),
				Column('enderesu', css_class='my-3'),
				Column('nu_kontaktu', css_class='my-3'),
				Column('about', css_class='my-3'),
				Column('logo', css_class='', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200'/> </center> """),	
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
					<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'>Save Changes</button>
				</div> """)
		)
