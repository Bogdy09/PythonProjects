from datetime import date

from services.services import Services


class UI:
    def __init__(self):
        self._services = Services()

    def print_menu(self):
        while(True):
            try:
                print("1. Find all reservations in a time interval. ")
                print("2. Create a reservation. ")
                print("3. Delete reservations. ")
                print("4. Display reservations. ")

                choice=int(input("Please enter a choice: "))
                if choice==1:
                    date1=input("Please enter the first date(dd-mm): ")
                    day, month=date1.split("-")
                    date1=date(2024, int(month), int(day))
                    date2 = input("Please enter the second date(dd-mm): ")
                    day, month = date2.split("-")
                    date2 = date(2024, int(month), int(day))
                    dict1=self._services.find_reservations_in_interval(date1, date2)
                    for each in dict1.values():
                        print(each)

                elif choice==2:
                    arrival_date1=input("Please enter the arrival date: ")
                    day, month = arrival_date1.split("-")
                    arrival_date = date(2024, int(month), int(day))

                    departure_date1=input("Please enter the departure date: ")
                    day, month = departure_date1.split("-")
                    departure_date = date(2024, int(month), int(day))

                    rooms=self._services.find_interval_in_reservations(arrival_date, departure_date)
                    print("The available rooms for reservation are: ")
                    for room in rooms.values():
                        print(room)
                    print("1. Continue reservation: ")
                    print("2. Cancel reservation: ")
                    option=int(input("Please enter a choice: "))
                    if option==2:
                        self.print_menu()
                    else:
                        room_number=input("Please enter the room number: ")
                        name=input("Please enter your name: ")
                        number_guests=input("Please enter the number of guests: ")
                        if not name:
                            raise TypeError("Invalid input!")
                        room_capacity=self._services.find_room_capacity(room_number)
                        if room_capacity<=number_guests:
                            raise TypeError("Invalid input! ")
                        self._services.make_reservation(room_number, name, number_guests, arrival_date1, departure_date1)

                elif choice==3:
                    print("1. Delete by ID: ")
                    print("2. Delete by date interval: ")
                    option=int(input("Please enter a choice: "))
                    if option==1:
                        id1=input("Please enter a valid ID: ")
                        self._services.delete_reservation_by_id(id1)

                    elif option==2:
                        start=input("Please enter the start date(dd-mm): ")
                        finish=input("Please enter the finish date(dd-mm): ")
                        day, month=start.split('-')
                        start="2024"+'-'+month+'-'+day
                        day, month = finish.split('-')
                        finish = "2024" + '-' + month + '-' + day
                        room_number=input("Please enter the room number: ")
                        wanted_room=self._services.find_reservation_by_room_number(room_number)
                        self._services.delete_reservation_by_date(start, finish, wanted_room)

                elif choice==4:
                    reservation = self._services.get_all_reservations()
                    for each in reservation:
                        print(each)


            except TypeError as ve:
                print("There was an error!")
                print(ve)


