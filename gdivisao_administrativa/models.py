from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.
class Gdivisao_administrativa_municipio(models.Model):
	id_municipio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	municipio = models.CharField(max_length=225, null=True, blank=True)
	codigo_municipio = models.CharField(max_length=20, null=True, blank=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gdivisao_administrativa_municipio'

	def __str__(self):
		template = '{0.municipio}'
		return template.format(self)

class Gdivisao_administrativa_posto(models.Model):
	id_posto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	municipio = models.ForeignKey(Gdivisao_administrativa_municipio, on_delete=models.CASCADE, null=True,related_name='postos')
	posto = models.CharField(max_length=225, null=True, blank=True)
	codigo_posto = models.CharField(max_length=20, null=True, blank=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gdivisao_administrativa_posto'

	def __str__(self):
		template = '{0.posto}'
		return template.format(self)

class Gdivisao_administrativa_suco(models.Model):
	id_suco = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	posto = models.ForeignKey(Gdivisao_administrativa_posto, on_delete=models.CASCADE, null=True,related_name='sucos')
	suco = models.CharField(max_length=225, null=True, blank=True)
	codigo_suco = models.CharField(max_length=20, null=True, blank=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gdivisao_administrativa_suco'

	def __str__(self):
		template = '{0.suco}'
		return template.format(self)

class Gdivisao_administrativa_aldeia(models.Model):
	id_aldeia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	suco = models.ForeignKey(Gdivisao_administrativa_suco, on_delete=models.CASCADE, null=True,related_name='aldeias')
	aldeia = models.CharField(max_length=225, null=True, blank=True)
	codigo_aldeia = models.CharField(max_length=20, null=True, blank=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."gdivisao_administrativa_aldeia'

	def __str__(self):
		template = '{0.aldeia}'
		return template.format(self)

class ViewDivisaoAdministrativa(models.Model):
    id_municipio = models.UUIDField(primary_key=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    data_inicio_municipio = models.DateField(default='1970-01-01')
    data_fim_municipio = models.DateField(default='1970-01-01')
    posto = models.CharField(max_length=100, null=True, blank=True)
    data_inicio_posto = models.DateField(default='1970-01-01')
    data_fim_posto = models.DateField(default='1970-01-01')
    suco = models.CharField(max_length=100, null=True, blank=True)
    data_inicio_suco = models.DateField(default='1970-01-01')
    data_fim_suco = models.DateField(default='1970-01-01')
    aldeia = models.CharField(max_length=100, null=True, blank=True)
    data_inicio_aldeia = models.DateField(default='1970-01-01')
    data_fim_aldeia = models.DateField(default='1970-01-01')

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = 'sgrh"."view_divisao_administrativa'

