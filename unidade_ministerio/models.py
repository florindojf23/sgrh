import uuid
from django.db import models
from gdivisao_administrativa.models import *
from django.utils import timezone
now = timezone.now()


class Instituicao(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nome = models.CharField(max_length=225, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True, verbose_name='Data Inicio')
    data_fim = models.DateField(null=True, blank=True, verbose_name='Data Fim')
    controlo_ativo = models.CharField(max_length=225, null=True, blank=True)
    descricao = models.CharField(max_length=225, null=True, blank=True)
    inserido_em = models.DateTimeField(auto_now_add=True, null=True)
    alterado_em = models.DateTimeField(null=True, blank=True)
    inserido_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Alterado por')
    class Meta:
    	db_table = 'sgrh"."ministerio_instituicao'
    def __str__(self):
    	template = '{0.nome}'
    	return template.format(self)


# class Secretario_estado(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
#     instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,related_name='se_inst')
#     nome = models.CharField(max_length=225, null=True, blank=True)
#     data_inicio = models.DateField(null=True, blank=True, verbose_name='Data Inicio')
#     data_fim = models.DateField(null=True, blank=True, verbose_name='Data Fim')
#     controlo_ativo = models.CharField(max_length=225, null=True, blank=True)
#     descricao = models.CharField(max_length=225, null=True, blank=True)
#     inserido_em = models.DateTimeField(auto_now_add=True, null=True)
#     alterado_em = models.DateTimeField(null=True, blank=True)
#     inserido_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Alterado por')
#     class Meta:
#     	db_table = 'sgrh"."ministerio_secretario_estado'
#     def __str__(self):
#     	template = '{0.nome}'
#     	return template.format(self)


class Direcao_geral(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,related_name='dg_inst')
    # se = models.ForeignKey(Secretario_estado, null=True, blank=True, on_delete=models.CASCADE,related_name='dg_se')
    municipio = models.ForeignKey(Gdivisao_administrativa_municipio, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=225, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True, verbose_name='Data Inicio')
    data_fim = models.DateField(null=True, blank=True, verbose_name='Data Fim')
    controlo_ativo = models.CharField(max_length=225, null=True, blank=True)
    descricao = models.CharField(max_length=225, null=True, blank=True)
    equiparacao = models.BooleanField(default=False)
    inserido_em = models.DateTimeField(auto_now_add=True, null=True)
    alterado_em = models.DateTimeField(null=True, blank=True)
    inserido_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Alterado por')

    def Totalfuncionario(self):
        return Ficha_colocacao.objects.filter(dg=self).filter(data_fim__isnull=True,data_fim_gte=now).filter(controlo_ativo__isnull=True).count()

    class Meta:
    	db_table = 'sgrh"."ministerio_direcao_geral'
    def __str__(self):
   		template = '{0.nome}'
   		return template.format(self)


class Direcao_nacional(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,related_name='dn_inst')
    dg = models.ForeignKey(Direcao_geral, null=True, blank=True, on_delete=models.CASCADE,related_name='dn_dg')
    # se = models.ForeignKey(Secretario_estado, null=True, blank=True, on_delete=models.CASCADE,related_name='dn_se')
    municipio = models.ForeignKey(Gdivisao_administrativa_municipio, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=225, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True, verbose_name='Data Inicio')
    data_fim = models.DateField(null=True, blank=True, verbose_name='Data Fim')
    controlo_ativo = models.CharField(max_length=225, null=True, blank=True)
    descricao = models.CharField(max_length=225, null=True, blank=True)
    equiparacao = models.BooleanField(default=False)
    inserido_em = models.DateTimeField(auto_now_add=True, null=True)
    alterado_em = models.DateTimeField(null=True, blank=True)
    inserido_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Alterado por')
    class Meta:
    	db_table = 'sgrh"."ministerio_direcao_nacional'
    def __str__(self):
    	template = '{0.nome}'
    	return template.format(self)


class Departamento(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,related_name='dep_inst')
    dg = models.ForeignKey(Direcao_geral, null=True, blank=True, on_delete=models.CASCADE,related_name='dep_dg')
    dn = models.ForeignKey(Direcao_nacional, null=True, blank=True, on_delete=models.CASCADE,related_name='dep_dn')
    # se = models.ForeignKey(Secretario_estado, null=True, blank=True, on_delete=models.CASCADE,related_name='dep_se')
    municipio = models.ForeignKey(Gdivisao_administrativa_municipio, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=225, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True, verbose_name='Data Inicio')
    data_fim = models.DateField(null=True, blank=True, verbose_name='Data Fim')
    controlo_ativo = models.CharField(max_length=225, null=True, blank=True)
    descricao = models.CharField(max_length=225, null=True, blank=True)
    inserido_em = models.DateTimeField(auto_now_add=True, null=True)
    alterado_em = models.DateTimeField(null=True, blank=True)
    inserido_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Alterado por')
    class Meta:
    	db_table = 'sgrh"."ministerio_departamento'
    def __str__(self):
    	template = '{0.nome}'
    	return template.format(self)



class Seccao(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    # se = models.ForeignKey(Secretario_estado, null=True, blank=True, on_delete=models.CASCADE,related_name='sec_se')
    dep = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE,related_name='sec_dep')
    dg = models.ForeignKey(Direcao_geral, null=True, blank=True, on_delete=models.CASCADE,related_name='sec_dg')
    dn = models.ForeignKey(Direcao_nacional, null=True, blank=True, on_delete=models.CASCADE,related_name='sec_dn')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,related_name='sec_inst')
    municipio = models.ForeignKey(Gdivisao_administrativa_municipio, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=225, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True, verbose_name='Data Inicio')
    data_fim = models.DateField(null=True, blank=True, verbose_name='Data Fim')
    controlo_ativo = models.CharField(max_length=225, null=True, blank=True)
    descricao = models.CharField(max_length=225, null=True, blank=True)
    inserido_em = models.DateTimeField(auto_now_add=True, null=True)
    alterado_em = models.DateTimeField(null=True, blank=True)
    inserido_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Alterado por')
    class Meta:
    	db_table = 'sgrh"."ministerio_seccao'
    def __str__(self):
    	template = '{0.nome}'
    	return template.format(self)

