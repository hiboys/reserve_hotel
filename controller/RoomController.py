#encoding=utf-8
from hotel.forms.SearchForm import SearchForm
from hotel.forms.SelectForm import SelectForm 
from django.shortcuts import render_to_response
from hotel.hotels.models import Room, Hotel
from hotel.service.ChooseRoomService import ChooseRoomService
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class RoomController:
    INSTANCE = None
    def __init__(self,choose_room_service ):
        self.choose_room_service = choose_room_service 

    @classmethod
    def instance(cls):
        if cls.INSTANCE is None:
            choose_room_service = ChooseRoomService(Hotel.objects, Room.objects)
            cls.INSTANCE = RoomController(choose_room_service)
        return cls.INSTANCE

    def get_date_from_cookie(self, request):
        check_in = request.COOKIES.get('check_in')
        check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out = request.COOKIES.get('check_out')
        check_out= datetime.strptime(check_out, "%Y-%m-%d").date()
        return check_in, check_out

    def execute(self, request, hotel_id):
        check_in, check_out = self.get_date_from_cookie(request)
        result_list = self.choose_room_service.get_available_rooms(hotel_id)
        form = SelectForm()
        form.fields["check_in"].initial = check_in
        form.fields["check_out"].initial = check_out
        hotel = Hotel.objects.get_hotel_by_id(int(hotel_id))
        render_dict = { "hotel":hotel, "form":form, "room_type_list":result_list,}
        return render_to_response('choose_room_type.html', render_dict)
