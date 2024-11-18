from random import choice
from src.domain.Person import Person
from src.repository.PersonRepo import RepoError
from src.services.activity_services import ServiceError
from src.services.undo_services import FunctionCall, Operation


class Person_services:
    """
    Handles person services.
    """
    def __init__(self, list_of_numbers, repo, undo_service):
        """
        Constructor for PersonServices.

        :param list_of_numbers: List of numbers used for generating person instances.
        :param repo: Repository for persons.
        :param undo_service: Undo service for tracking operations.
        """
        self.__repo = repo
        self._undo_service = undo_service
        #self.generate_numbers(list_of_numbers)

    def generate_numbers(self, list_of_nr):
        """
        Generates person instances based on the list_of_nr and adds them to the repository.

        :param list_of_nr: List of numbers to generate person instances.
        """
        names = ['Alex', 'Delia', 'Ioana', 'Ariana', 'Aris', 'Luca', 'Eric', 'Lucian',
                 'Romeo', 'Andreea', 'Nikol', 'Bogdan', 'Flaviu', 'Mihai', 'Andrei',
                 'Silviu', 'James', 'Chris', 'Marius', 'Joe', 'Mircea']
        prefix = "07"
        for i in range(20):
            name = choice(names)
            id = str(list_of_nr[i])
            number = ''.join(choice("0123456789") for _ in range(8))
            phone_number = prefix + number
            self.add_person(id, phone_number, name)

    def get_person(self, id):
        """
        Returns the person having a certain ID from the repository.

        :param id: ID of the person to retrieve.

        :returns: Person with the specified ID.
        """
        return self.__repo.get_person(id)

    def add_person(self, id: str, phone_number: str, name: str):
        """
        Adds a new person to the repository.

        :param id: ID of the person to be added.
        :param name: Name of the person to be added.
        :param phone_number: Phone number of the person to be added.
        """
        words = name.split()
        for word in words:
            if not word.isalpha():
                raise ValueError("Invalid name! ")
        if not phone_number.isdigit():
            raise ValueError("Invalid phone number!")
        if len(phone_number) != 10:
            raise ValueError("Invalid phone number!")
        if phone_number[0] != '0' or phone_number[1] != '7':
            raise ValueError("Invalid phone number")

        new_person = Person(id, phone_number, name)
        try:
            self.__repo.add_person_repo(new_person)
            redo_fun = FunctionCall(self.__repo.add_person_repo, new_person)
            undo_fun = FunctionCall(self.__repo.remove_person_repo, id)
            self._undo_service.record_undo(Operation(undo_fun, redo_fun))
        except RepoError:
            raise ServiceError("Cannot Add")

    def remove_person(self, id):
        """
        Removes a person from the repository by their ID.

        :param id: ID of the person to be removed.
        """
        try:
            person = self.__repo.get_person(id)
            self.__repo.remove_person_repo(id)
            redo_fun = FunctionCall(self.__repo.remove_person_repo, id)
            undo_fun = FunctionCall(self.__repo.add_person_repo, person)
            self._undo_service.record_undo(Operation(undo_fun, redo_fun))
        except RepoError:
            raise ServiceError("Cannot remove")

    def update_person(self, old_id, changed_id, changed_phone_number, changed_name):
        """
        Updates an existing person in the repository with new information.

        :param old_id: ID of the person to be updated.
        :param changed_id: New ID of the person.
        :param changed_name: New name of the person.
        :param changed_phone_number: New phone number of the person.
        """
        if not changed_name.isalpha():
            raise ValueError("Invalid name!")
        if not changed_phone_number.isdigit():
            raise ValueError("Invalid phone number!")
        if len(changed_phone_number) != 10:
            raise ValueError("Invalid phone number!")
        person = self.__repo.get_person(old_id)
        new_person = Person(changed_id, changed_phone_number, changed_name)
        try:
            self.__repo.update_person_repo(old_id, new_person)
            redo_fun = FunctionCall(self.__repo.update_person_repo, old_id, new_person)
            undo_fun = FunctionCall(self.__repo.update_person_repo, changed_id, person)
            self._undo_service.record_undo(Operation(undo_fun, redo_fun))
        except RepoError:
            raise ServiceError("Cannot update")

    def get_all_persons(self):
        """
        Returns all persons from the repository.

        :returns: List of all persons.
        """
        return self.__repo.get_all()

    def get_list(self):
        """
        Returns the list of active IDs in the current state.

        :returns: List of active IDs.
        """
        return self.__repo.get_list()

    def search_by_phone_number(self, searched_phone_number):
        """
        Searches and returns persons based on the provided phone number.

        :param searched_phone_number: Phone number to search for.

        :returns: List of persons with the specified phone number.
        """
        return self.__repo.search_by_phone_number_repo(searched_phone_number)

    def search_by_name(self, searched_name):
        """
        Searches and returns persons based on the provided name.

        :param searched_name: Name (substring) to search for.

        :returns: List of persons with names containing the specified substring.
        """
        return self.__repo.search_by_name_repo(searched_name)
