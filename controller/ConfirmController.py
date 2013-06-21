#encoding=utf-8
from hotel.forms.SearchForm import SearchForm
from hotel.forms.SelectForm import SelectForm 
from django.shortcuts import render_to_response
from hotel.hotels.models import Room, Hotel, Booking
from hotel.service.ChooseRoomService import ChooseRoomService
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ConfirmController:
    INSTANCE = None
    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = ConfirmController()
        return cls.INSTANCE

    def execute(self, request):
        Booking.objects.save(request)
        return render_to_response("booked.html", None)
