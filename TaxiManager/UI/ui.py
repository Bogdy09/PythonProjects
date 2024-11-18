from domain.Taxi import Taxi
from services.Taxi_services import taxi_services, ServiceError


class UiError(Exception):
    pass

class UI:
    def __init__(self, list_of_ids, list_of_coordinates):
        self.__Taxi_services=taxi_services(list_of_ids, list_of_coordinates)

    def menu(self):
        while True:
            print("1. Add a taxi")
            print("2. Add a ride")
            print("3. Generate a random ride")
            print("4. Display all taxis")
            choice=int(input("Please enter a choice: "))
            if choice==1:
                try:
                    try:
                        #print(self.__Taxi_services.find_all_taxis())
                        id1=input("Please enter the ID: ")
                        coordinates=input("Please enter the coordinates: ")
                        coordinates=coordinates.replace("(", "")
                        coordinates=coordinates.replace(")", "")

                        coordinates1=coordinates.split(",")
                        x=str(coordinates1[0])
                        y=str(coordinates1[1])
                        if not x.isdigit() or not y.isdigit():
                            raise UiError("The coordinates must be numeric! ")
                        x=int(x)
                        y=int(y)
                        fare=0
                        for i, j in self.__Taxi_services.get_coordinates():
                            if abs(x-i)+abs(y-j)<=5:
                                raise UiError("Invalid coordinates! ")
                        self.__Taxi_services.add_taxi(x, y, id1, fare)
                    except UiError as ve:
                        print("There was an error! ")
                        print(ve)

                except ServiceError as ve:
                    print("error")

            elif choice==2:
                try:
                    coordinates=input("Please enter the coordinates of the destination: ")
                    coordinates = coordinates.replace("(", "")
                    coordinates = coordinates.replace(")", "")

                    coordinates1 = coordinates.split(",")
                    x = coordinates1[0].strip()
                    y = coordinates1[1].strip()
                    if not x.isdigit() or not y.isdigit():
                        raise UiError("The coordinates must be numeric! ")
                    x=int(x)
                    y=int(y)

                    min=200
                    for i, j in self.__Taxi_services.get_coordinates():
                        if abs(x-i)+abs(y-j)<min:
                            min=abs(x-i)+abs(y-j)
                            a=i
                            b=j
                    assigned_taxi=self.__Taxi_services.find_by_coordinates(a, b)
                    print(f"The taxi assigned to your ride is {assigned_taxi}")
                    assigned_taxi._fare=assigned_taxi._fare+abs(x-assigned_taxi._x)+abs(y-assigned_taxi._y)
                    assigned_taxi._x=x
                    assigned_taxi._y=y
                except UiError as ve:
                    print("There was an error! ")
                    print(ve)

            elif choice==3:
                generated_coordinates=self.__Taxi_services.generate_coordinates()
                print(generated_coordinates)
                x = int(generated_coordinates[0])
                y = int(generated_coordinates[1])
                min = 200
                for i, j in self.__Taxi_services.get_coordinates():
                    if abs(x - i) + abs(y - j) < min:
                        min = abs(x - i) + abs(y - j)
                        a = i
                        b = j
                assigned_taxi = self.__Taxi_services.find_by_coordinates(a, b)
                print(f"The taxi assigned to your ride is {assigned_taxi}")
                assigned_taxi._fare = assigned_taxi._fare + abs(x - assigned_taxi._x) + abs(y - assigned_taxi._y)
                assigned_taxi._x = x
                assigned_taxi._y = y

            elif choice==4:
                self.__Taxi_services.print()




