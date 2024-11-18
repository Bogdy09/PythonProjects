class Taxi:
    def __init__(self, x, y, id, fare):
        self._x=x
        self._y=y
        self._id=id
        self._fare=fare
        
    @property
    def get_x(self):
        return self._x

    @property
    def get_y(self):
        return self._y

    @property
    def get_id(self):
        return self._id

    def __str__(self):
        return "Coordinates: "+"( "+str(self._x)+", "+str(self._y)+" ) "+ "ID: "+self._id+ " Fare: "+str(self._fare)

    @property
    def get_fare(self):
        return self._fare