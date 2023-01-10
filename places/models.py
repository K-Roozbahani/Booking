import datetime

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from users.models import User

CURRENCY_IRR = 1
CURRENCY_USD = 2
CURRENCY_EUR = 3
CURRENCY_CAD = 4
CHOICES_CURRENCY = ((CURRENCY_IRR, 'IRR'), (CURRENCY_USD, 'USD'), (CURRENCY_EUR, 'EUR'), (CURRENCY_CAD, 'CAD'))


class DateFilterManager(models.Manager):
    def get_queryset(self):
        now = timezone.now().date()
        next_date = now
        next_date.month += 2
        next_date.day = 1
        return super(DateFilterManager, self).get_queryset().filter(date__gte=now, date__lt=next_date)


class Holiday(models.Model):
    date = models.DateField(verbose_name=_('date'))
    description = models.CharField(verbose_name=_('description'), default=_('end weak'), max_length=64)
    last_update = models.DateTimeField(verbose_name=_('last_update'), auto_now=True, is_reserve=False)
    objects = models.Manager()
    holiday_list = DateFilterManager()

    @classmethod
    def holidays_list(cls):
        holidays = cls.holiday_list.all()
        timezone_list = [holiday.date for holiday in holidays]
        return timezone_list

    class Meta:
        db_table = 'holidays'
        verbose_name = _('holiday')
        verbose_name_plural = _('holidays')


class BaseModel(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=64)
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    create_time = models.DateTimeField(verbose_name=_('date join'), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_('last modify'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class DatePrice(models.Model):
    currency = models.PositiveIntegerField(verbose_name=_('currency'), choices=CHOICES_CURRENCY)
    is_reserve = models.BooleanField(verbose_name=_('is reserve'), default=False)
    date = models.DateField(verbose_name=_('date'))
    price = models.FloatField(verbose_name=_('price'))
    objects = models.Manager()
    date_price_list = DateFilterManager()

    def is_holiday(self):
        if self.date in Holiday.holidays_list():
            return True
        else:
            return False

    def get_price_list(self):
        return self.date_price_list.all()

    def auto_set_price(self, base_price, vacation_price, *args, **kwargs):
        now = timezone.now().date()
        next_date = now
        next_date.month += 2
        next_date.day = 1
        date_prices = []
        while now < next_date:
            date_price = self
            date_price.date = now
            if date_price.is_holiday():
                date_price.price = vacation_price
            else:
                date_price.price = base_price
            date_prices.append(date_price)
        try:
            self.objects.bulk_create(date_prices)
        except:
            print('sorry cant create date_prices')

    def __str__(self):
        return str(self.date) + ' ' + str(self.price)  # + str(self.currency)

    class Meta:
        abstract = True


class Attribute(BaseModel):
    description = models.CharField(verbose_name=_('description'), max_length=64, blank=True, null=True)

    class Meta:
        abstract = True


class Location(models.Model):
    country = models.CharField(verbose_name=_('country'), max_length=64)
    province = models.CharField(verbose_name=_('province'), max_length=64)
    city = models.CharField(verbose_name=_('city'), max_length=64)

    def __str__(self):
        return str(self.country) + ' ' + str(self.city)

    class Meta:
        db_table = 'location'
        verbose_name = _('location')
        verbose_name_plural = _('locations')


class LocationType(BaseModel):
    class Meta:
        db_table = 'location_type'
        verbose_name = _('location type')
        verbose_name_plural = _('locations type')


class Place(BaseModel):
    HOTEL_TYPE = 1
    MOTEL_TYPE = 2
    HOSTEL_TYPE = 3
    VILLA_TYPE = 4
    HOLIDAY_CAMP_TYPE = 5
    ROOM_TYPE = 6
    PLACE_TYPE = ((HOSTEL_TYPE, _('hotel')),
                  (MOTEL_TYPE, _('motel')),
                  (HOSTEL_TYPE, _('hostel')),
                  (VILLA_TYPE, _('vila')),
                  (HOLIDAY_CAMP_TYPE, _('holiday camp')),
                  (ROOM_TYPE, _('room'))
                  )
    owner = models.ForeignKey(User, models.CASCADE,
                              related_name='Accommodation', verbose_name=_(_('Accommodation'))
                              )
    location = models.ForeignKey(Location, models.DO_NOTHING, related_name='place_location',
                                 verbose_name=_('location'))
    location_type = models.ManyToManyField(LocationType, related_name='accommodation',
                                           verbose_name=_('location type'))
    address = models.TextField(verbose_name=_("address"))
    place_type = models.PositiveSmallIntegerField(verbose_name=_('place_type'), choices=PLACE_TYPE)
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)

    def __str__(self):
        return str(self.title) + ' cod: ' + str(self.id)

    class Meta:
        db_table = 'Place'
        verbose_name = _('Place')
        verbose_name_plural = _('Places')


# class ExtraItem(BaseModel):
#     price = models.FloatField(verbose_name=_('price'), default=0)
#     place = models.ForeignKey(Place, models.CASCADE, related_name='options', verbose_name=_('place'))
#
#     class Meta:
#         db_table = 'extra_items'
#         verbose_name = _('extra item')
#         verbose_name_plural = _('extra items')


class AccommodationAttribute(Attribute):
    class Meta:
        db_table = 'accommodation_attributes'
        verbose_name = _('accommodation attribute')
        verbose_name_plural = _('accommodation attributes')


# class HotelRoomAttribute(Attribute):
#     class Meta:
#         db_table = 'hotel_room_attributes'
#         verbose_name = _('hotel room attribute')
#         verbose_name_plural = _('hotels room attribute')


class AccommodationRoomAttribute(Attribute):
    class Meta:
        db_table = 'room_attributes'
        verbose_name = _('accommodation room attribute')
        verbose_name_plural = _('accommodation room attributes')


class RoomType(BaseModel, models.Model):
    class Meta:
        db_table = 'room_type'
        verbose_name = _('room type')
        verbose_name_plural = _('room types')


class AccommodationType(BaseModel):
    class Meta:
        db_table = 'accommodation_type'
        verbose_name = _('accommodation type')
        verbose_name_plural = _('accommodation types')


class Accommodation(BaseModel):
    place = models.ForeignKey(Place, models.DO_NOTHING, related_name='accommodation',
                              verbose_name=_('place'), blank=True, null=True)

    base_price = models.FloatField(verbose_name=_('base price'))

    currency = models.PositiveIntegerField(verbose_name=_('currency'), choices=CHOICES_CURRENCY)
    extra_person_price = models.FloatField(verbose_name=_('extra person price'))
    standard_capacity = models.IntegerField(verbose_name=_('standard capacity'))
    maximum_capacity = models.IntegerField(verbose_name=_('maximum capacity'))
    entry_time = models.TimeField(verbose_name=_('entry time'), default=datetime.time(12, 0, 0))
    exit_time = models.TimeField(verbose_name=_('exit time'), default=datetime.time(14, 0, 0))

    area_size = models.IntegerField(verbose_name=_('area size'), blank=True, null=True)
    accommodation_size = models.IntegerField(verbose_name=_('accommodation size'))
    is_charter = models.BooleanField(verbose_name=_('is charter'), default=True)

    accommodation_type = models.ManyToManyField(AccommodationType, related_name='accommodation',
                                                verbose_name=_('accommodation type'))
    attribute = models.ManyToManyField(AccommodationAttribute,
                                       related_name='accommodation', verbose_name=_('attribute'))
    description = models.TextField(verbose_name=_('description'))

    # extra_items = models.ManyToManyField(ExtraItem, related_name='accommodation', verbose_name=_('extra items'))

    class Meta:
        db_table = 'accommodation'
        verbose_name = _('accommodation')
        verbose_name_plural = _('accommodations')


class AccommodationRoom(BaseModel):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE,
                                      related_name='room', verbose_name=_('accommodation'),
                                      blank=True, null=True)
    size = models.IntegerField(verbose_name=_('size'), blank=True, null=True)
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)
    room_type = models.ForeignKey(RoomType, related_name='accommodation_room', verbose_name=_('room_type'),
                                  on_delete=models.CASCADE)
    attribute = models.ManyToManyField(AccommodationRoomAttribute, related_name='accommodation_room',
                                       verbose_name=_('attribute'))

    class Meta:
        db_table = 'accommodation_room'
        verbose_name = _('accommodation room')
        verbose_name_plural = _('accommodation rooms')


