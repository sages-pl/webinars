from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    firstname = models.CharField(verbose_name=_('Firstname'), max_length=100, null=False, blank=False)
    lastname = models.CharField(verbose_name=_('Lastname'), max_length=100, null=False, blank=False, db_index=True)
    birthdate = models.DateField(verbose_name=_('Birthdate'), null=True, blank=True, default=None)
    gender = models.CharField(verbose_name=_('Gender'), max_length=10, null=True, blank=True, default=None)
    tax_number = models.CharField(verbose_name=_('Tax Number'), max_length=15, null=True, blank=True, default=None)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True, default=None)
    phone = models.CharField(verbose_name=_('Phone'), max_length=20, null=True, blank=True, default=None)

    def __str__(self):
        return _(f'{self.firstname} {self.lastname}')

    class Meta:
        app_label = 'shop'
        ordering = ['lastname', 'firstname']
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
