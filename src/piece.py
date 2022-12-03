import os
from math import inf

class Piece:

    def __init__(self, name, color, value, texture=None, textureRect=None):
        self.name = name
        self.color = color

        # Value sign: + --> black; - --> white
        value_sign = -1 if color == 'white' else 1

        # Black ==> -ve value; White ==> +ve value
        self.value = value * value_sign

        # piece moves
        self.moves = []
        self.moved = False

        # Piece image
        self.texture = texture
        self.setTexture()
        self.textureRect = textureRect
    
    # Image of piece
    def setTexture(self, size=80):
        self.texture = os.path.join(
            f"assets/images/imgs-{size}px/{self.color}_{self.name}.png" # formatted path of png file
        )

    def addMoves(self, move):
        self.moves.append(move)

class Pawn(Piece):
    
    def __init__(self, color):
        # direction of pawn: color
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0) # calling the piece init method

class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.0)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):

    def __init__(self, color):
        super().__init__('king', color, inf)
