from django.db import models
from django.db.models import Q 
from datetime import date, datetime
from django.db import connection
from hotel.hotels.HotelManager import HotelManager
from hotel.hotels.RoomManager import RoomManager 
# Create your models here.

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

class Location(models.Model):
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)

class Hotel(models.Model):
    description = models.CharField(max_length=255)
    hotelname = models.CharField(max_length=255)
    starts = models.IntegerField()
    address = models.ForeignKey(Location)
    objects = HotelManager()

class Room(models.Model):
    hotel = models.ForeignKey(Hotel)
    room_type = models.IntegerField()
    price = models.FloatField()
    check_in = models.DateField()
    check_out = models.DateField()
    objects = RoomManager()

class Guest(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    phone= models.CharField(max_length=255)

class Booking(models.Model):
    guest = models.ForeignKey(Guest)
    hotel_id = models.IntegerField()
    room_type = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    room_num = models.IntegerField()
    objects = BookingManager()
