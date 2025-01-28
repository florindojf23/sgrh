from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid
import datetime
from gdivisao_administrativa.models import *
from unidade_ministerio.models import *
from funcao.models import *
from django.utils import timezone
now = timezone.now()
from django.db.models import Q
from datetime import date

# Create your models here.
class Funcionarios(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nome = models.CharField(max_length=225, null=True, blank=True)
	sexo = models.CharField(choices=[('Masculino','Masculino'),('Feminino','Feminino')], max_length=15,default='Masculino')
	id_sigap = models.CharField(max_length=30, null=True, blank=True)
	id_grp = models.CharField(max_length=50, verbose_name='Id GRP', null=True, blank=True)
	data_nascimento = models.DateField(verbose_name='Data de Nascimento',default='1970-01-01')
	lugar_nascimento = models.CharField(max_length=50, null=True, blank=True)
	nu_telemovel = models.CharField(max_length=50, null=True, blank=True)
	nu_emis = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	nss = models.CharField(max_length=50, null=True, blank=True)
	nu_eleitoral = models.CharField(max_length=50, null=True, blank=True)
	data_emissao_eleitoral = models.DateField(verbose_name='Data Emissao Eleitoral', null=True, blank=True)
	nu_bi = models.CharField(max_length=50, null=True, blank=True)
	data_validade_bi = models.DateField(verbose_name='Data Validade BI', null=True, blank=True)
	nu_conducao = models.CharField(max_length=50, null=True, blank=True)
	tipo_conducao = models.CharField(max_length=50, null=True, blank=True)
	data_validade_conducao = models.DateField(verbose_name='Data Validade Carta Conducao', null=True, blank=True)
	nome_pai = models.CharField(max_length=100, null=True, blank=True)
	nome_mae = models.CharField(max_length=100, null=True, blank=True)
	code_vendor = models.CharField(max_length=100, null=True, blank=True)
	controlo_ativo = models.CharField(choices=[('Ativo','Ativo'),('Não Exercício','Não Exercício'),('Saída Definitiva','Saída Definitiva')], max_length=40,default='Ativo')

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	def getidade(self):
		if self.data_nascimento:
			return datetime.date.today().year - self.data_nascimento.year
		else:
			return 0

	def getImagemPessoal(self):
		imagem = ImagemPessoal.objects.get(pessoa=self)
		return imagem.dados

	def getColocacao(self):
		objects = Ficha_colocacao.objects.filter(funcionario=self,data_fim__isnull=True).order_by('-data_inicio').last() 
		return objects

	def getContratacao(self):
		objects = Ficha_contratacao.objects.filter(funcionario=self,data_fim__gte=now).exclude(controlo_estado='Desabilitar').last() 
		return objects

	def getPermanente(self):
		objects = Ficha_permanente.objects.filter(funcionario=self,data_fim__isnull=True).exclude(controlo_estado='Desabilitar').last() 
		return objects

	def getFNE(self):
		objects = Ficha_nao_exercicio.objects.filter(funcionario=self).exclude(controlo_estado='Desabilitar').filter(Q(data_fim__isnull=True)|Q(data_fim__gt=date.today())).last() 
		return objects
	def getFSD(self):
		objects = Ficha_saida_definitiva.objects.filter(funcionario=self).exclude(controlo_estado='Desabilitar').order_by('-data_saida').first() 
		return objects
	

	class Meta:
		db_table = 'sgrh"."gfuncionarios'

	def __str__(self):
		template = '{0.nome}, {0.id_sigap}'
		return template.format(self)


# Model for arquivos
class ImagemPessoal(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	pessoa = models.OneToOneField(Funcionarios, on_delete=models.CASCADE,related_name="imagemfuncionario")
	dados = models.TextField()
	class Meta:
		db_table = 'arquivos"."binario_funcionario'  # Note the schema and table name



class Tipo_colocacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    controlo_estado = models.CharField(max_length=50, null=True, blank=True)

    inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
    alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

    class Meta:
        db_table = 'sgrh"."tipo_colocacao'

    def __str__(self):
        template = '{0.tipo} '
        return template.format(self)





class Ficha_colocacao(models.Model):
	id_colocacao = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE,related_name='colocacaoFuncionario')
	dg = models.ForeignKey('unidade_ministerio.Direcao_geral', on_delete=models.CASCADE,null=True)
	dn = models.ForeignKey('unidade_ministerio.Direcao_nacional', on_delete=models.CASCADE,null=True)
	dep = models.ForeignKey('unidade_ministerio.Departamento', on_delete=models.CASCADE,null=True)
	sec = models.ForeignKey('unidade_ministerio.Seccao', on_delete=models.CASCADE,null=True)
	local_trabalho = models.ForeignKey(Gdivisao_administrativa_municipio, on_delete=models.CASCADE)
	tipo_colocacao = models.ForeignKey(Tipo_colocacao, on_delete=models.CASCADE)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)
	controlo_estado = models.CharField(max_length=50, null=True, blank=True)

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)

	class Meta:
		db_table = 'sgrh"."colocacao'

	def __str__(self):
		template = '{0.funcionario}'
		return template.format(self)





