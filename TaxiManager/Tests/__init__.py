from unittest import TestCase
from random import randint

from UI.ui import UiError
from domain.Taxi import Taxi
from repository.Taxi_repo import Taxi_repo
from services.Taxi_services import taxi_services, ServiceError


def generate_ids(n):
    ids=set()
    while(len(ids)<n):
        nr=randint(1, 999)
        ids.add(nr)
    return list(ids)

def generate_coordinates(n):
    coordinates=[]
    while(len(coordinates)<n):
        x=int(randint(0, 100))
        y=int(randint(0, 100))
        if not coordinates:
            coordinates.append((x, y))
        else:
            ok=True
            for i, j in coordinates:
                    if abs(x-i)+abs(y-j)<=5:
                        ok=False
            if ok==True:
                coordinates.append((x, y))

    return coordinates


class Test(TestCase):
    def setUp(self):
        self.repo=Taxi_repo()
        self.services=taxi_services
        self.taxi1=Taxi(21,93, 123, 0)
        self.taxi2=Taxi("ab", 12, 1234, 0)

    def test_add_taxi(self):
        list_of_ids=generate_ids(10)
        list_of_coordinates=generate_coordinates(10)
        list_of_taxis=taxi_services(list_of_ids, list_of_coordinates)
        list_of_taxis.add_taxi(self.taxi1.get_x, self.taxi1.get_y, str(self.taxi1.get_id), self.taxi1.get_fare )
        self.assertEqual(len(list_of_taxis.find_all_taxis()), 11)
        self.assertEqual(self.taxi1.get_x, 21)
        self.assertEqual(self.taxi1.get_y, 93)
        self.assertEqual(self.taxi1.get_id, 123)
        self.assertEqual(self.taxi1.get_fare, 0)

    def test_already_used_taxi(self):
        list_of_ids=generate_ids(10)
        list_of_coordinates=generate_coordinates(10)
        list_of_taxis=taxi_services(list_of_ids, list_of_coordinates)
        list_of_taxis.add_taxi(self.taxi1.get_x, self.taxi1.get_y, str(self.taxi1.get_id), self.taxi1.get_fare )
        with self.assertRaises(ServiceError ):
            list_of_taxis.add_taxi(self.taxi1.get_x, self.taxi1.get_y, str(self.taxi1.get_id), self.taxi1.get_fare)
