from rest_framework import serializers

# my models here
from travel_destacame.travel.models import (Bus, Seat, Location, Trip, Driver, Ticket)


class SeatSerializer(serializers.ModelSerializer):
    seat_ubication = serializers.SerializerMethodField()

    def get_seat_ubication(self, obj):
        return obj.seat_ubication.ubication

    class Meta:
        model = Seat
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        self.fields['seats'] = SeatSerializer(many=True, read_only=True)
        return super(BusSerializer, self).to_representation(instance)

    class Meta:
        model = Bus
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    from_location = LocationSerializer()
    to_location = LocationSerializer()
    driver = DriverSerializer()
    bus = BusSerializer()
    bookings = serializers.SerializerMethodField()

    def get_bookings(self, obj):
        bookings = Ticket.objects.filter(trip=obj)
        serializer = TicketSerializer(bookings, many=True)

        return serializer.data

    class Meta:
        model = Trip
        fields = '__all__'


class TripStatsSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):

        return {
            'from': obj['from_location__name'].capitalize(),
            'to': obj['to_location__name'].capitalize(),
            'promedio': float(obj['promedio']) if obj['promedio'] else 0
        }


class BusStatsSerializer(serializers.BaseSerializer):

    def to_representation(self, obj):

        return {
            'trayecto': TripSerializer(obj).data,
            'capacidad_vendida': '{}%'.format(obj.capacidad_vendida)
        }







