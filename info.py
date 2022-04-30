
## piece = piece started prop
## y = row of piece
## x = column of piece
## type = type of propogation (ie normal move, eaten, threaten)
class Info:
    def __init__(self, piece, colour, y, x, t, d=None, dest_y=None, dest_x=None):
        self.piece = piece
        self.colour = colour
        self.y = y
        self.x = x
        self.type = t
        self.direction = d
        self.dest_y = dest_y
        self.dest_x = dest_x
        self.validMove = False
"""
    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def getType(self):
        return self._type
    
    def setType(self, t):
        self._type = t
    
    def getPiece(self):
        return self._piece

    def getColour(self):
        return self._colour

    def getDirection(self):
        return self._direction
    
    def setDirection(self, direction):
        self._direction = direction

    def getDest_y(self):
        return self._dest_y

    def getDest_x(self):
        return self._dest_x
    
    def target(self, y, x):
        self._dest_y = y
        self._dest_x = x

    def setValid(self, v):
        self._validMove = v

    def valid(self):
        return self._validMove
"""        