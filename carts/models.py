from django.db import models
from django.utils.translation import gettext_lazy as _

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
    user = models.OneToOneField(User, models.CASCADE, verbose_name=_('user'))
    status = models.PositiveSmallIntegerField(verbose_name=_('status'))


class Cart(User):
    class Meta:
        proxy = True

    @property
    def card_user(self):
        return self.get_full_name()

    @property
    def paid_orders(self):
        return None

    @property
    def unpaid_orders(self):
        return None


class AccommodationOrder(OrderBace):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'orders', verbose_name=_('accommodation'))
    date_price = models.ManyToManyField(AccommodationDatePrice,
                                        related_name='accommodation_orders', verbose_name=_('accommodation'))

    class Meta:
        db_table = 'accommodation_order'
        verbose_name = 'accommodation order'
        verbose_name_plural = 'accommodation orders'

    def order_price(self):
        pass

    def start_date_reserve(self):
        pass

    def end_date_reserve(self):
        pass


class HotelRoomOrder(OrderBace):
    hotel = models.ForeignKey(Place, models.CASCADE, 'orders', verbose_name=_('hotel'))
    date_prices = models.ManyToManyField(HotelRoomDatePrice, 'hotel_room_orders', verbose_name=_('date prices'))

    class Meta:
        db_table = 'hotel_room_order'
        verbose_name = _('hotel room order')
        verbose_name_plural = _('hotel room orders')

    def order_price(self):
        pass

    def start_date_reserve(self):
        pass

    def end_date_reserve(self):
        pass
