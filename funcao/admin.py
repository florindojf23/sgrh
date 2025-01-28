from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export import resources

class Relacao_juridica_empregoResource(resources.ModelResource):
    class Meta:
        model = Relacao_juridica_emprego
class Relacao_juridica_empregoAdmin(ImportExportModelAdmin):
    resource_class = Relacao_juridica_empregoResource
admin.site.register(Relacao_juridica_emprego, Relacao_juridica_empregoAdmin)


class Tipo_alteracao_fichaResource(resources.ModelResource):
    class Meta:
        model = Tipo_alteracao_ficha
class Tipo_alteracao_fichaAdmin(ImportExportModelAdmin):
    resource_class = Tipo_alteracao_fichaResource
admin.site.register(Tipo_alteracao_ficha, Tipo_alteracao_fichaAdmin)