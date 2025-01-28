from django.db import models

# Create your models here.
class FuncionarioPivotCASEXO(models.Model):
	# id = models.UUIDField(primary_key=True)
	controlo_ativo = models.CharField(primary_key=True,max_length=225)
	masculino = models.IntegerField()
	feminino = models.IntegerField()
	total = models.IntegerField()
	class Meta:
		managed = False 
		db_table = 'sgrh"."view_statis_controlo_ativo_sexo'


class FuncionarioPivotTFSEXO(models.Model):
	# id = models.UUIDField(primary_key=True)
	tipo_funcionario = models.CharField(primary_key=True,max_length=225)
	masculino = models.IntegerField()
	feminino = models.IntegerField()
	total = models.IntegerField()
	class Meta:
		managed = False 
		db_table = 'sgrh"."view_statis_tipo_funcionario_sexo'


class FuncionarioPivotGISEXO(models.Model):
	# id = models.UUIDField(primary_key=True)
	grupu_idade = models.CharField(primary_key=True,max_length=225)
	masculino = models.IntegerField()
	feminino = models.IntegerField()
	total = models.IntegerField()
	class Meta:
		managed = False 
		db_table = 'sgrh"."view_statis_grupu_idade_sexo'

class FuncionarioPivotLTSEXO(models.Model):
	# id = models.UUIDField(primary_key=True)
	local_trabalho = models.CharField(primary_key=True,max_length=225)
	masculino = models.IntegerField()
	feminino = models.IntegerField()
	total = models.IntegerField()
	class Meta:
		managed = False 
		db_table = 'sgrh"."view_statis_local_trabalho_sexo'


