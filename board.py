
from square import Square
from observer import *

class Board(Observer):

    def __init__(self, boardState=None):
        self._graveyard = []
        self._kings = []
        self._game = self.setBoard(self.newBoard(), boardState)
        self._gameMoves = []
        self._history = []
        self._turn = "w"
    
    def bounded(self, x, y):
        if x > 8 or y > 8 or x < 1 or y < 1:
            return False
        else:
            return True

    def _observeTarget(self, board, square, x, y, index=1):
        if self.bounded(x, y):
            square.attatch(index, board[x-1][y-1])
        else:
            square.attatch(index, self)

    def _observeSquares(self, board, square, x, y):
        #knights
        self._observeTarget(board, square, x-1, y+2, 0)
        self._observeTarget(board, square, x-1, y-2, 0)
        self._observeTarget(board, square, x-2, y+1, 0)
        self._observeTarget(board, square, x-2, y-1, 0)
        self._observeTarget(board, square, x+1, y+2, 0)
        self._observeTarget(board, square, x+1, y-2, 0)
        self._observeTarget(board, square, x+2, y+1, 0)
        self._observeTarget(board, square, x+2, y-1, 0)
        #clockwise around piece
        self._observeTarget(board, square, x, y+1)
        self._observeTarget(board, square, x+1, y+1)
        self._observeTarget(board, square, x+1, y)
        self._observeTarget(board, square, x+1, y-1)
        self._observeTarget(board, square, x, y-1)
        self._observeTarget(board, square, x-1, y-1)
        self._observeTarget(board, square, x-1, y)
        self._observeTarget(board, square, x-1, y+1)

    def newBoard(self):
        y = 1
        x = 1
        board = []
        while x <= 8:
            temp = []
            board.append(temp)
            while y <= 8:
                temp.append(None)
                y += 1
            y = 1
            x += 1
        x = 1
        while x <= 8 and y <= 8:
            board[x-1][y-1] = Square(x, y)
            if x == 8:
                y += 1
                x = 1
            else:
                x += 1
        x = 1
        y = 1
        while x < 8:
            while y < 8:
                self._observeSquares(board, board[x-1][y-1], x, y)
                y += 1
            y = 1
            x += 1
        return board

    def setBoard(self, board, boardState=None):
        if boardState == None:
            boardState = ["br8a", "bk8b", "bb8c", "bq8d", "bK8e", "bb8f", "bk8g", "br8h",
                          "bp7a", "bp7b", "bp7c", "bp7d", "bp7e", "bp7f", "bp7g", "bp7h",
                          "wp2a", "wp2b", "wp2c", "wp2d", "wp2e", "wp2f", "wp2g", "wp2h",
                          "wr1a", "wk1b", "wb1c", "wq1d", "wK1e", "wb1f", "wk1g", "wr1h", "w"]
        for piece in boardState:
            if len(piece) == 1:
                self._turn = piece
            else:
                if str(piece[1]) == "K":
                    self._kings.append(board[ord(piece[3])-97][ord(piece[2])-49])
                board[ord(piece[3])-97][ord(piece[2])-49].setPiece(piece[1], piece[0])
        return board
    
    def getState(self):
        x = 1
        y = 1
        state = []
        state.append(self._turn)
        while x <= 8:
            while y <= 8:
                info = self._game[x-1][y-1].getInfo()
                if info.piece != None:
                    state.append(info.colour + info.piece + str(info.y) + str(chr(info.x + 96)))
                y += 1
            y = 1
            x += 1
        return state

    def move(self, move):
        # ie. move = "2a3a" # move pawn from 2a to 3a
        y = (ord(move[0])-49) + 1
        x = (ord(move[1])-97) + 1
        targ_y = (ord(move[2])-49) + 1
        targ_x = (ord(move[3])-97) + 1
        if self.bounded(x, y) and self.bounded(targ_x, targ_y):
            info = self._game[x-1][y-1].getInfo()
            info.dest_y = targ_y
            info.dest_x = targ_x
            if info.piece != None and info.colour == self._turn:
                info.type = "move0"
                prevSave = self.getState()
                self._game[x-1][y-1].update(info)
                if not info.validMove:
                    self._game = self.setBoard(self.newBoard(), prevSave)
                    print("\n--Invalid Move--\n")
                else:
                    self._gameMoves.append(move)
            else:
                print("\n--Invalid Move--\n")
        else:
            print("\n--Invalid Move--\n")
        if self._turn == "w":
            self._turn = "b"
        else:
            self._turn = "w"


    def archive(self):
        self._history.append([self._game, self._gameMoves])