from abc import ABC, abstractmethod
from Game import Game, GameError
from tkinter import *
from itertools import product

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
        self.__Game = Game()

        game_win = Toplevel(self.__root)
        game_win.title = ("Game")
        frame = Frame(game_win)
        frame.grid(row=0, column=0)

        self.__buttons = [[None for _ in range(3)] for _ in range(3)]
        for row, col in product(range(3), range(3)):
            b = StringVar()
            b.set(self.__Game.at(row+1, col+1))
            self.__buttons[row][col] = b

            cmd = lambda r=row, c=col: self.__play(r,c)
            Button(
                game_win,
                textvariable=b,
                command=cmd
            ).grid(row=row,column=col)
        
        Button(game_win, text="dismiss", command=game_win.destroy).grid(row=3, column=1)

    def __play(self,r,c):
        self.__Game.play(r+1,c+1)
        self.__buttons[r][c].set(self.__Game.at(r+1,c+1))

    def __quit(self):
        self.__root.quit()

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
