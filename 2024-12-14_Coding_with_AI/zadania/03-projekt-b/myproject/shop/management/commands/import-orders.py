from django.core.management.base import BaseCommand
import json
from shop.models import Customer, Product, Order


class Command(BaseCommand):
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        filename = kwargs['file']
        with open(filename, mode='rt') as file:
            data = json.load(file)

        for values in data:
            customer = Customer.objects.get(email=values.pop('customer'))
            product = Product.objects.get(name=values.pop('product'))
            order = Order.objects.create(customer=customer)
            order.product.set([product])

        self.stdout.write(self.style.SUCCESS('Successfully imported products'))


