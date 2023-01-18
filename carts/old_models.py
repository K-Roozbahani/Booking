from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum, Count, Max, Min
from users.models import User
from places.models import PlaceDatePrice, Accommodation, Place
from flying.models import FlyTicket


class CardManager(models.Manager):
    pass


class OrderBace(models.Model):
    STATUS_CANCEL = 0
    STATUS_UNPAID = 1
    STATUS_PAID = 2
    STATUS_PAYMENT_FAILED = 3
    STATUS = ((STATUS_CANCEL, _('cancel')), (STATUS_UNPAID, _('unpaid')),
              (STATUS_PAID, _('paid')), (STATUS_PAYMENT_FAILED, _('payment failed')))
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('user'))
    status = models.PositiveSmallIntegerField(verbose_name=_('status'), choices=STATUS, default=0)
    create_date = models.DateTimeField(verbose_name=_('create_date'), auto_now_add=True)
    update_date = models.DateTimeField(verbose_name=_('update date'), auto_now=True)

    class Meta:
        abstract = True


class PlaceOrder(OrderBace):
    date_prices = models.ManyToManyField(PlaceDatePrice,
                                         related_name='place_orders', verbose_name=_('date price'))

    class Meta:
        db_table = 'place_orders'
        verbose_name = 'place order'
        verbose_name_plural = 'place orders'

    @property
    def number_nights(self):
        return self.date_prices.count()

    @property
    def order_price(self):
        order_prices_sum = self.date_prices.aggregate(Sum('price'))
        extra_items_price = self.date_price.aggregate(Sum('extra_price'))
        return order_prices_sum['price_sum']

    @property
    def start_date_reserve(self):
        order_date_minimum = self.date_prices.aggregate(start_date=Min('date'))
        return order_date_minimum['start_date']

    @property
    def end_date_reserve(self):
        order_date_maximum = self.date_prices.aggregate(end_date=Max('date'))
        return order_date_maximum['end_date']

    def is_free(self):
        reserve_date = self.date_prices.filter(date__gte=self.start_date_reserve,
                                               date__lte=self.end_date_reserve,
                                               is_reserve=True).count()
        if reserve_date == 0:
            return True
        else:
            return False

    def get_order_detail(self):
        detail_data = {'user': self.user__username, 'number_nights': self.number_nights,
                       'start_date': self.start_date_reserve, 'end_date': self.end_date_reserve,
                       'price': self.order_price}
        return detail_data


class Cart(User):
    class Meta:
        proxy = True

    @property
    def card_user(self):
        return self.user__username

    @property
    def paid_orders(self):
        return None

    @property
    def unpaid_orders(self):
        return None


# class FlyTicketOrder(OrderBace):
#
