
import tkinter as tk
from tkinter import Tk

class Interface():
    
    def __init__(self, boardState=None):
        self.board = []
        self.updated = True
        self._setNew()

    def _setNew(self):
        self.board = []
        redudant  = 0
        for i in range(8):
            temp = []
            redudant += i
            for j in range(8):
                temp.append(None)
                redudant += j
            self.board.append(temp)
    
    def setState(self, state):
        self.updated = True
        self._setNew()
        if state != None:
            for piece in state:
                if len(piece) != 1:
                    self.board[ord(piece[3])-97][ord(piece[2])-49] = piece[1]

    def textDisplay(self):
        x = 8
        y = 1
        while x >= 1:
            s = ""
            while y <= 8:
                item = self.board[y-1][x-1]
                if item == None:
                    s += "-"
                else:
                    s += item
                y += 1
            print(s)
            y = 1
            x -= 1
    
    def imgDisplay(self):
        img = Tk()
        img.title("TeeHee")
        img.geometry("500x300")