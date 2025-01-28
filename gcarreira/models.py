from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.
class Gcarreira_regime(models.Model):
	id_regime = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	regime = models.CharField(max_length=225, null=True, blank=True)
	base_legal = models.CharField(max_length=100, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gcarreira_regime'

	def __str__(self):
		template = '{0.regime}'
		return template.format(self)

class Gcarreira_categoria(models.Model):
	id_categoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	regime = models.ForeignKey(Gcarreira_regime, on_delete=models.CASCADE,related_name='cat_regime')
	categoria = models.CharField(max_length=225, null=True, blank=True)
	base_legal = models.CharField(max_length=20, null=True, blank=True)
	abreviatura = models.CharField(max_length=20, null=True, blank=True)
	escalao_maximo = models.CharField(max_length=20, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gcarreira_categoria'

	def __str__(self):
		template = '{0.categoria}'
		return template.format(self)

class Gcarreira_categoria_alias(models.Model):
	id_categoria_alias = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	categoria = models.ForeignKey(Gcarreira_categoria, on_delete=models.CASCADE)
	categoria_alias = models.CharField(max_length=225, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gcarreira_categoria_alias'

	def __str__(self):
		template = '{0.categoria_alias}'
		return template.format(self)

class Gcarreira_composicao(models.Model):
	id_composicao = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	composicao = models.CharField(max_length=225, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gcarreira_composicao'

	def __str__(self):
		template = '{0.composicao}'
		return template.format(self)

class Gcarreira_escalao(models.Model):
	id_escalao = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	categoria = models.ForeignKey(Gcarreira_categoria, on_delete=models.CASCADE,related_name='esc_categoria')
	escalao = models.CharField(max_length=100, null=True, blank=True)
	escalao_numerico = models.CharField(max_length=100, null=True, blank=True)
	codigo_grp = models.CharField(max_length=100, null=True, blank=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gcarreira_escalao'

	def __str__(self):
		template = '{0.escalao}'
		return template.format(self)

class Gcarreira_indice(models.Model):
	id_indice = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	escalao = models.ForeignKey(Gcarreira_escalao, on_delete=models.CASCADE,related_name='ind_escalao')
	composicao = models.ForeignKey(Gcarreira_composicao, on_delete=models.CASCADE)
	indice = models.CharField(max_length=100, null=True, blank=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gcarreira_indice'

	def __str__(self):
		template = '{0.indice}'
		return template.format(self)

