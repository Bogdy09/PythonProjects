from datetime import time

from domain.Flight import Flight
from repository.Flight_repository import RepositoryError
from services.Flight_service import FlightService

class UiError(Exception):
    pass

class UI:
    def __init__(self):
        self._service=FlightService()
    def print_menu(self):
        while True:
            print("1. Add a new flight.")
            print("2. Delete a flight.")
            print("3. List the airports.")
            print("4. List the time intervals during which no flights are taking place.")
            print("5. Backup radar.")

            try:
                try:
                    try:
                        option=input("Please enter a choice: ")
                        if not isinstance(option, str):
                            raise UiError("Invalid option!")
                        option=int(option)
                        if option==1:
                                    flight_id = input("Please enter the flight ID: ")
                                    dep_city = input("Please enter the departure city: ")
                                    dep_time = input("Please enter the departure time: ")
                                    arr_city = input("Please enter the arrival city: ")
                                    arr_time = input("Please enter the arrival time: ")
                                    if ":" not in dep_time or ":" not in arr_time:
                                        raise UiError("Invalid time!")
                                    hour, minute=dep_time.split(":")
                                    hour1, minute1=arr_time.split(":")
                                    hour=str(hour)
                                    minute=str(minute)
                                    hour1 = str(hour1)
                                    minute1 = str(minute1)
                                    if not hour.isdigit() or not minute.isdigit() or not hour1.isdigit() or not minute1.isdigit():
                                        raise UiError("Invalid time!")
                                    if not 1<=int(hour)<=24 or not 0<=int(minute)<=59 or not 1<=int(hour1)<=24 or not 0<=int(minute1)<=59:
                                        raise UiError("Invalid time!")

                                    if not 15<=(abs(int(hour)-int(hour1)))*60+abs(int(minute)-int(minute1))<=90:
                                        raise UiError("Flight is too short or too long!")
                                    dep_time=time(int(hour), int(minute))
                                    hour, minute=arr_time.split(":")
                                    arr_time=time(int(hour), int(minute))
                                    if dep_time>arr_time:
                                        raise UiError("Invalid time!")
                                    flight=Flight(flight_id, dep_city, dep_time, arr_city, arr_time)
                                    self._service.add_flight(flight)

                        elif option==2:
                            flight_id=input("Please enter the flight ID: ")
                            self._service.delete_flight(flight_id)

                        elif option==3:
                            print(self._service.list_airports())

                        elif option==4:
                            list1=self._service.free_time_intervals()
                            for element in list1:
                                dep_time_formatted = element[0]
                                arr_time_formatted = element[1]
                                print(f"({dep_time_formatted}, {arr_time_formatted})")

                        else:
                            print("Invalid choice!")
                    except RepositoryError as ve:
                        print("There was an error!")
                        print(ve)
                except UiError as ve:
                    print("There was an error!")
                    print(ve)
            except TypeError as ve:
                print("There was an error!")
                print(ve)

