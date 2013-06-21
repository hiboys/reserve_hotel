from hotel.forms.SelectForm import SelectForm 
class BookService:
    def __init__(self, hotel_manager, room_manager):
        self.hotel_manager = hotel_manager
        self.room_manager = room_manager

    def check_valid_booking(self, hotel_id, room_type,request):
        if  self.room_manager.check_valid_booking(hotel_id, room_type,request):
            hotel = self.hotel_manager.get_hotel_by_id(int(hotel_id))
            room_price = self.room_manager.get_price(hotel_id, room_type)
            select_form = SelectForm(request.GET)
            check_in = None
            check_out = None
            if select_form.is_valid():
                check_in = select_form.cleaned_data['check_in']
                check_out = select_form.cleaned_data['check_out']
            data ={
                "hotel":hotel,
                "room_type":room_type,
                "room_num":request.GET["room_num"],
                "room_price":room_price,
                "check_in": check_in,
                "check_out": check_out,
            }
            return data
        else:
            return None
