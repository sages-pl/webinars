from datetime import date
from django.test import TestCase
from shop.models import Customer, Address, Product, Order


class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            firstname='Jan',
            lastname='Kowalski',
            birthdate=date(2000, 1, 2),
            gender='M',
            tax_number='1234567890',
            email='jan.kowalski@example.com',
            phone='123456789'
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.firstname, 'Jan')
        self.assertEqual(self.customer.lastname, 'Kowalski')

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'Jan Kowalski')


class AddressModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            firstname='Jan',
            lastname='Kowalski'
        )
        self.address = Address.objects.create(
            customer=self.customer,
            type='Billing',
            street='Main St',
            city='Warsaw',
            postcode='00-001',
            region='Mazowieckie',
            country='Poland'
        )

    def test_address_creation(self):
        self.assertEqual(self.address.street, 'Main St')

    def test_address_str(self):
        self.assertEqual(str(self.address), 'Billing address for Jan Kowalski')


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            ean13='1234567890123',
            name='Product 1',
            price=100.0
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Product 1')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Product Product 1')


class OrderModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            firstname='Jan',
            lastname='Kowalski'
        )
        self.product1 = Product.objects.create(
            ean13='1234567890123',
            name='Product 1',
            price=100.0
        )
        self.product2 = Product.objects.create(
            ean13='1234567890124',
            name='Product 2',
            price=200.0
        )
        self.order = Order.objects.create(
            customer=self.customer
        )
        self.order.product.set([self.product1, self.product2])

    def test_order_creation(self):
        self.assertEqual(list(self.order.product.all()), [self.product1, self.product2])

    def test_order_str(self):
        self.assertEqual(str(self.order), 'Order from Jan Kowalski')
