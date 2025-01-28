from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid
import datetime
from gcarreira.models import Gcarreira_regime

# Create your models here.
class Anos_AD(models.Model):
	id_anos = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	anos_de_avaliacao= models.CharField(max_length=225, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)

	class Meta:
		db_table = 'sgrh"."ad_anos'

	def __str__(self):
		template = '{0.anos_de_avaliacao}'
		return template.format(self)

class Gad_tipo_ad(models.Model):
	id_tipo_ad = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	tipo_avaliacao = models.CharField(max_length=100, null=True, blank=True)
	controlo_estado = models.CharField(max_length=100, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."ad_tipo'

	def __str__(self):
		template = '{0.tipo_avaliacao}'
		return template.format(self)

class Gad_classificacao_servico(models.Model):
	id_classificacao_servico = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	regime = models.ForeignKey(Gcarreira_regime, on_delete=models.CASCADE)
	valor_max = models.CharField(max_length=100, null=True, blank=True)
	valor_min = models.CharField(max_length=100, null=True, blank=True)
	qualitativa = models.CharField(max_length=100, null=True, blank=True)
	sigla = models.CharField(max_length=10, null=True, blank=True)
	controlo_estado = models.CharField(max_length=100, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."ad_classificacao'

	def __str__(self):
		template = '{0.qualitativa}'
		return template.format(self)

class Gad_ficha_avaliacao_desempenho(models.Model):
	id_avaliacao_desempenho = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	tipo_ad = models.ForeignKey(Gad_tipo_ad, on_delete=models.CASCADE)
	ano_ad = models.ForeignKey(Anos_AD, on_delete=models.CASCADE)
	classificacao_servico = models.ForeignKey(Gad_classificacao_servico, on_delete=models.CASCADE,null=True,blank=True)
	quantitativa = models.CharField(max_length=10)
	qualitativa = models.CharField(max_length=10 )
	avaliador = models.CharField(max_length=100, null=True, blank=True)
	data_ad = models.DateField(null=True,blank=True)
	controlo_estado = models.CharField(max_length=100, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."ad_ficha_avaliacao_desempenho'

	def __str__(self):
		template = '{0.funcionario} | {0.ano_ad} '
		return template.format(self)





