## A class that implements oberserver

class Observer:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._piece = None
        self._colour = False
        
    def update(self, info):
        return None
    