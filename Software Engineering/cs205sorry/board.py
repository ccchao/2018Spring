"""
    CS205: Sorry! Final Project
    File name: board.py
    Main author: Chia-Chun Chao
    Change structure: Joe Embrey
"""

import sys, pygame


class Board:
    def __init__(self, main):
        self.main = main
        self.map = Map(main)


"""
        #Load deck
        self.deck = pygame.image.load('images/deck.png').convert_alpha()
        self.deck = pygame.transform.rotozoom(self.deck, 0, self.main.scale)

        #Load pawns
        self.pawnYellow = pygame.image.load('images/pawn_yellow.png').convert_alpha()
        self.pawnYellow = pygame.transform.rotozoom(self.pawnYellow, 0, self.main.scale*0.5)
        self.pawnGreen = pygame.image.load('images/pawn_green.png').convert_alpha()
        self.pawnGreen = pygame.transform.rotozoom(self.pawnGreen, 0, self.main.scale*0.5)
        self.pawnRed = pygame.image.load('images/pawn_red.png').convert_alpha()
        self.pawnRed = pygame.transform.rotozoom(self.pawnRed, 0, self.main.scale*0.5)
        self.pawnBlue = pygame.image.load('images/pawn_blue.png').convert_alpha()
        self.pawnBlue = pygame.transform.rotozoom(self.pawnBlue, 0, self.main.scale*0.5)"""

        #self.main.screen.blit(self.deck, (56*self.main.scale + 456*self.main.scale, 56*self.main.scale + 392*self.main.scale))


class Map:
    def __init__(self, main):
        self.main = main
        self.layer = 1
        self.main.activeObj.add(self)
        colorToAngle = {'red': 90, 'blue': 180, 'green': 0, 'yellow': 270}
        self.map = pygame.image.load('images/map_1400.png').convert_alpha()
        self.map = pygame.transform.rotozoom(self.map, colorToAngle[self.main.color], self.main.scale)


    def draw(self):
        #self.rect = self.main.screen.blit(self.map, (56*self.main.scale, 56*self.main.scale))
        self.rect = self.main.screen.blit(self.map, (self.main.scale, self.main.scale))

    def tick(self):
        pass

    def onClick(self):
        pass
