from datetime import datetime

from src.domain.Activities import Activity
from src.repository.ActivityRepo import ActivityRepo


class ActivityRepoTextFile(ActivityRepo):
    """
    Manages activities and stores data in 'activity.txt', inheriting methods and functions from ActivityRepo.
    """

    def __init__(self, file_name="activity.txt"):
        """
        Initializes the repository with necessary methods and requires a file to load from.

        :param file_name: The name of the text file to load and save data.
        """
        super(ActivityRepoTextFile, self).__init__()
        self._file_name = file_name
        self._load_from_file()

    def _load_from_file(self):
        """
        Reads lines from the text file, splits them into components, and creates new activities.
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
            date = line[2].strip()
            time = line[3].strip()
            date1 = date.split("-")
            time1 = time.split(":")
            the_date = datetime(int(date1[0]), int(date1[1]), int(date1[2]), int(time1[0]), int(time1[1]), int(time1[2]))
            new_activity = Activity(line[0].strip(), line[1].split(), the_date, line[4].strip(), line[5].strip())
            super().add(new_activity)

    def save_at_file(self):
        """
        Writes the data back into the text file.
        """
        fout = open(self._file_name, "wt")
        for activity in self.get_all():
            the_date = str(activity._date).split()
            to_str = ''
            for i in range(len(activity._list)):
                if activity._list[i] != '   ':
                    to_str += str(activity._list[i]) + " "
            activity_list = (
                activity._id + ',' + to_str[:-1] + ',' + str(the_date[0]) + ',' + str(the_date[1]) + ',' + str(
                    activity._time) + ',' + str(activity._description) + "\n"
            )
            fout.write(activity_list)

        fout.close()

    def add_activity_repo(self, new_activity):
        """
        Adds a new activity to the repository and saves the changes to the text file.

        :param new_activity: An instance of the Activity class to be added.
        """
        super().add_activity_repo(new_activity)
        self.save_at_file()

    def remove_activity_repo(self, activity_id):
        """
        Removes an activity from the repository by its ID and saves the changes to the text file.

        :param activity_id: ID of the activity to be removed.
        """
        super().remove_activity_repo(activity_id)
        self.save_at_file()

    def update(self, activity_id, new_activity):
        """
        Updates an existing activity in the repository with new information and saves the changes to the text file.

        :param activity_id: ID of the activity to be updated.
        :param new_activity: An instance of the Activity class with updated information.
        """
        super().update(activity_id, new_activity)
        self.save_at_file()

    def remove_all(self, persons_id):
        """
        Removes occurrences of a person's ID from all activities and saves the changes to the text file.

        :param persons_id: ID of the person to be removed.
        """
        super().remove_all(persons_id)
        self.save_at_file()
