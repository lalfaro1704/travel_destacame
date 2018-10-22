from django.contrib import admin

# Register your models here.
from travel_destacame.travel.models import (Seat, Bus, SeatBus, Location,
                                            Driver, Trip, Ticket)


class SeatBusM2MInline(admin.TabularInline):
    model = SeatBus
    extra = 5


class SeatAdmin(admin.ModelAdmin):
    search_fields = ('number', 'seat_ubication__ubication')


class BusAdmin(admin.ModelAdmin):
    list_display = ['id', 'serial']
    search_fields = ('id', 'serial')
    inlines = (SeatBusM2MInline,)


class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    search_fields = ('id', 'first_name', 'last_name')


class TripAdmin(admin.ModelAdmin):
    list_display = ['from_location', 'to_location', 'departure', 'driver']
    search_fields = ('from_location', 'to_location', 'departure')


class TicketAdmin(admin.ModelAdmin):
    list_display = ['trip', 'id', 'passenger', 'seat']
    search_fields = ('id', 'trip__from_location', 'trip__to_location',
                     'passenger__first_name', 'passenger__last_name')


admin.site.register(Seat, SeatAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Ticket, TicketAdmin)
