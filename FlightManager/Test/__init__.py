from datetime import time
from unittest import TestCase

from domain.Flight import Flight
from repository.Flight_repository import FlightRepository, RepositoryError
from services.Flight_service import FlightService


class Test(TestCase):
    def setUp(self):
        self._flight1=Flight("RO1", "Oradea", time(12, 34), "Cluj", time(13, 00))
        self._flight2=Flight("RO2", "Timisoara", time(14, 30), "Oradea", time(15, 30))
        self._services=FlightService
        self._repo=FlightRepository
    def test_flight(self):
        with self.assertRaises(TypeError):
            Flight( "Oradea", time(12, 34), "Cluj", time(13, 00))

    def test_flight1(self):
        self.assertEqual(self._flight1._id, "RO1")
        self.assertEqual(self._flight1._dep_city, "Oradea")
        self.assertEqual(self._flight1._dep_time, time(12, 34))

    def test_add_flight(self):
        flights=[]
        flights=FlightService()
        flights.add_flight(self._flight1)
        self.assertEqual(len(flights.get_all()), 1)
        flights.add_flight(self._flight2)
        self.assertEqual(len(flights.get_all()), 2)
        with self.assertRaises(RepositoryError):
            flights.add_flight(self._flight1)
        flights.delete_flight(self._flight1.get_id())
        self.assertEqual(len(flights.get_all()), 1)