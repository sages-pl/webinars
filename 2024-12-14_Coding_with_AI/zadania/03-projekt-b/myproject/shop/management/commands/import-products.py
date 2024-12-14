from django.core.management.base import BaseCommand
import json
from shop.models import Product


class Command(BaseCommand):
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        filename = kwargs['file']
        with open(filename, mode='rt') as file:
            data = json.load(file)
        products = [Product(**values) for values in data]
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS('Successfully imported products'))


