from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    ean13 = models.CharField(verbose_name=_('EAN-13'), max_length=13, null=False, blank=False, default='')
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=False, blank=False, default='')
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2, null=False, blank=False, default=0.00)

    def __str__(self):
        return _(f'Product {self.name}')

    class Meta:
        app_label = 'shop'
        ordering = ['name']
        verbose_name = _('Product')
        verbose_name_plural = _('Product')

