from django.utils.translation import gettext_lazy as _
from django.db import models
from places.models import BaseModel, Location


class Airline(models.Model):
    title = models.CharField(verbose_name=_('name'), max_length=64)
    logo = models.ImageField(verbose_name=_('logo'), upload_to='/airline-logo/')

    class Meta:
        db_table = 'airline'
        verbose_name = _('airline')
        verbose_name_plural = _('airlines')


class Airport(BaseModel):
    title = models.CharField(verbose_name=_('name'), max_length=64)
    location = models.ForeignKey(Location, models.DO_NOTHING, related_name='location', verbose_name=_('location'))
    abbreviated_name = models.CharField(verbose_name=_('abbreviated name'), max_length=16, default=title)

    def __str__(self):
        return str(self.location__city) + ' (' + str(self.abbreviated_name) + ')'

    class Meta:
        db_name = 'airport'
        verbose_name = _('airport')
        verbose_name_plural = _('airports')
