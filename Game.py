class Game:

    EMPTY = " "
    P1 = "O"
    P2 = "X"

    def __init__(self):
        self.__board = [[Game.EMPTY for _ in range(3)] for _ in range(3)]
        self.__player = Game.P1

    def __repr__(self):
        return("this is the board")

    def play(self,row,col):
        row -= 1
        col -= 1
        self.__board[row][col] = self.__player
        if self.__player == Game.P1:
            self.__player = Game.P2
        elif self.__player == Game.P2:
            self.__player = Game.P1
    
    @property
    def winner(self):
        return None
        
if __name__ == "__main__":
    pass
