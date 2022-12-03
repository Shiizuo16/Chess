class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece  # Square may/may not have a piece; default- None

    def hasPiece(self):
        return self.piece != None