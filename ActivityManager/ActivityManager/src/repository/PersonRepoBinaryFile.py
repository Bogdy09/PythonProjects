from src.repository.PersonRepo import PersonRepo
import pickle


class PersonRepoBinaryFile(PersonRepo):
    """
    Manages persons and stores data in 'person.bin', inheriting methods and functions from PersonRepo.
    """

    def __init__(self, file_name="person.bin"):
        """
        Inherits the necessary methods and additionally requires a file to load from.

        :param file_name: The name of the binary file to load and save data.
        """
        super(PersonRepoBinaryFile, self).__init__()
        self._file_name = file_name
        self._load_from_file()

    def _load_from_file(self):
        """
        If there is something to load, it will do so and add it.
        """
        try:
            with open(self._file_name, 'rb') as fin:
                obj = pickle.load(fin)
        except (EOFError, FileNotFoundError):
            return

        for new_person in obj:
            self.add_person_repo(new_person)

    def save_at_file(self):
        """
        Saves the data by writing it to the file.
        """
        print("Data to save:", self.get_all())
        with open(self._file_name, "wb") as fout:
            pickle.dump(self.get_all(), fout)
        print("File saved at:", self._file_name)

    def add_person_repo(self, new_person):
        """
        Adds a new person to the repository and saves the changes to the binary file.

        :param new_person: An instance of the Person class to be added.
        """
        super().add_person_repo(new_person)
        self.save_at_file()
        print("Saved to file")

    def update_person_repo(self, old_id, new_person):
        """
        Updates an existing person in the repository with new information and saves the changes to the binary file.

        :param old_id: ID of the person whose information needs to be updated.
        :param new_person: An instance of the Person class with updated information.
        """
        super().update_person_repo(old_id, new_person)
        self.save_at_file()

    def remove_person_repo(self, person_id):
        """
        Removes a person from the repository by their ID and saves the changes to the binary file.

        :param person_id: ID of the person to be removed.
        """
        super().remove_person_repo(person_id)
        self.save_at_file()
