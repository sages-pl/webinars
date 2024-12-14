from django.db import models
from django.utils.translation import gettext as _


class Order(models.Model):
    customer = models.ForeignKey(verbose_name=_('Customer'), to='shop.Customer', on_delete=models.CASCADE, null=False, blank=False, default=None)
    product = models.ManyToManyField(verbose_name=_('Product'), to='shop.Product', blank=False, default=None)

    def __str__(self):
        return _(f'Order from {self.customer}')

    class Meta:
        app_label = 'shop'
        ordering = ['customer']
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
