from calendar import calendar

from repository.repository import Repository
from faker import Faker
import texttable


class Services:
    def __init__(self):
        self._repository = Repository()

    def find_reservations_in_interval(self, date1, date2):
        dict1 = self._repository.find_reservations_in_interval_repo(date1, date2)
        sorted_reservations = dict(sorted(dict1.items()))
        return sorted_reservations

    def find_interval_in_reservations(self, date1, date2):
        rooms = {}
        for each in self.get_all_rooms():

            rooms[each.get_room_number()] = each
        for reservation in self.get_all_reservations():

            if not((date1 <= self.convert_to_date(reservation.get_arrival_date()) and date2<=self.convert_to_date(reservation.get_arrival_date())) or(date1>=self.convert_to_date(reservation.get_departure_date()))):
                if reservation.get_room_number() in rooms:
                    del rooms[reservation.get_room_number()]
        return rooms

    def get_all_reservations(self):
        return self._repository.get_all_repo()

    def get_all_rooms(self):
        return self._repository.get_all_rooms_repo()

    def convert_to_date(self, date1):
        return self._repository.convert_to_date(date1)

    def make_reservation(self, room_number, name, number_guests, arrival_date, departure_date):
        self._repository.make_reservation_repo(room_number, name, number_guests, arrival_date, departure_date)

    def find_room_capacity(self, room_number):
        return self._repository.find_room_capacity_repo(room_number)

    def delete_reservation_by_id(self, id1):
        self._repository.delete_reservation_by_id_repo(id1)

    def find_reservation_by_room_number(self, room_number):
        return self._repository.find_reservation_by_room_number_repo(room_number)

    def delete_reservation_by_date(self, start, finish, wanted_rooms):
        self._repository.delete_reservation_by_date_repo(start, finish, wanted_rooms)
