from django.shortcuts import render_to_response
from hotel.hotels.models import Room, Hotel
from datetime import datetime
import sys
from hotel.forms.SelectForm import SelectForm 
from hotel.service.BookService import BookService 
reload(sys)
sys.setdefaultencoding('utf-8')
class BookController:
    INSTANCE = None
    def __init__(self, book_service):
        self.book_service = book_service

    @classmethod
    def instance(cls):
        if cls.INSTANCE is None:
            book_service =  BookService(Hotel.objects, Room.objects)
            cls.INSTANCE = BookController(book_service)
        return cls.INSTANCE

    def set_cookie4book(self, response, data):
        response.set_cookie("hotel_id", data["hotel"].id)
        response.set_cookie("room_type", data["room_type"])
        response.set_cookie("room_num", data["room_num"])
        response.set_cookie("check_in", data["check_in"])
        response.set_cookie("check_out", data["check_out"])

    def execute(self, request, hotel_id, room_type):
        data = self.book_service.check_valid_booking(hotel_id, room_type,request)
        if  data != None:
            response = render_to_response('booking.html', data)
            self.set_cookie4book(response, data)
            return response
        else:
            return render_to_response('booking_error.html', None)