# class Tipo_escola(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     tipo = models.CharField(max_length=100, null=True, blank=True)
#     controlo_estado = models.CharField(max_length=50, null=True, blank=True)

#     inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
#     inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
#     alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
#     alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

#     class Meta:
#         db_table = 'sgrh"."tipo_escola'

#     def __str__(self):
#         template = '{0.tipo} '
#         return template.format(self)

# class Escola(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
#     instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,related_name='escola_ins')
#     # se = models.ForeignKey(Secretario_estado, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_se')
#     dg = models.ForeignKey(Direcao_geral, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_dg')
#     dn = models.ForeignKey(Direcao_nacional, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_dn')
#     dep = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_dep')
#     municipio = models.ForeignKey(Gdivisao_administrativa_municipio, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_mun')
#     posto = models.ForeignKey(Gdivisao_administrativa_posto, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_posto')
#     suco = models.ForeignKey(Gdivisao_administrativa_suco, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_suco')
#     aldeia = models.ForeignKey(Gdivisao_administrativa_aldeia, null=True, blank=True, on_delete=models.CASCADE,related_name='escola_ald')
#     tipo_escola = models.ForeignKey(Tipo_escola, null=True, blank=True, on_delete=models.CASCADE)
#     nome = models.CharField(max_length=225, null=True, blank=True)
#     data_inicio = models.DateField(null=True, blank=True, verbose_name='Data Inicio')
#     data_fim = models.DateField(null=True, blank=True, verbose_name='Data Fim')
#     controlo_ativo = models.CharField(max_length=225, null=True, blank=True)
#     descricao = models.CharField(max_length=225, null=True, blank=True)
    
#     inserido_em = models.DateTimeField(auto_now_add=True, null=True)
#     alterado_em = models.DateTimeField(null=True, blank=True)
#     inserido_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Inserido por')
#     alterado_por = models.CharField(max_length=50, null=True, blank=True, verbose_name='Alterado por')
#     class Meta:
#     	db_table = 'sgrh"."ministerio_escola'
#     def __str__(self):
#     	template = '{0.nome}'
#     	return template.format(self)

# the views
class InstituicaoReport(models.Model):
    instituicao_id = models.UUIDField(primary_key=True)
    total_seccoes = models.IntegerField()
    total_departamentos = models.IntegerField()
    total_direcoes_nacionais = models.IntegerField()
    total_direcoes_gerais = models.IntegerField()
    # total_secretarios_estados = models.IntegerField()

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = 'sgrh"."view_instituicao_report'