# class HotelRoom(BaseModel):
#     CURRENCY_IRR = 1
#     CURRENCY_USD = 2
#     CURRENCY_EUR = 3
#     CURRENCY_CAD = 4
#     CHOICES_CURRENCY = ((CURRENCY_IRR, 'IRR'), (CURRENCY_USD, 'USD'), (CURRENCY_EUR, 'EUR'), (CURRENCY_CAD, 'CAD'))
#     place = models.ForeignKey(Place, models.CASCADE, related_name='hotel_room', verbose_name=_('place'))
#     room_number = models.PositiveIntegerField(verbose_name=_('room number'))
#     size = models.IntegerField(verbose_name=_('size'))
#     description = models.TextField(verbose_name=_('description'), blank=True, null=True)
#     room_type = models.ForeignKey(RoomType, related_name='hotel_room', verbose_name=_('room_type'),
#                                   on_delete=models.CASCADE)
#     base_price = models.FloatField(verbose_name=_('bace price'), null=True, blank=True)
#     currency = models.PositiveIntegerField(verbose_name=_('currency'), choices=CHOICES_CURRENCY)
#     room_star = models.PositiveIntegerField(verbose_name=_('room star'), validators=[MaxValueValidator(5)], default=2)
#     capacity = models.PositiveSmallIntegerField(verbose_name=_('capacity'), default=2)
#     attribute = models.ManyToManyField(HotelRoomAttribute, 'hotel_room', verbose_name=_('attribute'))
#
#     def __str__(self):
#         return str(self.title)
#
#     class Meta:
#         db_table = 'hotel_room'
#         verbose_name = _('hotel_room')
#         verbose_name_plural = _('hotels_rooms')


class PlaceDatePrice(DatePrice):
    accommodation_number = models.PositiveIntegerField(verbose_name=_('accommodation_number'), default=1)
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'date_price', verbose_name=_('accommodation'))
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    person_numbers = models.PositiveIntegerField(verbose_name=_('person number'))
    extra_price = models.FloatField(verbose_name=_('extra price'), null=True, blank=True)

    class Meta:
        db_table = 'place_date_price'
        verbose_name = _('place date price')
        verbose_name_plural = _('place dates prices')

    def order_check(self):
        standard_capacity = self.accommodation__standard_capacity
        maximum_capacity = self.accommodation__maximum_capacity
        if self.person_numbers > maximum_capacity:
            return False
        elif self.person_numbers > standard_capacity:
            extra_number = int(self.person_numbers) - standard_capacity
            self.extra_price = self.accommodation__extera_person_price * extra_number
            return True
        else:
            return True

# class HotelRoomDatePrice(DatePrice):
#     room = models.ForeignKey(HotelRoom, models.CASCADE, 'date_price', verbose_name=_('accommodation'))
#
#     class Meta:
#         db_table = 'hotel_room_date_price'
#         verbose_name = _('hotel room date price')
#         verbose_name_plural = _('hotel rooms dates price')
