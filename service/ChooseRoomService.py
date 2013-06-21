class ChooseRoomService:
    def __init__(self, hotel_manager, room_manager):
        self.hotel_manager = hotel_manager
        self.room_manager = room_manager 

    def get_available_rooms(self, hotel_id):
        hotel = self.hotel_manager.get_hotel_by_id(int(hotel_id))
        result_list = self.room_manager.get_room_type_by_hotel(hotel)
        return result_list
