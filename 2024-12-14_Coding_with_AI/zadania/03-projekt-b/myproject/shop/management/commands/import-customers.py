from django.core.management.base import BaseCommand
import json
from shop.models import Customer


class Command(BaseCommand):
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        filename = kwargs['file']
        with open(filename, mode='rt') as file:
            data = json.load(file)
        customers = [Customer(**values) for values in data]
        Customer.objects.bulk_create(customers)
        self.stdout.write(self.style.SUCCESS('Successfully imported products'))


