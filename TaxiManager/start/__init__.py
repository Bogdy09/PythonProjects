from random import randint
from UI.ui import UI


def generate_ids(n):
    ids=set()
    while(len(ids)<n):
        nr=randint(1, 999)
        ids.add(nr)
    return list(ids)

def generate_coordinates(n):
    coordinates=[]
    while(len(coordinates)<n):
        x=int(randint(0, 100))
        y=int(randint(0, 100))
        if not coordinates:
            coordinates.append((x, y))
        else:
            ok=True
            for i, j in coordinates:
                    if abs(x-i)+abs(y-j)<=5:
                        ok=False
            if ok==True:
                coordinates.append((x, y))

    return coordinates


list_of_ids=generate_ids(10)
list_of_coordinates=generate_coordinates(10)
ui=UI(list_of_ids, list_of_coordinates)
ui.menu()

