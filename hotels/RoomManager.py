from django.db import models
from django.db.models import Q 
from datetime import date, datetime
from django.db import connection
from hotel.forms.SelectForm import SelectForm

class RoomManager(models.Manager):
    def get_room_num(self, hobj):
        return self.filter(hotel=hobj).count()
    def get_full_room_num(self, hobj, check_in, check_out):
        return self.filter( Q(hotel = hobj) & (
            Q(check_in__range = [check_in, check_out]) |
            Q(check_out__range = [check_in, check_out]))).count()
    def get_price(self, hotel_id, room_type):
        return self.filter(hotel__id = hotel_id, room_type = room_type)[0].price
    def get_room_type_by_hotel(self, hotel):
        return self.filter(hotel = hotel).values("room_type").distinct()
    def get_room_num4hotel_roomtype(self, hotel_id, room_type):
        num = self.filter( Q(hotel__id= hotel_id) & 
                          Q(room_type = room_type)).count()
        return num
    def get_full_room_num4booking(self, hotel_id, room_type, check_in, check_out):
        num = self.filter( Q(hotel__id= hotel_id) & 
                          Q(room_type = room_type) &
                          (Q(check_in__range = [check_in, check_out]) |
                           Q(check_out__range = [check_in, check_out]))).count()
        print connection.queries
        return num
	def get_full_room_num(self, hobj, check_in, check_out):
		return self.filter( Q(hotel = hobj) & (
            Q(check_in__range = [check_in, check_out]) |
            Q(check_out__range = [check_in, check_out]))).count()

    def check_valid_booking(self, hotel_id, room_type, request):
        select_form = SelectForm(request.GET)
        check_in = None
        check_out= None 
        if select_form.is_valid():
            check_in = select_form.cleaned_data['check_in']
            check_out= select_form.cleaned_data['check_out']
        room_booked4type= self.get_full_room_num4booking(int(hotel_id), int(room_type),
                                                         check_in, check_out)
        room_num4type = self.get_room_num4hotel_roomtype(int(hotel_id), int(room_type))
        room_num = int(request.GET['room_num'])
        if room_num4type - room_booked4type < room_num:
            return False 
        else:
            return True
