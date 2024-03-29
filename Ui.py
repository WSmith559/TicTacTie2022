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
        self.__game_win = None
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

        scroll = Scrollbar(frame)
        console = Text(frame, height=4, width=50)
        scroll.pack(side=RIGHT, fill=Y)
        console.pack(side=LEFT, fill=Y)

        scroll.config(command= console.yview)
        console.config(yscrollcommand=scroll.set)

        self.__root = root
        self.__console = console

    def __show_help(self):
        pass

    def __play_game(self):
        self.__finished=False
        self.__Game = Game()

        game_win = Toplevel(self.__root)
        game_win.title = ("Game")
        frame = Frame(game_win)
        #frame.grid(row=0, column=0)

        Grid.columnconfigure(game_win, 0, weight=1)
        Grid.rowconfigure(game_win, 0, weight=1)
        frame.grid(row=0, column=0, sticky=N+S+E+W)

        self.__buttons = [[None for _ in range(3)] for _ in range(3)]
        for row, col in product(range(3), range(3)):
            b = StringVar()
            b.set(self.__Game.at(row+1, col+1))
            self.__buttons[row][col] = b

            cmd = lambda r=row, c=col: self.__play(r,c)
            Button(
                frame,
                textvariable=b,
                command=cmd
            ).grid(row=row,column=col,sticky=N+S+E+W)
        
        for i in range(3):
            Grid.rowconfigure(frame, i, weight=1)
            Grid.columnconfigure(frame,i,weight=1)

        self.__game_win = game_win
        Button(game_win, text="dismiss", command=self.__dismiss_game_win).grid(row=1, column=0)

    def __dismiss_game_win(self):
        self.game_win.destroy()
        self.game_win = None

    def __play(self,r,c):
        if self.__finished:
            return

        try:
            self.__Game.play(r+1,c+1)
        except GameError as e:
            self.__console.insert(END, f"{e}\n")

        self.__buttons[r][c].set(self.__Game.at(r+1,c+1))

        if self.__Game.winner ==Game.DRAW:
            self.__console.insert(END, "game is drawn\n")
            self.__finished = True
        elif self.__Game.winner:
            self.__console.insert(END,f"game was won by {self.__Game.winner}\n")
            self.__finished = True


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
