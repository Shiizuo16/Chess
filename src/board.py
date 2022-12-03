from const import *
from square import Square
from piece import *

class Board:

    def __init__(self):
        self.squares = []

        # 2-D board array
        self.createBoard()

        # Adding Pieces to the array
        self.addPiece('white')
        self.addPiece('black')

    def calcMoves(self, piece, row, col):
        '''
            Calculate all the possible (valid) moves of a specific piece on a specific position
        '''
        pass

    def createBoard(self):

        # Initializing the squares w/ 0
        self.squares = [[0 for col in range(cols)] for row in range(rows)] 

        # Adding square objects to the squares array
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col)
 
    def addPiece(self, color):
        # if color == 'white':
        #     rowPawn, rowOther = (1, 0)
        # else:
        #     rowPawn, rowOther = (6, 7)
        rowPawn, rowOther = (6,7) if color == 'white' else (0,1) # row of pawns and other pieces

        # Pawns
        for col in range(cols):
            self.squares[rowPawn][col] = Square(rowPawn, col, Pawn(color))


        # Knights
        self.squares[rowOther][1] = Square(rowOther, 1, Knight(color))
        self.squares[rowOther][6] = Square(rowOther, 6, Knight(color))

        # Bishops
        self.squares[rowOther][2] = Square(rowOther, 2, Bishop(color))
        self.squares[rowOther][5] = Square(rowOther, 5, Bishop(color))

        # Rooks
        self.squares[rowOther][0] = Square(rowOther, 0, Rook(color))
        self.squares[rowOther][7] = Square(rowOther, 7, Rook(color))

        # Queen
        self.squares[rowOther][3] = Square(rowOther, 3, Queen(color))

        # King
        self.squares[rowOther][4] = Square(rowOther, 4, King(color))

