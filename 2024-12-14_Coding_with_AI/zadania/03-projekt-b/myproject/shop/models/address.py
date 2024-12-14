from django.db import models
from django.utils.translation import gettext as _


class AddressType(models.TextChoices):
    BILLING = 'billing', _('Billing')
    SHIPPING = 'shipping', _('Shipping')


class Address(models.Model):
    customer = models.ForeignKey(verbose_name=_('Customer'), to='shop.Customer', on_delete=models.CASCADE)
    type = models.CharField(verbose_name=_('Type'), choices=AddressType, max_length=20, null=True, blank=True, default=None)
    street = models.CharField(verbose_name=_('Street'), max_length=255, null=True, blank=True, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=100, null=False, blank=False)
    postcode = models.CharField(verbose_name=_('Postcode'), max_length=20, null=True, blank=True, default=None)
    region = models.CharField(verbose_name=_('Region'), max_length=100, null=True, blank=True, default=None)
    country = models.CharField(verbose_name=_('Country'), max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return _(f'{self.type} address for {self.customer}')

    class Meta:
        app_label = 'shop'
        ordering = ['customer']
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
