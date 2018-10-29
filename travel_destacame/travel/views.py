import coreapi

from django.db.models import Count, OuterRef, Subquery, FloatField, F
from django.utils.translation import ugettext_lazy as _

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend, OrderingFilter

# my models here
from travel_destacame.travel.models import (Bus, Location, Trip, Ticket)

# my serializers here
from .serializers import (BusSerializer, TripSerializer, TripStatsSerializer, BusStatsSerializer)


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
        from_location = request.GET.get('from_location', None)
        if from_location:
            return queryset.filter(from_location__name__icontains=from_location.upper())

        return queryset


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    filter_backends = [BusFilterBackend]


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [TripFilterBackend]


class TripStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripStatsSerializer

    def list(self, request):

        """ external queryset """
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
            promedio=Subquery(tickets_query, output_field=FloatField()) / F('dcount')
        )

        serializer = self.serializer_class(trips, many=True)
        return Response(serializer.data)


class BusStatsViewSet(viewsets.ReadOnlyModelViewSet):
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
        trips = Trip.objects.annotate(
            capacidad_vendida=Subquery(tickets_query, output_field=FloatField())
        ).filter(capacidad_vendida__isnull=False)

        serializer = self.serializer_class(trips, many=True)
        return Response(serializer.data)











