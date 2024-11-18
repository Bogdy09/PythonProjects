from domain.Flight import Flight
from datetime import timedelta, time


class RepositoryError(Exception):
    pass

class FlightRepository:
    def __init__(self):
        self._data = {}
        self.load()

    def load(self):
        with open("flights.txt", "r") as f:
            for line in f.readlines():
                line=line.strip()
                if line=="":
                    continue

                (
                    flight_id,
                    dep_city,
                    dep_time,
                    arr_city,
                    arr_time
                )=line.split(",")

                flight=Flight(flight_id, dep_city, dep_time, arr_city, arr_time)

                self._data[flight_id]=flight

    def save(self):
        with open("flights.txt", "w") as f:
            for flight in self._data.values():
                f.write(
                    f"{flight._id}, {flight._dep_city}, {flight._dep_time}, {flight._arr_city}, {flight._arr_time}\n"
                )

    def add_flight_repo(self, flight:Flight):
        for i in self._data.values():
            if i.get_id()==flight.get_id():
                raise RepositoryError("Flights cannot have the same ID!")
            if i.get_dep_time()==flight.get_dep_time() or i.get_arr_time()==flight.get_arr_time():
                raise RepositoryError("Airport can manage only one departure or arrival at once!")

        self._data[flight._id]=flight
        self.save()

    def delete_flight_repo(self, flight_id):
        ok=False
        for i in self._data.values():
            if i.get_id()==flight_id:
                ok=True
                self._data.pop(flight_id)
                break
        if ok==False:
            raise RepositoryError("Non-existent ID!")
        self.save()

    def list_airports_repo(self):
        count={}
        for i in self._data.values():
            count[i.get_dep_city()]=count.get(i.get_dep_city(), 0)+1
            count[i.get_arr_city()]=count.get(i.get_arr_city(), 0)+1
        sorted_count=dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        list1=list(sorted_count.keys())
        return list1

    def free_time_intervals_repo(self):
        intervals=[]
        for i in self._data.values():
            hour, minute, seconds = i.get_dep_time().split(":")
            hour1, minute1, seconds1 = i.get_arr_time().split(":")
            a=time(int(hour), int(minute), int(seconds))
            b=time(int(hour1), int(minute1), int(seconds1))
            intervals.append((a, b))
        sorted_intervals=sorted(intervals, key=lambda x:x[0])
        final=[]
        if sorted_intervals[0][0]!=time(0, 0, 0):
            final.append((time(0,0,0), sorted_intervals[0][0]))

        if len(sorted_intervals)>=2:
            for i in range(0, len(sorted_intervals)-1):
                if sorted_intervals[i][1]<sorted_intervals[i+1][0]:
                    final.append((sorted_intervals[i][1], sorted_intervals[i+1][0]))
                else:
                    if i==len(sorted_intervals)-2:
                        final.append((max(sorted_intervals[i+1][1], sorted_intervals[i][1]), time(23, 59)))
                    continue

        return final

    def get_all_repo(self):
        return list(self._data.values())
