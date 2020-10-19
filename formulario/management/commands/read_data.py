import csv
from django.core.management.base import BaseCommand, CommandError
from formulario.models import Municipio

class Command(BaseCommand):
    help = 'Read a base of Brazilian municipalities'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            help='Place the path for the file with data from municipalities.',
        )

    def handle(self, *args, **options):
        if options['file']:
            with open(options['file'], 'r') as f:
                cities = csv.DictReader(f)
                cities_list = []

                for city in cities:
                    kwargs = {
                        'ibge': int(city['IBGE']),
                        'ibge7': int(city['IBGE7']),
                        'uf': city['UF'],
                        'municipio': city['Município'],
                        'regiao': city['Região'],
                        'populacao_2010': None if city['População 2010'] == '' else city['População 2010'],
                        'capital': city['Capital'] == 'Capital',
                    }
                    cities_list.append(Municipio(**kwargs))

                Municipio.objects.bulk_create(cities_list)
            self.stdout.write(self.style.SUCCESS('Successfully read data'))
        else:
            raise CommandError('Enter the file path: python manage.py read_data --file data.csv')
