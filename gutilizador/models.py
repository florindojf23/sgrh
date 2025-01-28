from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid
from master.utils_upload import upload_profile
from gfuncionarios.models import Funcionarios
import datetime

# Create your models here.
class Profile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user_profile")
	first_name = models.CharField(max_length=30, null=True, blank=True)
	last_name = models.CharField(max_length=30, null=True, blank=True)
	pob = models.CharField(max_length=50, verbose_name='Fatin Moris', null=True, blank=True)
	dob = models.DateField(verbose_name='Data Moris', null=True, blank=True)
	sex = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')], max_length=6, null=True, blank=True)
	image = models.ImageField(upload_to=upload_profile, null=True, blank=True,
			validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], verbose_name="Upload Imajen")
	date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

	def getAge(self):
		if self.dob:
			return datetime.date.today().year - self.dob.year
		else:
			return 0
			
	def getTotalLogin(self):
		return AuditLogin.objects.filter(user=self.user).count()

	class Meta:
		db_table = 'sgrh"."profile'
		
	def __str__(self):
		template = '{0.user}, {0.first_name} {0.last_name}'
		return template.format(self)

class Funcionario_user(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user_funcionario")
	funcionario = models.ForeignKey(Funcionarios, on_delete=models.SET_NULL,null=True)

	# def getTotalLogin(self):
	# 	return AuditLogin.objects.filter(user=self.user).count()

	class Meta:
		db_table = 'sgrh"."auth_user_funcionario'
		
	def __str__(self):
		template = '{0.user}'
		return template.format(self)

class AuditLogin(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="audituserlogin")
	login_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

	class Meta:
		db_table = 'sgrh"."gauditlogin'

	def __str__(self):
		template = '{0.user}, {0.login_time}'
		return template.format(self)

# class Gauth_permissao(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	nivel = models.CharField(max_length=30)
# 	permissao = models.CharField(max_length=30)

# 	class Meta:
# 		db_table = 'sgrh"."gauth_permissao'

# 	def __str__(self):
# 		template = '{0.permissao}'
# 		return template.format(self)

class Gestao(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nome_gestao = models.CharField(max_length=100)
	sigla_gestao = models.CharField(max_length=100)
	controlo_estado = models.CharField(max_length=100)
	descricao = models.TextField()

	class Meta:
		db_table = 'sgrh"."gestao'

	def __str__(self):
		template = '{0.nome_gestao}'
		return template.format(self)


# class Gauth_perfil_usuario(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	perfil = models.CharField(max_length=50, null=True, blank=True)
# 	permissao = models.ForeignKey(Gauth_permissao, on_delete=models.CASCADE)

# 	class Meta:
# 		db_table = 'sgrh"."gauth_perfil_usuario'
		
# 	def __str__(self):
# 		template = '{0.perfil}'
# 		return template.format(self)

# class Gauth_permissao_acesso_usuario(models.Model):
# 	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
# 	perfil = models.ForeignKey(Gauth_perfil_usuario, on_delete=models.CASCADE)
# 	gestao = models.ForeignKey(Gauth_gestao, on_delete=models.CASCADE)
# 	data_termina = models.DateField(verbose_name='Data Termina  Permissao', null=True, blank=True)
# 	controlo_ativo = models.CharField(max_length=50, null=True, blank=True)

# 	class Meta:
# 		db_table = 'sgrh"."gauth_permissao_acesso_usuario'
		
# 	def __str__(self):
# 		template = '{0.usuario}'
# 		return template.format(self)






