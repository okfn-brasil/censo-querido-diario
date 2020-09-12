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
                cities = f.readlines()
                for city in cities[1:]:
                    elements = city.split(',')
                    if elements[5] == '':
                        elements[5] = None
                    obj = {
                    'ibge': int(elements[0]),
                    'ibge7': int(elements[1]),
                    'uf': elements[2],
                    'municipio': elements[3],
                    'regiao': elements[4],
                    'populacao_2010': elements[5],
                    'capital': elements[6] == 'Capital',
                    }
                    Municipio(**obj).save()
            self.stdout.write(self.style.SUCCESS('Successfully read data'))
        else:
            raise CommandError('Enter the file path: python manage.py read_data --file data.csv')
