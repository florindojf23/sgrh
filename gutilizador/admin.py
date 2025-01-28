from django.contrib import admin
from .models import Profile,AuditLogin,Funcionario_user
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User,Group
from django.contrib.auth.admin import UserAdmin

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
admin.site.register(Profile, ProfileAdmin)

class AuditLoginResource(resources.ModelResource):
    class Meta:
        model = AuditLogin
class AuditLoginAdmin(ImportExportModelAdmin):
    resource_class = AuditLoginResource
admin.site.register(AuditLogin, AuditLoginAdmin)

# class AuditSystemResource(resources.ModelResource):
#     class Meta:
#         model = AuditSystem
# class AuditSystemAdmin(ImportExportModelAdmin):
#     resource_class = AuditSystemResource
# admin.site.register(AuditSystem, AuditSystemAdmin)

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
class GroupAdmin(ImportExportModelAdmin):
    resource_class = GroupResource

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

admin.site.register(Funcionario_user)