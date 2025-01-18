import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from atores.models import Ator


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo com atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
    
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Ator.objects.create(
                    nome=name,
                    nascimento=birthday,
                    nacionalidade=nationality,
                )

        self.stdout.write(self.style.SUCCESS('ATORES CADASTRADOS COM SUCESSO!'))
