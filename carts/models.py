from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum, Count, Max, Min
from users.models import User
from places.models import AccommodationDatePrice, Accommodation, Place, HotelRoomDatePrice


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


class PlaceOrderBace(OrderBace):
    class Meta:
        abstract = True

    @property
    def number_nights(self):
        return self.date_prices.count()

    @property
    def order_price(self):
        order_prices_sum = self.date_prices.aggregate(Sum('price'))
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

    # def save(self, *args, **kwargs):
    #     if self.is_free():
    #         super(PlaceOrderBace, self).save(*args, **kwargs)
    #     else:
    #         raise FileExistsError('It is reserved during this period')


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


class AccommodationOrder(PlaceOrderBace):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'orders', verbose_name=_('accommodation'))
    date_prices = models.ManyToManyField(AccommodationDatePrice,
                                         related_name='accommodation_orders', verbose_name=_('date price'))

    class Meta:
        db_table = 'accommodation_orders'
        verbose_name = 'accommodation order'
        verbose_name_plural = 'accommodation orders'


class HotelRoomOrder(OrderBace):
    hotel = models.ForeignKey(Place, models.CASCADE, 'hotel_room_order', verbose_name=_('hotel'))
    date_prices = models.ManyToManyField(HotelRoomDatePrice, 'hotel_room_orders', verbose_name=_('date prices'))

    class Meta:
        db_table = 'hotel_room_order'
        verbose_name = _('hotel room order')
        verbose_name_plural = _('hotel room orders')
