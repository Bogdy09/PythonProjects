from datetime import timedelta, time, datetime

class RepoError(Exception):
    """
    The exception raised in the class below
    """
    pass

class ActivityRepo:
    '''
    class that manages activities
    '''

    def __init__(self):
        self._dictt = {}

    def add_activity_repo(self, new_activity):
        if str(new_activity._description).isdigit():
            raise RepoError("Invalid!")
        check = 1
        if self._dictt != {}:
            check = self.checkif(new_activity)
        if new_activity._id not in self._dictt:
            if check == 1:
                self._dictt[new_activity._id] = new_activity
        else:
            raise RepoError("Invalid input!")

    def remove_activity_repo(self, activity_id):
        if self._dictt == {}:
            raise RepoError("Nothing to remove here!\n")
        if activity_id in self._dictt:
            del self._dictt[activity_id]
        else:
            raise RepoError("Cannot remove an ID not in use.\n")

    def checkif(self, new_activity):
        for i in range(len(new_activity._list)):
            for activity in self._dictt.values():
                start = new_activity._date
                start1 = activity._date
                start2 = new_activity._time
                start3 = activity._time

                if start == start1 and start2 == start3:
                    return 0
        return 1

    def update(self, activity_id, new_activity):
        check = 1
        if self._dictt != {}:
            check = self.checkif(new_activity)
        if activity_id in self._dictt and check == 1:
            self._dictt[activity_id] = new_activity
            new_dict = {new_activity._id if old_key == activity_id else old_key: value for old_key, value in
                        self._dictt.items()}
            self._dictt = new_dict
        else:
            raise RepoError("ID not in use! \n")

    def search_after_date(self, date):
        found = []
        for each in self._dictt.values():
            each_date = str(each._date)
            if str(date) in each_date:
                found.append(each)
        return found

    def search_after_description(self, description):
        found = []
        desc = description.lower()
        for each in self._dictt.values():
            descc = each._description.lower()
            if desc in descc:
                found.append(each)
        return found

    def get_activity(self, id):
        if id in self._dictt:
            return self._dictt[id]
        else:
            return "Not an existing activity"

    def get_activities_on_date_repo(self, date):
        found = []
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        for activity in self._dictt.values():
            if str(activity._date) == str(input_date):
                found.append(activity)

    def remove_all(self, id):
        new_list = []
        ok = 0
        to_remove = []
        for activity in self._dictt.values():
            for i in range(len(activity._list)):
                if str(activity._list[i]) != str(id):
                    new_list.append(activity._list[i])
                else:
                    ok = 1
            if new_list == ['    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ']:
                to_remove.append(activity._id)
                new_list = []
            else:
                if ok == 1:
                    new_list.append("    ")
                activity._list = new_list
                new_list = []
            ok = 0

        for i in range(len(to_remove)):
            self.remove(to_remove[i])

    def get_activities_of_p(self, id):
        occurrences = []
        for obj in self._dictt.values():
            listt = obj._list
            for i in range(len(listt)):
                if str(id) == str(listt[i]):
                    occurrences.append(obj)

        return occurrences

    def get_stat_date(self):
        dic = {}
        timeee = datetime(1, 1, 1, 0, 0, 0)
        for obj in self._dictt.values():
            data = str(obj._date).split()
            dic[data[0]] = timeee

        for obj in self._dictt.values():
            timee = obj._time.split(":")
            data = str(obj._date).split()
            dic[data[0]] += timedelta(days=0, hours=int(timee[0]), minutes=int(timee[1]), seconds=int(timee[2]))
        return dic

    def get_all(self):
        return list(self._dictt.values())

    def search_activity_based_on_id_repo(self, id):
        for each in self._dictt.values():
            if each._id == id:
                return each
