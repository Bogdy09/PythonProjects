class Taxi_repo:
    def __init__(self):
        self._data={}

    def add_taxi_repo(self, new_taxi):
        self._data[new_taxi._id]=new_taxi

    def print_repo(self):
        for i in self._data.values():
            print(i)

    def get_ids_repo(self):
        ids=[]
        for i in self._data.values():
            if i._id is not None:
                ids.append(i._id)
        return list(ids)

    def get_coordinates_repo(self):
        coordinates=[]
        for i in self._data.values():
            coordinates.append((i._x, i._y))
        return coordinates

    def find_by_coordinates_repo(self, a, b):
        for i in self._data.values():
            if i._x==a and i._y==b:
                return i

    def find_all_taxis_repo(self):
        list1=[]
        for i in self._data.values():
            list1.append(i)
        return list1