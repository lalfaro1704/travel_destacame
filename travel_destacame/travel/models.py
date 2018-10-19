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

    def save(self):
       self.ubication = self.ubication.upper()
       super(SeatUbication, self).save()

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
    passenger = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('passenger'),
        blank=True,
        null=True
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


class Driver(AbstractUser):
    """Location from/to object."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        verbose_name = _('driver')
        verbose_name_plural = _('drivers')

    def __str__(self):
        return "{} {}".format(self.first_name.capitalize(), self.last_name.capitalize())

















