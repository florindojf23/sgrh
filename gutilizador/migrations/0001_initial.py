# Generated by Django 5.1 on 2025-01-27 04:06

import django.core.validators
import django.db.models.deletion
import master.utils_upload
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gfuncionarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestao',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_gestao', models.CharField(max_length=100)),
                ('sigla_gestao', models.CharField(max_length=100)),
                ('controlo_estado', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
            options={
                'db_table': 'sgrh"."gestao',
            },
        ),
        migrations.CreateModel(
            name='AuditLogin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('login_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audituserlogin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sgrh"."gauditlogin',
            },
        ),
        migrations.CreateModel(
            name='Funcionario_user',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('funcionario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gfuncionarios.funcionarios')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_funcionario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sgrh"."auth_user_funcionario',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('pob', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fatin Moris')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Data Moris')),
                ('sex', models.CharField(blank=True, choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=master.utils_upload.upload_profile, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])], verbose_name='Upload Imajen')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sgrh"."profile',
            },
        ),
    ]
