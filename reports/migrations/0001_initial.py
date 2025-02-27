# Generated by Django 5.1 on 2024-11-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuncionarioPivotCASEXO',
            fields=[
                ('controlo_ativo', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('masculino', models.IntegerField()),
                ('feminino', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'sgrh"."view_statis_controlo_ativo_sexo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuncionarioPivotTFSEXO',
            fields=[
                ('tipo_funcionario', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('masculino', models.IntegerField()),
                ('feminino', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'sgrh"."view_statis_tipo_funcionario_sexo',
                'managed': False,
            },
        ),
    ]
