from hotel.forms.SearchForm import SearchForm
class SearchHotelService:
	def __init__(self, hotel_manager, room_manager):
		self.hotel_manager = hotel_manager
		self.room_manager = room_manager

	def search(self, request):
		search_form = SearchForm(request.GET)
		if search_form.is_valid():
			check_in = search_form.cleaned_data['check_in']
			check_out = search_form.cleaned_data['check_out']
			hotel_list = self.hotel_manager.get_hotels_by_city(request)
			print self.room_manager.get_room_num
			result_list = []
			for hotel in hotel_list:
				total_room_num = self.room_manager.get_room_num(hotel)
				full_room_num = self.room_manager.get_full_room_num(hotel, check_in, check_out)
				if  total_room_num - full_room_num > 0:
					result_list.append(hotel)
			return result_list
