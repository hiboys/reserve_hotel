from django.contrib import admin
from hotel.hotels.models import Location, Hotel, Room, Guest, Booking
admin.site.register(Location)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Booking)
