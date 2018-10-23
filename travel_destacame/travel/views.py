import coreapi

from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend, OrderingFilter

# my models here
from travel_destacame.travel.models import (Bus)

# my serializers here
from .serializers import (BusSerializer)


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


class BusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    filter_backends = [BusFilterBackend]














