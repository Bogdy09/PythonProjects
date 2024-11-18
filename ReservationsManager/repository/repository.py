from datetime import date
from random import randint

from domain.Reservation import Reservation
from domain.Room import Room


class Repository:
    def __init__(self):
        self._rooms={}
        self._reservations={}
        self.load_rooms_file()
        self.load_reservations_file()

    def load_rooms_file(self):
        with open("rooms.txt", 'r') as f:
            for line in f.readlines():
                line=line.strip()
                if line=="":
                    continue
                (
                    room_number,
                    room_type
                )=line.split(",")
                hotel_room=Room(room_number, room_type)
                self._rooms[room_number]=hotel_room

    def load_reservations_file(self):
        with open("reservations.txt", 'r') as f:
            for line in f.readlines():
                line=line.strip()
                if line=="":
                    continue
                (
                    reservation_number,
                    room_number,
                    name,
                    number_guests,
                    arrival_date,
                    departure_date
                )=line.split(",")
                reservation=Reservation(reservation_number, room_number, name, number_guests, arrival_date,departure_date)
                self._reservations[reservation_number]=reservation

    def convert_to_date(self, date1):
        year, month, day = date1.split("-")
        date1 = date(int(year), int(month), int(day))
        return date1
    """def find_reservations_in_interval_repo(self, date1, date2):
        dict={}
        for each in self._reservations.values():
            if self.convert_to_date(each.get_arrival_date())>=date1 and self.convert_to_date(each.get_departure_date())<=date2:
                dict[each.get_arrival_date()]=each
        return dict"""

    def find_reservations_in_interval_repo(self, date1, date2):
        reservations_dict = {}
        for each in self._reservations.values():

            arrival_date = self.convert_to_date(each.get_arrival_date())
            departure_date = self.convert_to_date(each.get_departure_date())
            if arrival_date >= date1 and departure_date <= date2:
                reservations_dict[arrival_date] = each

        return reservations_dict


    def get_all_repo(self):
        return self._reservations.values()

    def get_all_rooms_repo(self):
        return self._rooms.values()

    def make_reservation_repo(self, room_number, name, number_guests, arrival_date, departure_date):
        id=randint(0, 100)
        while id in self._reservations:
            id=randint(0, 100)
        day, month=arrival_date.split('-')
        arrival_date=date(2024, int(month), int(day))
        day, month = departure_date.split('-')
        departure_date = date(2024, int(month), int(day))
        reservation=Reservation(id, room_number, name, number_guests, arrival_date, departure_date)
        self._reservations[id]=reservation
        for each in self._reservations.values():
            print(each)

    def find_room_capacity_repo(self,room_number):
        for room in self._rooms.values():
            if room.get_room_number()==room_number:
                if room.get_room_type()=="Single Room":
                    return 1
                elif room.get_room_type()=="Double Room":
                    return 2
                else:
                    return 4

    def delete_reservation_by_id_repo(self, id1):
        for reservation in self._reservations.values():
            if reservation.get_id()==id1:
                del self._reservations[id1]
                break

    def find_reservation_by_room_number_repo(self, room_number):
        wanted_rooms={}
        for reservation in self._reservations.values():
            if reservation.get_room_number()==room_number:
                wanted_rooms[reservation.get_id()]=reservation
        return wanted_rooms

    def delete_reservation_by_date_repo(self, start, finish, wanted_rooms:dict):
        deletion = {}
        for each in wanted_rooms.values():

            arrival_date = self.convert_to_date(each.get_arrival_date())
            departure_date = self.convert_to_date(each.get_departure_date())
            start1=self.convert_to_date(start)
            finish1=self.convert_to_date(finish)
            if not ((arrival_date<start1 and departure_date<start1) or (arrival_date>finish1 and departure_date>finish1)):
                deletion[arrival_date] = each

        copy=self._reservations.copy()
        for each in deletion.values():
            for each1 in copy.values():
                if each.get_id()==each1.get_id():
                    del self._reservations[each1.get_id()]


