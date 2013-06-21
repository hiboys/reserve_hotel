#encoding=utf-8
from hotel.forms.SearchForm import SearchForm
from django.shortcuts import render_to_response
import sys
from hotel.hotels.models import Room, Hotel
from hotel.service.SearchHotelService import SearchHotelService
reload(sys)
sys.setdefaultencoding('utf-8')
class SearchController:
    INSTANCE = None
    def __init__(self, search_hotel_service):
        self.search_hotel_service = search_hotel_service

    @classmethod
    def instance(cls):
        if cls.INSTANCE is None:
            search_hotel_service =  SearchHotelService(Hotel.objects, Room.objects)
            cls.INSTANCE = SearchController(search_hotel_service)
        return cls.INSTANCE

    def execute(self, request):
        result_list = self.search_hotel_service.search(request)
        response = render_to_response('search_result.html', {'result_list':result_list})
        self.set_cookie(request, response)
        return response

    def set_cookie(self, request, response):
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            check_in = search_form.cleaned_data['check_in']
            check_out = search_form.cleaned_data['check_out']
            response.set_cookie('check_in', check_in)
            response.set_cookie('check_out',check_out)
