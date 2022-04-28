from abc import ABC, abstractmethod
from Game import Game, GameError

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
        while True:
            try: #type and range check
                row = int(input("enter row "))
                col = int(input("enter column "))
                if 1 <= row <= 3 and 1<= col <= 3:
                    break
                else:
                    print("Invalid Input, Try Again")
                break
            except ValueError:
                print("Invalid Input, Try Again")
        return row, col

    def run(self):
        while self.__Game.winner == None:
            print(self.__Game)
            row, col = self.__get_input()
            try:
                self.__Game.play(row, col)
            except GameError:
                pass
        
        print(self.__Game)
        if self.__Game.winner == Game.DRAW:
            print("game is a draw")
        else:
            print(f"the winner is {self.__Game.winner}")
