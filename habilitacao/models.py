from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid
import datetime
from gcarreira.models import Gcarreira_regime
from master.models import Pais

# Create your models here.
class Nivel_habilitacao(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nivel_habilitacao= models.CharField(max_length=225, null=True, blank=True)
	controlo_estado = models.CharField(max_length=100, null=True, blank=True)
	ordem= models.CharField(max_length=225, null=True, blank=True)
	pontos_promocao_rg = models.CharField(max_length=100, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)

	class Meta:
		db_table = 'sgrh"."hab_nivel_habilitacao'

	def __str__(self):
		template = '{0.nivel_habilitacao}'
		return template.format(self)

class Entidade_habilitacao(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	entidade = models.CharField(max_length=100, null=True, blank=True)
	tipo_entidade = models.CharField(max_length=100, null=True, blank=True)
	controlo_estado = models.CharField(max_length=100, null=True, blank=True)
	pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."hab_entidade'

	def __str__(self):
		template = '{0.entidade}'
		return template.format(self)

class Curso_habilitacao(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nome_curso = models.CharField(max_length=225, null=True, blank=True)
	sigla = models.CharField(max_length=10, null=True, blank=True)
	controlo_estado = models.CharField(max_length=100, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."hab_curso'

	def __str__(self):
		template = '{0.nome_curso}'
		return template.format(self)

class Habilitacao_academica(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	nivel_habilitacao = models.ForeignKey(Nivel_habilitacao, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso_habilitacao, on_delete=models.CASCADE)
	entidade = models.ForeignKey(Entidade_habilitacao, on_delete=models.CASCADE,null=True,blank=True)
	data_inicio = models.DateField(null=True,blank=True)
	data_habilitacao = models.DateField(null=True,blank=True)
	controlo_estado = models.CharField(max_length=100, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."hab_habilitacao_academica'

	def __str__(self):
		template = '{0.funcionario} | {0.nivel_habilitacao} '
		return template.format(self)






class DashboardHabilitacao(models.Model):
    id_habilitacao = models.UUIDField(primary_key=True)
    nivel_habilitacao = models.IntegerField()
    total_habilitacao = models.IntegerField()

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = 'sgrh"."view_dashboard_habilitacao'

class ViewMonitorHabilitacao(models.Model):
    id = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=225, null=True, blank=True)
    sexo = models.CharField(max_length=20, null=True, blank=True)
    id_sigap = models.CharField(max_length=20, null=True, blank=True)
    data_inicio_habilitacao = models.DateField(default='1970-01-01')
    data_fim_habilitacao = models.DateField(default='1970-01-01')
    nivel_habilitacao = models.CharField(max_length=50, null=True, blank=True)
    curso = models.CharField(max_length=100, null=True, blank=True)
    entidade = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = 'sgrh"."view_monitor_habilitacao'
