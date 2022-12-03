import pygame
from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initialRow = 0
        self.initialCol = 0

    # Blit methods
    def updateBlit(self, surface):
        # texture
        self.piece.setTexture(size=128)
        texture = self.piece.texture

        # piece img
        img = pygame.image.load(texture)

        # rect
        imgCenter = (self.mouseX, self.mouseY)
        self.piece.textureRect = img.get_rect(center=imgCenter)

        # blit
        surface.blit(img, self.piece.textureRect)


    # Other methods
    def updateMouse(self, pos):
        self.mouseX, self.mouseY = pos  # (xcor, ycor)

    def saveInitial(self, pos):
        self.initialRow = pos[1] // sqSize
        self.initialCol = pos[0] // sqSize

    def dragPiece(self, piece):
        self.piece = piece
        self.dragging = True

    def undragPiece(self):
        self.piece.setTexture(size=80)
        self.piece = None
        self.dragging = False
