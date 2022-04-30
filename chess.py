from board import Board
from interface import Interface

board = Board()

state = board.getState()

interface = Interface()
interface.setState(state)

interface.imgDisplay()


gameloop = True
while gameloop:
    if interface.updated:
        interface.updated = False
        interface.textDisplay()
    player = input("input: ")
    if player == "end":
        gameloop = False
    elif player == "a":
        move0 = input("move: ")
        board.move(move0)
        state = board.getState()
        interface.setState(state)

    