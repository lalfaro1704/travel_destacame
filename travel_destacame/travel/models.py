import uuid
from datetime import datetime

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from model_utils.models import TimeStampedModel


class SeatUbication(models.Model):
    """Seat ubication."""
    ubication = models.CharField(
        max_length=150,
        verbose_name=_('ubication')
    )

    class Meta:
        verbose_name = _('seat ubication')
        verbose_name_plural = _('seat ubications')

    def __str__(self):
        return "{}".format(self.ubication.capitalize())


class Seat(models.Model):
    """Seat object."""
    number = models.IntegerField(
        verbose_name=_('number')
    )
    seat_ubication = models.ForeignKey(
        SeatUbication,
        on_delete=models.CASCADE,
        verbose_name=_('seat ubication')
    )

    class Meta:
        verbose_name = _('seat')
        verbose_name_plural = _('seats')

    def __str__(self):
        return "#{} - {}".format(
            self.number, self.seat_ubication
        )


class Bus(models.Model):
    """Bus object."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    serial = models.CharField(
        max_length=150,
        verbose_name=_('serial')
    )
    seats = models.ManyToManyField(
        Seat,
        through="SeatBus",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('bus')
        verbose_name_plural = _('buses')

    def save(self):
       self.serial = self.serial.upper()
       super(Bus, self).save()

    def __str__(self):
        return "{}".format(self.serial)


class SeatBus(models.Model):
    """Many to many relationship between bus and seat."""
    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        verbose_name=_('bus')
    )
    seat = models.ForeignKey(
        Seat,
        on_delete=models.CASCADE,
        verbose_name=_('seat')
    )


class Location(models.Model):
    """Location from/to object."""
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )

    def save(self):
       self.name = self.name.upper()
       super(Location, self).save()

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def __str__(self):
        return "{}".format(self.name.capitalize())


class Driver(models.Model):
    """Bus driver object."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=150
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is active?')
    )

    def save(self):
       self.first_name = self.first_name.upper()
       self.last_name = self.last_name.upper()
       super(Driver, self).save()

    class Meta:
        verbose_name = _('driver')
        verbose_name_plural = _('drivers')

    def __str__(self):
        return "{} {}".format(
            self.first_name.capitalize(), self.last_name.capitalize()
        )


class Trip(models.Model):
    """Trip object."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    from_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="from_location",
        verbose_name=_('from')
    )
    to_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="to_location",
        verbose_name=_('to')
    )
    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        verbose_name=_('bus')
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        verbose_name=_('driver')
    )
    departure = models.DateTimeField(
        _('departure')
    )

    class Meta:
        verbose_name = _('trip')
        verbose_name_plural = _('trips')

    def __str__(self):
        return "{}-{} {}".format(
            self.from_location, self.to_location, self.departure
        )


class Ticket(models.Model):
    """Trip object."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        verbose_name=_('trip')
    )
    seat = models.ForeignKey(
        SeatBus,
        on_delete=models.CASCADE,
        verbose_name=_('seat')
    )
    passenger = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('passenger'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')

    def __str__(self):
        return "{} {} {}".format(
            self.id, self.trip, self.passenger
        )














