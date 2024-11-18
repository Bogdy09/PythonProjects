from src.repository.ActivityRepo import ActivityRepo
import pickle


class ActivityRepoBinaryFile(ActivityRepo):
    """
    Manages activities and stores data in 'activity.bin', inheriting methods and functions from ActivityRepo.
    """

    def __init__(self, file_name="activity.bin"):
        """
        Initializes the repository with necessary methods and requires a file to load from.

        :param file_name: The name of the binary file to load and save data.
        """
        super().__init__()
        self._file_name = file_name
        self._load_from_file()

    def _load_from_file(self):
        """
        Loads data from the binary file and adds it to the repository.
        """
        try:
            fin = open(self._file_name, 'rb')
            obj = pickle.load(fin)
        except EOFError:
            return

        for new_activity in obj:
            super().add_activity_repo(new_activity)
        fin.close()

    def save_at_file(self):
        """
        Saves the data by writing it to the binary file.
        """
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all(), fout)
        fout.close()

    def add_activity_repo(self, new_activity):
        """
        Adds a new activity to the repository and saves the changes to the binary file.

        :param new_activity: An instance of the Activity class to be added.
        """
        super().add_activity_repo(new_activity)
        self.save_at_file()

    def update(self, old_id, new_activity):
        """
        Updates an existing activity in the repository with new information and saves the changes to the binary file.

        :param old_id: ID of the activity to be updated.
        :param new_activity: An instance of the Activity class with updated information.
        """
        super().update(old_id, new_activity)
        self.save_at_file()

    def remove_activity_repo(self, activity_id):
        """
        Removes an activity from the repository by its ID and saves the changes to the binary file.

        :param activity_id: ID of the activity to be removed.
        """
        super().remove_activity_repo(activity_id)
        self.save_at_file()

    def remove_all(self, persons_id):
        """
        Removes occurrences of a person's ID from all activities and saves the changes to the binary file.

        :param persons_id: ID of the person to be removed.
        """
        super().remove_all(persons_id)
        self.save_at_file()
