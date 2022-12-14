from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from users.models import User


class LocationType(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=64)
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    create_time = models.DateTimeField(verbose_name=_('date join'), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_('last modify'), auto_now=True)

    class Meta:
        db_table = 'location_type'
        verbose_name = _('location type')
        verbose_name_plural = _('locations type')


class RoomType(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=64)
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    create_time = models.DateTimeField(verbose_name=_('date join'), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_('last modify'), auto_now=True)

    class Meta:
        db_table = 'room_type'
        verbose_name = _('room type')
        verbose_name_plural = _('rooms type')


class AccommodationType(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=64)
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    create_time = models.DateTimeField(verbose_name=_('date join'), auto_now_add=True)
    last_modify = models.DateTimeField(verbose_name=_('last modify'), auto_now=True)

    class Meta:
        db_table = 'accommodation_type'
        verbose_name = _('accommodation type')
        verbose_name_plural = _('accommodations type')


class Accommodation(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=64)
    owner = models.ForeignKey(User, models.CASCADE,
                              related_name='Accommodation', verbose_name=_(_('Accommodation'))
                              )
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
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


class Room(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=64)
    accommodation = models.ForeignKey(Accommodation, models.CASCADE,
                                      related_name='room', verbose_name=_('accommodation'))
    description = models.TextField(verbose_name=_('description'))
    room_type = models.ManyToManyField(RoomType, related_name='room', verbose_name=_('room type'))

    class Meta:
        db_table = 'room'
        verbose_name = _('room')
        verbose_name_plural = _('rooms')


class Attribute(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=64, blank=True, null=True)
    is_valid = models.BooleanField(verbose_name=_('is valid'), default=True)
    description = models.CharField(verbose_name=_('description'), max_length=64, blank=True, null=True)

    class Meta:
        abstract = True


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


class DatePrice(models.Model):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, related_name='date_price',
                                      verbose_name=_('accommodation'))
    is_reserve = models.BooleanField(verbose_name=_('is reserve'), default=False)
    date = models.DateField(verbose_name=_('date'))
    price = models.FloatField(verbose_name=_('price'))

    class Meta:
        db_table = 'date_price'
        verbose_name = _('date price')
        verbose_name_plural = _('dates price')
