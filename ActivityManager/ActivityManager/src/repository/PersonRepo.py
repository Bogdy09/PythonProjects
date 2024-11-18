from src.domain.Person import Person

class RepoError(Exception):
    """
    The exception raised in the class below
    """
    pass

class PersonRepo:
    """
    Class that manages the persons
    """
    def __init__(self):
        self._dictt = {}
        self._id_list = []

    def add_person_repo(self, new_person: Person):
        if new_person._id not in self._id_list:
            self._dictt[new_person._id] = new_person
            self._id_list.append(new_person.get_id)
        else:
            raise RepoError("You cannot add a person with the same ID!")

    def remove_person_repo(self, id: str):
        if id not in self._id_list:
            raise RepoError("You cannot remove a non-existent ID!")
        else:
            del self._dictt[id]
            for each in self._id_list:
                if each == id:
                    self._id_list.pop()

    def get_list(self):
        return self._id_list

    def get_person(self, id):
        if id in self._dictt:
            return self._dictt[id]
        else:
            return "Not an existing person"

    def check_existing_person(self, id):
        if id in self._dictt.values():
            return self._dictt[id]
        else:
            return "Not an existing person"

    def update_person_repo(self, old_id: str, new_person: Person):
        if self._dictt == {}:
            raise RepoError("Nothing to update here!")
        if old_id in self._dictt:
            self._dictt[old_id] = new_person
            new_dict = {new_person._id if old_key == old_id else old_key: value for old_key, value in
                        self._dictt.items()}
            self._dictt = new_dict
        else:
            raise RepoError("Cannot update an ID not in use.\n")

    def search_by_phone_number_repo(self, searched_phone_number):
        found = []
        for each in self._dictt.values():
            if searched_phone_number in each._phone_number:
                found.append(each)
        return list(found)

    def search_by_name_repo(self, searched_name):
        found = []
        for each in self._dictt.values():
            if searched_name.lower() in each._name.lower():
                found.append(each)
        return list(found)

    def get_all(self):
        return list(self._dictt.values())
