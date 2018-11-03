import coreapi

from django.db.models import Count, OuterRef, Subquery, FloatField, F, IntegerField
from django.utils.translation import ugettext_lazy as _

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend, OrderingFilter
from rest_framework import mixins

# my models here
from travel_destacame.travel.models import (Bus, Location, Trip, Ticket, Driver)

# my serializers here
from .serializers import (BusSerializer, TripSerializer, TripStatsSerializer, BusStatsSerializer, DriverSerializer, 
                          TicketSerializer)


class BusFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        description = 'Filter buses by serial. Example: "XCD-93Y".'
        return [
            coreapi.Field(
                name='serial',
                location='query',
                required=False,
                type='str',
                description=description,
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        serial = request.GET.get('serial', None)
        if serial:
            return queryset.filter(serial=serial.upper())
        return queryset


class TripFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='from_location',
                location='query',
                required=False,
                type='str',
                description='Filter trips by origin location. Example: "La florida".',
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        distinct = request.GET.get('distinct', None)

        if distinct:
            return queryset.distinct("from_location","to_location")

        return queryset


class BusViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Autobus por ID.

    list:
    Lista de autobuses.

    create:
    Crea un nuevo autobus.

    update:
    Actualiza los valores de un autobus.

    delete:
    Borra un autobus.
    """
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class TripViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Trayecto por ID.

    list:
    Lista de trayectos.

    create:
    Crea un nuevo trayecto.

    update:
    Actualiza los valores de un trayecto.

    delete:
    Borra un trayecto.
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class DriverViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Chofer por ID.

    list:
    Lista de choferes.

    create:
    Crea un nuevo chofer.

    update:
    Actualiza los valores de un chofer

    delete:
    Borra un chofer
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Boleto por ID.

    list:
    Lista de boletos.

    create:
    Crea un nuevo boleto.

    update:
    Actualiza los valores de un boleto

    delete:
    Borra un boleto
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TripStatsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    Lista de trayectos junto a su promedio de pasajeros.
    """
    queryset = Trip.objects.all()
    serializer_class = TripStatsSerializer

    def list(self, request):
        tickets_query = (
            Ticket.objects.filter(
                trip__from_location=OuterRef('from_location'),
                trip__to_location=OuterRef('to_location')
            ).values(
                'trip__from_location',
                'trip__to_location'
            ).annotate(
                dcount=Count('id')
            ).values('dcount')[:1]
        )

        """ internal queryset """
        trips = Trip.objects.values(
            'from_location__name',
            'to_location__name'
        ).annotate(
            dcount=Count('id')
        ).annotate(
            promedio=Subquery(tickets_query, output_field=IntegerField()) / F('dcount')
        )

        serializer = self.serializer_class(trips, many=True)
        return Response(serializer.data)


class BusStatsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    Lista de autobuses de un trayecto con más del 0% de su capacidad vendida.
    """
    queryset = Bus.objects.all()
    serializer_class = BusStatsSerializer

    def list(self, request):

        """ external queryset """
        tickets_query = (
            Ticket.objects.filter(
                trip__id=OuterRef('id')
            ).values(
                'trip__from_location',
                'trip__to_location'
            ).annotate(
                dcount=Count('id')
            ).values('dcount')[:1]
        )

        """ internal queryset """
        trips = Trip.objects.annotate(seats=Count('bus__seats')).annotate(
            capacidad_vendida=Subquery(tickets_query, output_field=IntegerField()) * 100 / F('seats')
        ).filter(capacidad_vendida__isnull=False)

        serializer = self.serializer_class(trips, many=True)
        return Response(serializer.data)











