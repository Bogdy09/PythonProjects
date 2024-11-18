class Person:
    def __init__(self, id:str, name:str, phone_number:str):
        self._id=id
        self._name=name
        self._phone_number=phone_number

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    @property
    def get_phone_number(self):
        return self._phone_number

    def __str__(self):
        return "ID: "+self._id+" Name: "+self._name+" Phone Number: "+self._phone_number
