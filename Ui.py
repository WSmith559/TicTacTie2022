from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.__Game = Game()

    def __get_input(self):
        row = int(input("enter row"))
        col = int(input("enter column"))
        return row, col

    def run(self):
        while self.__Game.winner == None:
            print(self.__Game)
            row, col = self.__get_input()
            self.__game.play(row, col)
        
        print(f"the winner is {self.__Game.winner}")
