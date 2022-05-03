from abc import ABC, abstractmethod
from Game import Game, GameError
from tkinter import *

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("TicTacToe")
        frame = Frame(root)
        frame.pack()

        Button(
            frame, 
            text="help",
            command=self.__show_help
        ).pack(fill=X)
        Button(
            frame, 
            text="play",
            command=self.__play_game
        ).pack(fill=X)
        Button(
            frame, 
            text="quit",
            command=self.__quit
        ).pack(fill=X)
        self.__root = root

    def __show_help(self):
        pass

    def __play_game(self):
        pass

    def __quit(self):
        self.__root.quit

    def run(self):
        self.__root.mainloop()

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
