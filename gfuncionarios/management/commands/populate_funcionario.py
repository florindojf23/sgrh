import random
import uuid
from django.core.management.base import BaseCommand
from gfuncionarios.models import Funcionarios
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the Funcionarios model with dummy data.'

    def handle(self, *args, **kwargs):
        # Define some example values
        sexos = ['Masculino', 'Feminino']
        controlo_ativo_choices = ['Ativo', 'Não Exercício', 'Saída Definitiva']
        tipo_conducao_choices = ['A', 'B', 'C', 'D', None]

        # Number of records to create
        num_records = 50000

        # Create dummy data
        for _ in range(num_records):
            nome = fake.name()
            sexo = random.choice(sexos)
            id_sigap = fake.uuid4()[:8]  # Random UUID shortened
            id_grp = fake.uuid4()[:10]   # Random UUID shortened
            data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
            lugar_nascimento = fake.city()
            nu_telemovel = fake.phone_number()
            nu_emis = fake.uuid4()[:8]
            email = fake.email()
            nss = fake.uuid4()[:6]
            nu_eleitoral = fake.uuid4()[:8]
            data_emissao_eleitoral = fake.date_between(start_date='-10y', end_date='today')
            nu_bi = fake.uuid4()[:10]
            data_validade_bi = fake.date_between(start_date='today', end_date='+10y')
            nu_conducao = fake.uuid4()[:8]
            tipo_conducao = random.choice(tipo_conducao_choices)
            data_validade_conducao = fake.date_between(start_date='today', end_date='+10y')
            nome_pai = fake.name_male()
            nome_mae = fake.name_female()
            code_vendor = fake.uuid4()[:6]
            controlo_ativo = random.choice(controlo_ativo_choices)

            inserido_em = make_aware(fake.date_time_between(start_date='-2y', end_date='now'))
            inserido_por = fake.user_name()
            alterado_em = inserido_em + timedelta(days=random.randint(1, 365))
            alterado_por = fake.user_name()

            # Create and save the record
            funcionario = Funcionarios(
                id=uuid.uuid4(),
                nome=nome,
                sexo=sexo,
                id_sigap=id_sigap,
                id_grp=id_grp,
                data_nascimento=data_nascimento,
                lugar_nascimento=lugar_nascimento,
                nu_telemovel=nu_telemovel,
                nu_emis=nu_emis,
                email=email,
                nss=nss,
                nu_eleitoral=nu_eleitoral,
                data_emissao_eleitoral=data_emissao_eleitoral,
                nu_bi=nu_bi,
                data_validade_bi=data_validade_bi,
                nu_conducao=nu_conducao,
                tipo_conducao=tipo_conducao,
                data_validade_conducao=data_validade_conducao,
                nome_pai=nome_pai,
                nome_mae=nome_mae,
                code_vendor=code_vendor,
                controlo_ativo=controlo_ativo,
                inserido_em=inserido_em,
                inserido_por=inserido_por,
                alterado_em=alterado_em,
                alterado_por=alterado_por,
            )
            funcionario.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {num_records} Funcionarios records'))
