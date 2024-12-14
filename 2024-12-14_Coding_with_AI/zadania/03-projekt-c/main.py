from unittest import TestCase


class Dragon:
    def __init__(self, name, /):
        if name == '':
            raise TypeError('Name cannot be empty')
        self.name = name


class NameTest(TestCase):
    def test_name_positional(self):
        dragon = Dragon('Name')
        self.assertEqual(dragon.name, 'Name')

    def test_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Name')  # noqa

    def test_name_default(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_name_empty(self):
        with self.assertRaises(TypeError):
            Dragon('')

