from django.db import models
from django.db.models import Q 
from datetime import date, datetime
from django.db import connection
from models import Booking
class BookingManager(models.Manager):

    def save(self, request):
        check_in = request.COOKIES.get('check_in')
        check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out = request.COOKIES.get('check_out')
        check_out= datetime.strptime(check_out, "%Y-%m-%d").date()
        hotel_id = int(request.COOKIES.get("hotel_id"))
        room_type = int(request.COOKIES.get("room_type"))
        room_num = int(request.COOKIES.get("room_num"))
        booking = Booking()
        booking.hotel_id = hotel_id
        booking.room_type = room_type
        booking.check_in = check_in
        booking.check_out = check_out
        booking.room_num = room_num

        guest = Guest()
        guest.firstname = request.GET["firstname"]
        guest.lastname= request.GET["lastname"]
        guest.phone= request.GET["phone"]
        guest.save()
        booking.guest = guest
        booking.save()

