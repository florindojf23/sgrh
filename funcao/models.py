from django.db import models
# from gfuncionarios.models import Funcionarios
from gcarreira.models import *
# Create your models here.



class Relacao_juridica_emprego(models.Model):
	id_rje = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	relacao_juridica_emprego = models.CharField(max_length=100, null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."relacao_juridica_emprego'

	def __str__(self):
		template = '{0.relacao_juridica_emprego} '
		return template.format(self)

class Tipo_alteracao_ficha(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	tipo_alteracao_ficha = models.CharField(max_length=100, null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."tipo_alteracao_ficha'

	def __str__(self):
		template = '{0.tipo_alteracao_ficha} '
		return template.format(self)


class Tipo_nomeacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_nomeacao = models.CharField(max_length=100, null=True, blank=True)
    controlo_estado = models.CharField(max_length=50, null=True, blank=True)

    inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
    alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

    class Meta:
        db_table = 'sgrh"."tipo_nomeacao'

    def __str__(self):
        template = '{0.tipo_nomeacao} '
        return template.format(self)

class Motivo_nao_exercicio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    motivo = models.CharField(max_length=100, null=True, blank=True)
    controlo_estado = models.CharField(max_length=50, null=True, blank=True)

    inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
    alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

    class Meta:
        db_table = 'sgrh"."motivo_nao_exercicio'

    def __str__(self):
        template = '{0.motivo} '
        return template.format(self)

class Motivo_saida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    motivo = models.CharField(max_length=100, null=True, blank=True)
    controlo_estado = models.CharField(max_length=50, null=True, blank=True)

    inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
    alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

    class Meta:
        db_table = 'sgrh"."motivo_saida'

    def __str__(self):
        template = '{0.motivo} '
        return template.format(self)


class Ficha_contratacao(models.Model):
	id_contratacao = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	regime = models.ForeignKey(Gcarreira_regime, on_delete=models.CASCADE,null=True)
	categoria = models.ForeignKey(Gcarreira_categoria, on_delete=models.CASCADE,null=True)
	escalao = models.ForeignKey(Gcarreira_escalao, on_delete=models.CASCADE)
	indice = models.ForeignKey(Gcarreira_indice, on_delete=models.CASCADE)
	tipo_alteracao_ficha = models.ForeignKey(Tipo_alteracao_ficha, on_delete=models.SET_NULL,null=True)
	relacao_juridica_emprego = models.ForeignKey(Relacao_juridica_emprego, on_delete=models.SET_NULL,null=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."funcao_contratacao'

	def __str__(self):
		template = '{0.funcionario} | {0.escalao}'
		return template.format(self)


class Tipo_casual(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    controlo_estado = models.CharField(max_length=50, null=True, blank=True)

    inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
    alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

    class Meta:
        db_table = 'sgrh"."tipo_casual'

    def __str__(self):
        template = '{0.tipo} '
        return template.format(self)

class Categoria_casual(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    controlo_estado = models.CharField(max_length=50, null=True, blank=True)

    inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
    alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

    class Meta:
        db_table = 'sgrh"."categoria_casual'

    def __str__(self):
        template = '{0.categoria} '
        return template.format(self)


class Ficha_casual(models.Model):
	id_casual = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	regime = models.ForeignKey(Gcarreira_regime, on_delete=models.CASCADE,null=True)
	categoria = models.ForeignKey(Gcarreira_categoria, on_delete=models.CASCADE,null=True)
	escalao = models.ForeignKey(Gcarreira_escalao, on_delete=models.CASCADE)
	indice = models.ForeignKey(Gcarreira_indice, on_delete=models.CASCADE)
	tipo_casual = models.ForeignKey(Tipo_casual, on_delete=models.SET_NULL,null=True)
	categoria_casual = models.ForeignKey(Categoria_casual, on_delete=models.SET_NULL,null=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)
	indice_casual = models.CharField(max_length=50, null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."funcao_casuais'

	def __str__(self):
		template = '{0.funcionario} | {0.escalao}'
		return template.format(self)

class Ficha_permanente(models.Model):
	id_permanente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	regime = models.ForeignKey(Gcarreira_regime, on_delete=models.CASCADE,null=True)
	categoria = models.ForeignKey(Gcarreira_categoria, on_delete=models.CASCADE,null=True)
	escalao = models.ForeignKey(Gcarreira_escalao, on_delete=models.CASCADE)
	indice = models.ForeignKey(Gcarreira_indice, on_delete=models.CASCADE)
	tipo_alteracao_ficha = models.ForeignKey(Tipo_alteracao_ficha, on_delete=models.SET_NULL,null=True)
	relacao_juridica_emprego = models.ForeignKey(Relacao_juridica_emprego, on_delete=models.SET_NULL,null=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)
	data_inicio_categoria = models.DateField(verbose_name='Data Inicio Categoria', null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."funcao_permanente'

	def __str__(self):
		template = '{0.funcionario} | {0.escalao}'
		return template.format(self)

class Ficha_comissao_servico(models.Model):
	id_comissao_servico = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	regime = models.ForeignKey(Gcarreira_regime, on_delete=models.CASCADE,null=True)
	categoria = models.ForeignKey(Gcarreira_categoria, on_delete=models.CASCADE,null=True)
	escalao = models.ForeignKey(Gcarreira_escalao, on_delete=models.CASCADE)
	indice = models.ForeignKey(Gcarreira_indice, on_delete=models.CASCADE)
	tipo_alteracao_ficha = models.ForeignKey(Tipo_alteracao_ficha, on_delete=models.SET_NULL,null=True)
	tipo_nomeacao = models.ForeignKey(Tipo_nomeacao, on_delete=models.SET_NULL,null=True)
	relacao_juridica_emprego = models.ForeignKey(Relacao_juridica_emprego, on_delete=models.SET_NULL,null=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."funcao_comissao_servico'

	def __str__(self):
		template = '{0.funcionario} | {0.escalao}'
		return template.format(self)



class Ficha_nao_exercicio(models.Model):
	id_nao_exercicio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	motivo_nao_exercicio = models.ForeignKey(Motivo_nao_exercicio, on_delete=models.SET_NULL,null=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."ficha_nao_exercicio'

	def __str__(self):
		template = '{0.funcionario} | {0.motivo_nao_exercicio}'
		return template.format(self)

class Ficha_saida_definitiva(models.Model):
	id_saida = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey('gfuncionarios.Funcionarios', on_delete=models.CASCADE)
	motivo_saida = models.ForeignKey(Motivo_saida, on_delete=models.SET_NULL,null=True)
	data_saida = models.DateField(verbose_name='Data Saida', null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."ficha_saida_definitiva'

	def __str__(self):
		template = '{0.funcionario} | {0.motivo_saida}'
		return template.format(self)


