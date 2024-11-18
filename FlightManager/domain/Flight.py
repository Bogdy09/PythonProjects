from datetime import time


class Flight:
    def __init__(self, flight_id:str, dep_city:str, dep_time:time, arr_city:str, arr_time:time):
        if not flight_id or not dep_city or not dep_time or not arr_time or not arr_city:
            raise TypeError("Invalid input!")

        if not isinstance(flight_id, str):
            raise TypeError("Invalid input!")

        """if not isinstance(dep_time, time) or not isinstance(arr_time, time):
            raise TypeError("Inv")
        if not dep_city.isalpha():
            raise TypeError("Invalid input!!!")

        if not arr_city.isalpha():
            raise TypeError("Invalid input")"""

        self._id = flight_id
        self._dep_city = dep_city
        self._dep_time = dep_time
        self._arr_city = arr_city
        self._arr_time = arr_time

    def get_id(self):
        return self._id

    def get_dep_time(self):
        return self._dep_time

    def get_arr_time(self):
        return self._arr_time

    def get_dep_city(self):
        return self._dep_city

    def get_arr_city(self):
        return self._arr_city

    def __str__(self):
        return "Flight " + self._id + " departs from: " + self._dep_city + " at: " + self._dep_time + " and arrives at: " + self._arr_city + " at: " + self._arr_time
