from random import randint

from domain.Taxi import Taxi
from repository.Taxi_repo import Taxi_repo

class ServiceError(Exception):
    pass
class taxi_services:
    def __init__(self, list_of_ids, list_of_coordinates):
        self._repo=Taxi_repo()
        self.generate_taxis(list_of_ids, list_of_coordinates)

    def generate_taxis(self, list_of_ids, list_of_coordinates):
        for i in range(10):
            id=str(list_of_ids[i])
            x=list_of_coordinates[i][0]
            y=list_of_coordinates[i][1]
            fare=0
            self.add_taxi(x, y, id, fare)

    def generate_coordinates(self):
        coordinates = self.get_coordinates()
        generated_coordinates = None
        while (not generated_coordinates):
            x = int(randint(0, 100))
            y = int(randint(0, 100))

            if not coordinates and abs(x-y)>=10:
                generated_coordinates=(x,y)
            else:
                ok = True
                for i, j in coordinates:
                    if abs(x - i) + abs(y - j) <= 5:
                        ok = False
                if ok == True and abs(x-y)>=10:
                    generated_coordinates=(x,y)

        return generated_coordinates


    def add_taxi(self, x, y, id1, fare:str):
        if not id1.isdigit():
            raise ServiceError("The ID must be numeric! ")
        ids=self.get_ids()
        if id1 in ids:
            raise ServiceError()
        new_taxi=Taxi(x, y, id1, fare)
        self._repo.add_taxi_repo(new_taxi)

    def print(self):
        self._repo.print_repo()

    def get_ids(self):
        return self._repo.get_ids_repo()

    def get_coordinates(self):
        return self._repo.get_coordinates_repo()

    def find_by_coordinates(self, a, b):
        return self._repo.find_by_coordinates_repo(a, b)

    def find_all_taxis(self):
        return self._repo.find_all_taxis_repo()