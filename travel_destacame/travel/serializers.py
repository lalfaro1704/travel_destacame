from rest_framework import serializers

# my models here
from travel_destacame.travel.models import (Bus, Seat)


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