# views

class ListaFuncionarioCompleto(models.Model):
	id = models.UUIDField(primary_key=True)
	nome = models.CharField(max_length=225, null=True, blank=True)
	sexo = models.CharField(choices=[('Masculino','Masculino'),('Feminino','Feminino')], max_length=15,default='Masculino')
	id_sigap = models.CharField(max_length=30, null=True, blank=True)
	id_grp = models.CharField(max_length=50, verbose_name='Id GRP', null=True, blank=True)
	data_nascimento = models.DateField(verbose_name='Data de Nascimento',default='1970-01-01')
	lugar_nascimento = models.CharField(max_length=50, null=True, blank=True)
	nu_telemovel = models.CharField(max_length=50, null=True, blank=True)
	nu_emis = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	nss = models.CharField(max_length=50, null=True, blank=True)
	nu_eleitoral = models.CharField(max_length=50, null=True, blank=True)
	data_emissao_eleitoral = models.DateField(verbose_name='Data Emissao Eleitoral', null=True, blank=True)
	nu_bi = models.CharField(max_length=50, null=True, blank=True)
	data_validade_bi = models.DateField(verbose_name='Data Validade BI', null=True, blank=True)
	nu_conducao = models.CharField(max_length=50, null=True, blank=True)
	tipo_conducao = models.CharField(max_length=50, null=True, blank=True)
	data_validade_conducao = models.DateField(verbose_name='Data Validade Carta Conducao', null=True, blank=True)
	nome_pai = models.CharField(max_length=100, null=True, blank=True)
	nome_mae = models.CharField(max_length=100, null=True, blank=True)
	code_vendor = models.CharField(max_length=100, null=True, blank=True)
	controlo_ativo = models.CharField(choices=[('Ativo','Ativo'),('Não Exercício','Não Exercício'),('Saída Definitiva','Saída Definitiva')], max_length=40,default='Ativo')

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)
	dados_imajen = models.TextField()
	idade = models.IntegerField()


	class Meta:
		managed = False
		db_table = 'sgrh"."viewlistafuncionariofompleto'

	

class ListaFuncionarioCompleto1(models.Model):
	id = models.UUIDField(primary_key=True)
	nome = models.CharField(max_length=225, null=True, blank=True)
	sexo = models.CharField(choices=[('Masculino','Masculino'),('Feminino','Feminino')], max_length=15,default='Masculino')
	id_sigap = models.CharField(max_length=30, null=True, blank=True)
	id_grp = models.CharField(max_length=50, verbose_name='Id GRP', null=True, blank=True)
	data_nascimento = models.DateField(verbose_name='Data de Nascimento',default='1970-01-01')
	lugar_nascimento = models.CharField(max_length=50, null=True, blank=True)
	nu_telemovel = models.CharField(max_length=50, null=True, blank=True)
	nu_emis = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	nss = models.CharField(max_length=50, null=True, blank=True)
	nu_eleitoral = models.CharField(max_length=50, null=True, blank=True)
	data_emissao_eleitoral = models.DateField(verbose_name='Data Emissao Eleitoral', null=True, blank=True)
	nu_bi = models.CharField(max_length=50, null=True, blank=True)
	data_validade_bi = models.DateField(verbose_name='Data Validade BI', null=True, blank=True)
	nu_conducao = models.CharField(max_length=50, null=True, blank=True)
	tipo_conducao = models.CharField(max_length=50, null=True, blank=True)
	data_validade_conducao = models.DateField(verbose_name='Data Validade Carta Conducao', null=True, blank=True)
	nome_pai = models.CharField(max_length=100, null=True, blank=True)
	nome_mae = models.CharField(max_length=100, null=True, blank=True)
	code_vendor = models.CharField(max_length=100, null=True, blank=True)
	controlo_ativo = models.CharField(choices=[('Ativo','Ativo'),('Não Exercício','Não Exercício'),('Saída Definitiva','Saída Definitiva')], max_length=40,default='Ativo')

	inserido_em = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	inserido_por = models.CharField(max_length=50, verbose_name='Inserido por', null=True, blank=True)
	alterado_em = models.DateTimeField(auto_now_add=False,null=True,blank=True)
	alterado_por = models.CharField(max_length=50, verbose_name='Alterado por', null=True, blank=True)
	dados_imajen = models.TextField()
	idade = models.IntegerField()
	tipo_funcionario = models.CharField(max_length=100, null=True, blank=True)
	data_inicio = models.DateField(verbose_name='Data Inicio', null=True, blank=True)
	data_fim = models.DateField(verbose_name='Data Fim', null=True, blank=True)
	categoria_cargo = models.CharField(max_length=100, null=True, blank=True)
	unidade = models.CharField(max_length=100, null=True, blank=True)
	local_trabalho = models.CharField(max_length=100, null=True, blank=True)


	class Meta:
		managed = False
		db_table = 'sgrh"."viewlistafuncionariocompleto'

	

