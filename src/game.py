import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.started = False


    # Show Methods

    def showBackground(self, surface):
        for row in range(rows):
            for col in range(cols):
                # Picking color of rectangle
                if (row + col) % 2 == 0:
                    color = (241,217,192) # Soft yellow
                else:
                    color = (169, 122, 101) # brown

                # Rectangular piece on board
                rect = (col*sqSize, row*sqSize, sqSize, sqSize)

                # Drawing the rectangle
                pygame.draw.rect(surface, color, rect)
                
    def showPieces(self, surface):
         for row in range(rows):
            for col in range(cols):
                # square has piece?
                if self.board.squares[row][col].hasPiece():
                    # saving piece to variable
                    piece = self.board.squares[row][col].piece

                    # piece image except dragger piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        imgCenter = col * sqSize + sqSize // 2, row * sqSize + sqSize // 2 # to center the image
                        piece.textureRect = img.get_rect(center= imgCenter) # centered piece image

                        surface.blit(img, piece.textureRect) # putting img in the textureRect rectangle