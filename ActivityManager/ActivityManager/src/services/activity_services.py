from datetime import datetime, time, date
from random import randint, choice, sample
from src.domain.Activities import Activity
from src.repository.ActivityRepo import RepoError
from src.services.undo_services import FunctionCall, Operation


class ServiceError(Exception):
    pass


class Activity_services:
    def __init__(self, list_of_numberss, repo, undo_service):
        """
        Initializes the ActivityServices.

        :param list_of_numberss: List of numbers used for generating activities.
        :param repo: Repository for activities.
        :param undo_service: Undo service for tracking operations.
        """
        self.__repo = repo
        self.__undo_service = undo_service
        #self.generate_random_numbers(list_of_numberss)
        #self.list_of_numbers = list_of_numberss

    @staticmethod
    def generate_numbers(num_numbers, start_range, end_range):
        """
        Generate a list of unique numbers within a specified range.

        :param num_numbers: Number of unique numbers to generate.
        :param start_range: Starting range for number generation (inclusive).
        :param end_range: Ending range for number generation (inclusive).

        :returns List of unique numbers within the specified range.
        """
        unique_numbers = sample(range(start_range, end_range + 1), num_numbers)
        return unique_numbers

    def generate_random_numbers(self, list_of_numbers1):
        """
        Generates random activities based on input data and adds them to the repository.

        :param list_of_numbers1: List of numbers to be used in generating activities.
        """
        list_description = ["tennis practice", "play guitar", "therapist", "running", "playing golf", "cooking", "studying", "skiing", "gym workout", "playing basketball"]
        list_of_numbers = self.generate_numbers(20, 100, 999)

        for i in range(20):
            num_people = randint(1, 10)
            person_indices = self.generate_numbers(num_people, 1, 19)
            people_list = [list_of_numbers1[index] for index in person_indices]
            empty_slots = ["   "] * (20 - num_people - 10)

            formated_date = date(2023, randint(1, 12), randint(1, 28))
            time1 = time(randint(0, 23), randint(0, 59), randint(0, 59))

            self.add_activity(str(list_of_numbers[i]), people_list + empty_slots, formated_date, time1, choice(list_description), [])

    def add_activity_at_startup(self, id, persons_id, formated_date, time, description):
        """
        Adds an activity at startup.

        :param id: ID of the new activity.
        :param persons_id: List of IDs of persons involved in the activity.
        :param formated_date: Date of the activity.
        :param time: Time of the activity.
        :param description: Description of the activity.
        """
        new_activity = Activity(id, persons_id, formated_date, time, description)
        try:
            self.__repo.add_activity_repo(new_activity)
        except RepoError:
            pass

    def add_activity(self, id, persons_id, date1, time, description, options):
        """
        Adds a new activity to the repository.

        :param id: ID of the new activity.
        :param persons_id: List of IDs of persons involved in the activity.
        :param date1: Date of the activity.
        :param time: Time of the activity.
        :param description: Description of the activity.
        :param options: List of available options.
        """
        for i in range(len(persons_id)):
            ok = 0
            for j in range(len(options)):
                if persons_id[i] == options[j]:
                    ok = 1
            if ok == 0 and options != []:
                raise ServiceError("Cannot add non-existent person ID's")
        new_activity = Activity(id, persons_id, date1, time, description)
        try:
            self.__repo.add_activity_repo(new_activity)
            redo_fun = FunctionCall(self.__repo.add_activity_repo, new_activity)
            undo_fun = FunctionCall(self.__repo.remove_activity_repo, id)
            self.__undo_service.record_undo(Operation(undo_fun, redo_fun))
        except RepoError:
            raise ServiceError("Cannot Add")

    def remove_activity(self, id):
        """
        Removes an activity from the repository based on its ID.

        :param id: ID of the activity to be removed.
        """
        try:
            activity = self.__repo.get_activity(id)
            self.__repo.remove_activity_repo(id)
            redo_fun = FunctionCall(self.__repo.remove_activity_repo, id)
            undo_fun = FunctionCall(self.__repo.add_activity_repo, activity)
            self.__undo_service.record_undo(Operation(undo_fun, redo_fun))
        except RepoError:
            raise ServiceError("Cannot remove")

    def update_activity(self, old_id, new_id, new_list, new_formated_date, new_time, new_description, activity, options):
        """
        Updates an existing activity in the repository with new information.

        :param old_id: ID of the activity to be updated.
        :param new_id: New ID of the activity.
        :param new_list: List of IDs of persons involved in the updated activity.
        :param new_formated_date: Updated date of the activity.
        :param new_time: Updated time of the activity.
        :param new_description: Updated description of the activity.
        :param activity: Existing activity to be updated.
        :param options: List of available options.
        """
        for i in range(len(new_list)):
            ok = 0
            for j in range(len(options)):
                if new_list[i] == options[j]:
                    ok = 1
            if ok == 0 and options != []:
                raise ServiceError("The person ID does not exist!")
        new_activity = Activity(new_id, new_list, new_formated_date, new_time, new_description)
        try:
            self.__repo.update(old_id, new_activity)
            redo_fun = FunctionCall(self.__repo.update, old_id, new_activity)
            undo_fun = FunctionCall(self.__repo.update, new_id, activity)
            self.__undo_service.record_undo(Operation(undo_fun, redo_fun))
        except RepoError:
            raise ServiceError("Cannot update")

    def search_activity_based_on_date(self, date):
        """
        Searches for activities based on a specific date.

        :param date: Date to search for activities.

        :returns List of activities occurring on the specified date.
        """
        return self.__repo.search_after_date(date)

    def search_activity_based_on_description(self, description):
        """
        Searches for activities based on a specific description.

        :param description: Description (substring) to search for.

        :returns List of activities with descriptions containing the specified substring.
        """
        return self.__repo.search_after_description(description)

    def get_activities_on_date(self, date):
        """
        Retrieves activities occurring on a specific date.

        :param date: Date to retrieve activities for.

        :returns List of activities occurring on the specified date.
        """
        return self.__repo.get_activities_on_date_repo(date)

    def get_activities_of_person(self, id):
        """
        Retrieves activities associated with a particular person.

        :param id: ID of the person.

        :returns List of activities associated with the specified person ID.
        """
        return self.__repo.get_activities_of_p(id)

    def remove_all_occurrences(self, id):
        """
        After a person is removed, its ID also flees from all the activities it belonged to, removing any
        occurrence there might exist.
        """
        self.__repo.remove_all(id)

    def get_statistic_date(self):
        """
        Goes through all the dates from the dictionary and creates another dictionary having as index the date and as value
        the effective time.
        """
        return self.__repo.get_stat_date()

    def get_all_activities(self):
        """
        Lists all activities from the dictionary.

        :returns: List of all activities.
        """
        return self.__repo.get_all()

    def search_activity_based_on_id(self, id):
        """
        Searches for an activity based on its ID.

        :param id: ID of the activity to search for.

        :returns: Activity with the specified ID or None if not found.
        """
        return self.__repo.search_activity_based_on_id_repo(id)
