from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum, Count, Max, Min
from users.models import User
from places.models import PlaceDatePrice, Accommodation, Place
from flying.models import FlyTicket


class Order(models.Model):
    STATUS_CANCEL = 0
    STATUS_UNPAID = 1
    STATUS_PAID = 2
    STATUS_PAYMENT_FAILED = 3
    STATUS = ((STATUS_CANCEL, _('cancel')), (STATUS_UNPAID, _('unpaid')),
              (STATUS_PAID, _('paid')), (STATUS_PAYMENT_FAILED, _('payment failed')))
    user = models.ForeignKey(User, models.CASCADE, related_name='orders', verbose_name=_('user'))
    status = models.PositiveSmallIntegerField(verbose_name=_('status'), choices=STATUS, default=0)
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)
    total_price = models.FloatField(verbose_name=_('total price'), null=True, blank=True)


class PlaceItem(models.Model):
    order = models.OneToOneField(Order, models.CASCADE, related_name='place_item')
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)
    items = models.ManyToManyField(FlyTicket, related_name='place_items', blank=True, null=True)

    class Meta:
        db_table = 'place_items'
        verbose_name = 'place item'
        verbose_name_plural = 'place items'

        def get_price(self):
            price = self.items.all().aggregate(Sum('price'))
            items = self.items.all()
            extra_price = 0
            for item in items:
                item.order_check()
                extra_price = item.extra_price
            return price + extra_price


class FlyItem(models.Model):
    order = models.OneToOneField(Order, models.CASCADE, related_name='fly_item')
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)
    items = models.ManyToManyField(PlaceDatePrice, related_name='fly_items', blank=True, null=True)

    class Meta:
        db_table = 'fly_items'
        verbose_name = 'fly item'
        verbose_name_plural = 'fly items'

    def get_price(self):
        return self.items.all().aggregate(Sum('price'))
