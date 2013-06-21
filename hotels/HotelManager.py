from django.db import models
from django.db.models import Q 
from datetime import date, datetime
from django.db import connection


class HotelManager(models.Manager):
    def str2date(self, year, month, day):
        year= int(year)
        month= int(month)
        day= int(day)
        return date(year, month, day)

    def get_hotel_by_id(self, hotel_id):
        query_set = self.filter(id = hotel_id)
        if  query_set != None:
            return query_set[0]
        else:
            return None
	def hello(self):
		pass

    def get_hotels_by_city(self,request):
        city =  request.GET['city']
        return self.filter(address__city = city)
