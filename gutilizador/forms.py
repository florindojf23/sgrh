from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div,HTML

from django.contrib.auth.models import User,Group
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Row(
                Column('username'),
                Column('email'),
                css_class='form-row'
            ),
            Div(
                Submit('submit', 'Save Changes', css_class='btn btn-primary', css_id='kt_account_profile_details_submit'),
                css_class='card-footer d-flex justify-content-end py-6 px-9'
            )
        )


class DateInput(forms.DateInput):
	input_type = 'date'

class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['group'] = forms.ModelChoiceField(
            queryset=Group.objects.all(),
            empty_label='No group'
        )
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			HTML(""" <br><button type="submit" class="btn btn-sm btn-success btn-icon-text"><i class="mdi mdi-content-save"></i> Save </button> """)
		)

class ProfileUpdateForm(forms.ModelForm):
	dob = forms.DateField(label='Data Moris', widget=DateInput(), required=False)
	sex = forms.ChoiceField(
		choices=[('Mane', 'Mane'), ('Feto', 'Feto')],
		widget=forms.Select(attrs={'class': 'my-3 form-select '})
	)
	# image = forms.FileField(
	# 	widget=forms.ClearableFileInput(attrs={'class': 'form-control '})
	# )
    
	class Meta:
		model = Profile
		fields = ['first_name','last_name','pob','dob','sex']
		excluded = ['image']
		labels = {
		    "sex": "seksu"
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-10'
		self.helper.layout = Layout(
			Row(
				Column('first_name', css_class='my-3'),
				Column('last_name', css_class='my-3'),
				css_class='form-row'
			),
			Row(
				# Column('sex', css_class='my-3'),
				Column('sex', css_class='my-3'),
				Column('pob', css_class='my-3'),
				Column('dob', css_class='my-3'),
				# Column('image', css_class='', onchange="myFunction()"),
				css_class='form-row'
			),
			# HTML(""" <center> <img id='output' width='200' /> </center> """),	
			HTML(""" <br><div class='card-footer d-flex justify-content-end py-6 px-9'>
												<button type='submit' class='btn btn-primary' id='kt_account_profile_details_submit'>Save Changes</button>
											</div> """)
		)
