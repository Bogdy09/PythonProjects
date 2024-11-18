import unittest

from domain.Reservation import Reservation
from repository.repository import Repository
with open('rooms.txt', 'a'):
    pass
with open('reservations.txt', 'a'):
    pass
class TestHotel(unittest.TestCase):
    def setUp(self):

        self._repo=Repository()

    def test_make_a_reservation(self):
        first=self._repo.get_all_repo()
        print(len(first))
        self._repo.make_reservation_repo('05', 'Bogdan', 2, '20-03', '26-03')
        print(len(first))
        second=self._repo.get_all_repo()



if __name__=='__main__':
    unittest.main()
