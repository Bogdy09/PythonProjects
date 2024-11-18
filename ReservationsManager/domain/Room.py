class Room:
    def __init__(self, room_number:int, room_type:str):
        self._room_number=room_number
        self._room_type=room_type

    def get_room_number(self):
        return self._room_number

    def get_room_type(self):
        return self._room_type

    def __str__(self):
        return "Room number: "+str(self._room_number)+" Room type: "+self._room_type
