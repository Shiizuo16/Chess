import pygame
import sys

from const import *
from game import Game


class Main:

    def __init__(self):
        pygame.init()

        # Creating game screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('CHESS')
        
        # Game object
        self.game = Game()

    def mainloop(self):
        
        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # Displaying background and pieces
            game.showBackground(screen)
            game.showPieces(screen)

            if dragger.dragging:
                dragger.updateBlit(screen)

            # Looking for events - key press, button press, etc
            for event in pygame.event.get():

                # mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.updateMouse(event.pos)

                    clickedRow = dragger.mouseY // sqSize
                    clickedCol = dragger.mouseX // sqSize

                    # if clicked square has piece
                    if board.squares[clickedRow][clickedCol].hasPiece():
                        piece = board.squares[clickedRow][clickedCol].piece
                        dragger.dragPiece(piece)

                        # saving initial pos of piece
                        dragger.saveInitial(event.pos)



                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.updateMouse(event.pos)
                        # dragger.updateBlit(screen)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undragPiece()

                # exit application; pressing quit button
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Updates the game screen
            pygame.display.update()

main = Main()
main.mainloop()