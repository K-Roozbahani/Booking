from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from places.models import BaseModel, Location


class Airline(BaseModel):
    title = models.CharField(verbose_name=_('name'), max_length=64)
    logo = models.ImageField(verbose_name=_('logo'), upload_to='airline-logo/')

    class Meta:
        db_table = 'airline'
        verbose_name = _('airline')
        verbose_name_plural = _('airlines')


class Airport(BaseModel):
    title = models.CharField(verbose_name=_('name'), max_length=64)
    location = models.ForeignKey(Location, models.DO_NOTHING, related_name='location', verbose_name=_('location'))
    abbreviated_name = models.CharField(verbose_name=_('abbreviated name'), max_length=16)

    def __str__(self):
        return self.abbreviated_name
    class Meta:
        db_table = 'airport'
        verbose_name = _('airport')
        verbose_name_plural = _('airports')


class FlightRule(BaseModel):
    description = models.TextField(verbose_name=_('flight rule'), blank=True, null=True)
    is_penalty = models.BooleanField(verbose_name=_('is penalty'), default=True)

    class Meta:
        db_table = 'flight_rule'
        verbose_name = _('flight rule')
        verbose_name_plural = _('flights rules')


class Flight(BaseModel):
    flight_number = models.IntegerField(verbose_name=_('flight number'))
    source = models.ForeignKey(Airport, models.CASCADE, related_name='flight_source', verbose_name=_('source'))
    destination = models.ForeignKey(Airport, models.CASCADE, related_name='flight_destination',
                                    verbose_name=_('destination'))
    fly_datetime = models.DateTimeField(verbose_name=_('fly datetime'))
    landing_datetime = models.DateTimeField(verbose_name=_('landing datetime'))
    airline = models.ForeignKey(Airline, models.CASCADE, related_name='flight_airline',
                                verbose_name=_('airline'))
    carried_by = models.ForeignKey(Airline, models.CASCADE, related_name='flight_carried_by',
                                   verbose_name=_('carried by'), blank=True, null=True)
    flight_rules = models.ManyToManyField(FlightRule, related_name='flight',
                                          verbose_name=_('flight rules'))

    def __str__(self):
        return str(self.source) + " to " + str(self.destination)

    class Meta:
        db_table = 'flight'
        verbose_name = _('flight')
        verbose_name_plural = _('flights')


class AirTravel(BaseModel):
    CURRENCY_IRR = 1
    CURRENCY_USD = 2
    CURRENCY_EUR = 3
    CURRENCY_CAD = 4
    CHOICES_CURRENCY = ((CURRENCY_IRR, 'IRR'), (CURRENCY_USD, 'USD'), (CURRENCY_EUR, 'EUR'), (CURRENCY_CAD, 'CAD'))
    title = None
    airline = models.ForeignKey(Airline, models.CASCADE, related_name='airline_airline',
                                verbose_name=_('airline'), null=True, blank=True)
    is_international_flight = models.BooleanField(verbose_name=_('is international flight'))
    origin = models.ForeignKey(Airport, models.CASCADE, 'origin', verbose_name=_('origin'))
    final_destination = models.ForeignKey(Airport, models.CASCADE, 'final_destination',
                                          verbose_name=_('final destination'))
    fly_datetime = models.DateTimeField(verbose_name=_('fly datetime'), blank=True, null=True)

    flight_time = models.TimeField(verbose_name=_('flight time'), null=True, blank=True)
    stop_time = models.TimeField(verbose_name=_('stop time'), null=True, blank=True)
    stop_in = models.ForeignKey(Location, models.CASCADE, related_name='air_travel_stop',
                                blank=True, null=True, verbose_name=_('stop in'))
    flights = models.ManyToManyField(Flight, related_name='air_travel', verbose_name='flights')
    adults_price = models.FloatField(verbose_name=_('adult_price'))
    children_price = models.FloatField(verbose_name=_('children_price'))
    infant_price = models.FloatField(verbose_name=_('infant price'))
    currency = models.PositiveSmallIntegerField(verbose_name=_('currency'), choices=CHOICES_CURRENCY, default=1)

    def __str__(self):
        return str(self.final_destination)

    class Meta:
        db_table = 'air_travel'
        verbose_name = _('air travel')
        verbose_name_plural = _('air travels')


class PassengerInformation(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = ((MALE, _("male")), (FEMALE, _('female')))
    first_name = models.CharField(verbose_name=_('first name'), max_length=64)
    last_name = models.CharField(verbose_name=_('last name'), max_length=64)
    gender = models.PositiveSmallIntegerField(verbose_name=_('gender'), choices=GENDER_CHOICE)
    nationality = models.CharField(verbose_name=_('nationality'), max_length=64)
    national_id = models.CharField(verbose_name=_('national id'), max_length=64)
    passport_number = models.CharField(verbose_name=_('passport number'), max_length=64, null=True, blank=True)
    birthday = models.DateField(verbose_name=_('birthday'))
    passport_expire_date = models.DateField(verbose_name=_('passport expire date'), )

    def __str__(self):
        return str(self.first_name) + ' ' + str(self)

    @property
    def age(self):
        birthday = self.birthday
        now = timezone.now()
        return now.year - birthday.year

    class Meta:
        db_table = 'passenger_information'
        verbose_name = _('passenger information')
        verbose_name_plural = _('passengers information')


class Currency(BaseModel):
    national_symbol = models.CharField(verbose_name=_('national symbol'), max_length=8, unique=True)

    class Meta:
        db_table = 'currency'
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        from utils.redis_utils import set_currency
        self.national_symbol = self.national_symbol.upper()
        super(Currency, self).save(force_insert, force_update, using, update_fields)
        set_currency(self.id, self.national_symbol)


class CurrencyExchange(models.Model):
    from utils.redis_utils import currency_choices
    CURRENCIES_CHOICES = currency_choices()
    currency_from = models.PositiveIntegerField(verbose_name=_('currency from'),
                                                choices=CURRENCIES_CHOICES, default=1)
    currency_to = models.PositiveIntegerField(verbose_name=_('currency to'), choices=CURRENCIES_CHOICES, default=1)
    rate = models.FloatField(verbose_name=_('rate'))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        from utils.redis_utils import set_exchange_rate
        super(CurrencyExchange, self).save(force_insert, force_update, using, update_fields)
        set_exchange_rate(self.currency_from, self.currency_to, self.rate)
