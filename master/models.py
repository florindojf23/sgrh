from django.db import models
import uuid

# Create your models here.
class Core(models.Model):
    sysname = models.CharField(max_length=100)
    syssigla = models.CharField(max_length=10, blank=True, null=True)
    owner = models.CharField(max_length=100,blank=True,null=True)
    logo = models.ImageField(upload_to='Owner',blank=True,null=True)
    is_active = models.BooleanField(default=False)
    nu_kontaktu = models.CharField(max_length=10, blank=True, null=True)
    enderesu = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'sgrh"."core'

    def __str__(self):
        return self.sysname 
    

class Pais(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sigla = models.CharField(max_length=10, blank=True, null=True)
    nome = models.CharField(max_length=100,blank=True,null=True)
    logo = models.ImageField(upload_to='Pais',blank=True,null=True)

    class Meta:
        db_table = 'sgrh"."pais'

    def __str__(self):
        return self.nome 
    




