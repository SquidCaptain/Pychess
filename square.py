from observer import *
from subject import *    
from info import Info

class Square(Observer, Subject):

    def __init__(self, x, y, piece=None, colour=None):
        self._x = x
        self._y = y
        self._colour = colour
        self._piece = piece
        self._danger = False
        self._mate = False
        # for subject
        self._allItem = []
        knights = []
        self._allItem.append(knights)

    def emptySelf(self):
        self._colour = None
        self._piece = None
        self._danger = False
        self._mate = False

    def notify(self, info):
        if info.direction != 0:
            if info.x == self._x:
                self._allItem[info.direction].update(info)    
            elif info.y == self._y:
                self._allItem[info.direction].update(info)
        else: 
            for i in self._allItem[0]:
                i.update(info)

    def _updateDir(self, info):
        if self._piece == "r" or self._piece == "q" or self._piece == "K":
            i = 1
            while i <= 8:
                info.direction = i
                self.notify(info)
                i = i + 2
        if self._piece == "b" or self._piece == "q" or self._piece == "K":
            i = 2
            while i <= 8:
                info.direction = i
                self.notify(info)
                i = i + 2
        updateType = info.type
        if self._piece == "p":
            if self._colour == "w": 
                info.direction = 2
                self.notify(info)
                info.direction = 8
                self.notify(info)
                if updateType == "move1":
                    info.direction = 1
                    self.notify(info)
            else:
                info.info.direction = 4
                self.notify(info)
                info.info.direction = 6
                self.notify(info)
                if updateType == "move1":
                    info.direction = 5
                    self.notify(info)
        if self._piece == "k":
            info.direction = 0
            self.notify(info)

    def update(self, info):
        updateType = info.type
        updatePiece = info.piece
        updateDirec = info.direction
        dy = info.dest_y
        dx = info.dest_x
        if not info.validMove:
            if updateType == "move1" and self._piece == None and self._y == dy and self._x == dx: 
                if updatePiece != "p":
                    info.validMove = True
                    self.emptySelf()
                    self._colour = info.colour
                    self._piece = info.piece
                elif updatePiece == "p" and updateDirec % 2 == 1:
                    info.validMove = True
                    self.emptySelf()
                    self._colour = info.colour
                    self._piece = info.piece
            if self._piece != None:
                if updateType == "threat0":
                    info = Info(self._piece, self._colour, self._y, self._x, "threat1")
                    self._updateDir(info)
                elif updateType == "threat1":
                    self._danger = True
                elif updateType == "move0":
                    info.type = "move1"
                    self._updateDir(info)
                    print("wot")
                    print(info.validMove)############
                    if info.validMove:
                        self.emptySelf()
                elif updateType == "move1": 
                    if self._y == dy and self._x == dx:
                        if info.colour != self._colour and updatePiece != "p":
                            info.validMove = True
                            self.emptySelf()
                            self._colour = info.colour
                            self._piece = info.piece
                        elif info.colour != self._colour and updatePiece == "p" and updateDirec % 2 == 0:
                            info.validMove = True
                            self.emptySelf()
                            self._colour = info.colour
                            self._piece = info.piece
                else:
                    print("\n Update error:" + updateType)
            elif updateType != "threat0" and updateType != "move0" and updatePiece != "K" and updatePiece != "p" and updatePiece != "k":
                self.notify(info)

    def getInfo(self):
        return Info(self._piece, self._colour, self._y, self._x, None)

    def setPiece(self, piece, colour):
        self._piece = piece
        self._colour = colour
    
    def removePiece(self):
        self._piece = None
        self._colour = None

    def observeKnight(self, knight):
        self._allItem[0].append(knight)

    def safe(self):
        self._danger = False
    
    def getDanger(self):
        return self._danger