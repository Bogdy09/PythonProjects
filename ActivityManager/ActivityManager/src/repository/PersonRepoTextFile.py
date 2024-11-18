import os

from src.domain.Person import Person
from src.repository.PersonRepo import PersonRepo


class PersonRepoTextFile(PersonRepo):
    """
    Manages persons and stores data in 'person.txt', inheriting methods and functions from PersonRepo.
    """

    def __init__(self, file_name="person.txt"):
        """
        Inherits the necessary methods and additionally requires a file to load from.

        :param file_name: The name of the text file to load and save data.
        """
        super(PersonRepoTextFile, self).__init__()
        self._file_name = file_name
        self._load_from_file()

    def _load_from_file(self):
        """
        Opens the text file from which lines are read and split into ID, phone number, and name,
        a new person being created afterward.
        """
        read = []

        try:
            fin = open(self._file_name, 'rt')
            read = fin.readlines()
            fin.close()
        except IOError:
            pass

        for to_read in read:
            line = to_read.split(",")
            new_person = Person(line[0].strip(), line[1].strip(), line[2].strip())
            super().add_person_repo(new_person)

    def save_at_file(self):
        """
        Writes the data back into the file.
        """
        fout = open(self._file_name, "wt")

        for person in self.get_all():
            person_list = f"{person._id},{person._phone_number},{person._name}\n"
            fout.write(person_list)

        fout.close()

    def add_person_repo(self, new_person):
        """
        Adds a new person to the repository and saves the changes to the text file.

        :param new_person: An instance of the Person class to be added.
        """
        super().add_person_repo(new_person)
        self.save_at_file()

    def remove_person_repo(self, person_id):
        """
        Removes a person from the repository by their ID and saves the changes to the text file.

        :param person_id: ID of the person to be removed.
        """
        super().remove_person_repo(person_id)
        self.save_at_file()

    def update_person_repo(self, person_id, new_person):
        """
        Updates an existing person in the repository with new information and saves the changes to the text file.

        :param person_id: ID of the person whose information needs to be updated.
        :param new_person: An instance of the Person class with updated information.
        """
        super().update_person_repo(person_id, new_person)
        self.save_at_file()
