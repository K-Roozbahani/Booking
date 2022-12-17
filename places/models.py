import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


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
    # currency = models.ForeignKey('Currency', models.CASCADE,
    #                              related_name=_('%(class)'), verbose_name=_('currency'))
    is_reserve = models.BooleanField(verbose_name=_('is reserve'), default=False)
    date = models.DateField(verbose_name=_('date'))
    price = models.FloatField(verbose_name=_('price'))

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

    location = models.ForeignKey(Location, models.DO_NOTHING, related_name='place',
                                 verbose_name=_('location'))
    address = models.TextField(verbose_name=_("address"))
    place_type = models.PositiveSmallIntegerField(verbose_name=_('place_type'), choices=PLACE_TYPE)
    description = models.TextField(verbose_name=_('description'))

    def __str__(self):
        return str(self.title) + ' cod: ' + str(self.id)

    class Meta:
        db_table = 'place'
        verbose_name = _('place')
        verbose_name_plural = _('places')


class Option(BaseModel):
    is_free = models.BooleanField(verbose_name=_('is free'), default=True)
    price = models.FloatField(verbose_name=_('price'), default=0)
    place = models.ForeignKey(Place, models.CASCADE, verbose_name=_('place'))

    class Meta:
        db_table = 'option'
        verbose_name = _('option')
        verbose_name_plural = _('options')


class LocationType(BaseModel):
    pass

    class Meta:
        db_table = 'location_type'
        verbose_name = _('location type')
        verbose_name_plural = _('locations type')


class RoomType(BaseModel, models.Model):
    pass

    class Meta:
        db_table = 'room_type'
        verbose_name = _('room type')
        verbose_name_plural = _('rooms type')


class AccommodationType(BaseModel):
    pass

    class Meta:
        db_table = 'accommodation_type'
        verbose_name = _('accommodation type')
        verbose_name_plural = _('accommodations type')


class Accommodation(BaseModel):

    place = models.ForeignKey(Place, models.DO_NOTHING, related_name='accommodation',
                              verbose_name=_('place'), blank=True, null=True)
    owner = models.ForeignKey(User, models.CASCADE,
                              related_name='Accommodation', verbose_name=_(_('Accommodation'))
                              )
    base_price = models.FloatField(verbose_name=_('base price'))
    extra_person_price = models.FloatField(verbose_name=_('extra person price'))
    standard_capacity = models.IntegerField(verbose_name=_('standard capacity'))
    maximum_capacity = models.IntegerField(verbose_name=_('maximum capacity'))
    entry_time = models.TimeField(verbose_name=_('entry time'), default=datetime.time(12, 0, 0))
    exit_time = models.TimeField(verbose_name=_('exit time'), default=datetime.time(14, 0, 0))

    area_size = models.IntegerField(verbose_name=_('area size'))
    build_size = models.IntegerField(verbose_name=_('build size'))
    is_charter = models.BooleanField(verbose_name=_('is charter'), default=True)
    location_type = models.ManyToManyField(LocationType, related_name='accommodation',
                                           verbose_name=_('location type'))
    accommodation_type = models.ManyToManyField(AccommodationType, related_name='accommodation',
                                                verbose_name=_('accommodation type'))
    description = models.TextField(verbose_name=_('description'))

    class Meta:
        db_table = 'accommodation'
        verbose_name = _('accommodation')
        verbose_name_plural = _('accommodations')


class Room(BaseModel):
    place = models.ForeignKey(Place, models.CASCADE, 'room', parent_link=True, verbose_name=_('room'))
    accommodation = models.ForeignKey(Accommodation, models.CASCADE,
                                      related_name='room', verbose_name=_('accommodation'),
                                      blank=True, null=True)
    size = models.IntegerField(verbose_name=_('size'))
    description = models.TextField(verbose_name=_('description'))
    room_type = models.ManyToManyField(RoomType, related_name='room', verbose_name=_('room type'))

    def __str__(self):
        return 'room ' + str(self.title)

    class Meta:
        db_table = 'room'
        verbose_name = _('room')
        verbose_name_plural = _('rooms')


class AccommodationAttribute(Attribute):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE,
                                      related_name='accommodation_attribute',
                                      verbose_name=_('accommodation'))

    class Meta:
        db_table = 'accommodation_attribute'
        verbose_name = _('accommodation attribute')
        verbose_name_plural = _('accommodations attribute')


class RoomAttribute(Attribute):
    room = models.ForeignKey(Accommodation, models.CASCADE,
                             related_name='room_attribute',
                             verbose_name=_('room'))

    class Meta:
        db_table = 'room_attribute'
        verbose_name = _('room attribute')
        verbose_name_plural = _('rooms attribute')


class AccommodationDatePrice(DatePrice):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'accommodation', verbose_name=_('accommodation'))

    class Meta:
        db_table = 'accommodation_date_price'
        verbose_name = _('accommodation date price')
        verbose_name_plural = _('accommodation dates price')


class RoomDatePrice(DatePrice):
    room = models.ForeignKey(Room, models.CASCADE, 'room_date_price', verbose_name=_('accommodation'))

    class Meta:
        db_table = 'room_date_price'
        verbose_name = _('room date price')
        verbose_name_plural = _('rooms dates price')