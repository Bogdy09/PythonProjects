from domain.Flight import Flight
from repository.Flight_repository import FlightRepository


class FlightService:
    def __init__(self):
        self._repo=FlightRepository()

    def add_flight(self, flight:Flight):
        self._repo.add_flight_repo(flight)

    def delete_flight(self, flight_id):
        self._repo.delete_flight_repo(flight_id)

    def list_airports(self):
        return self._repo.list_airports_repo()

    def free_time_intervals(self):
        return self._repo.free_time_intervals_repo()

    def get_all(self):
        return self._repo.get_all_repo()