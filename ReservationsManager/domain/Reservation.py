

class Reservation:
    def __init__(self, reservation_number: int, room_number: int, name: str, number_guests: int, arrival_date,
                 departure_date):
        self.__reservation_number = reservation_number
        self.__room_number = room_number
        self.__name = name
        self.__number_guests = number_guests
        self.__arrival_date = arrival_date
        self.__departure_date = departure_date

    def get_arrival_date(self):
        return self.__arrival_date

    def get_departure_date(self):
        return self.__departure_date

    def get_room_number(self):
        return self.__room_number

    def get_id(self):
        return self.__reservation_number

    def __str__(self):
        return "ID: " + str(self.__reservation_number) + " Room: " + str(
            self.__room_number) + " Name: " + self.__name + " Guests number: " + str(
            self.__number_guests) + " Arrival date: " + str(self.__arrival_date)+" Departure date: "+str(self.__departure_date)
