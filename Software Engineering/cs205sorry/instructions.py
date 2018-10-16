"""
    CS205: Sorry! Final Project
    File name: instructions.py
    Main author: Gavin Gunkle
"""
#Instructions on how to play the game
#from menu import menu
from board import Board
###still need to incorporate gui design into showing instructions

import pygame

def Instructions():

    #pygame.init()

    #instructionsDisplay = pygame.display.set_mode((800,600))
    #pygame.display.set_caption('Instructions for SORRY!')

    #should be its own gui
    #basicfont = pygame.font.SysFont(None, 48)
    #text = basicfont.render('Hello World!', True, (255, 0, 0), (255, 255, 255))
    #textrect = text.get_rect()
    #self.main.screen.blit(text, textrect)

    print('Instructions for SORRY!')
    print('OBJECTIVE: The first player to move all four of their ' +
          'pawns from START to HOME wins.')
    print('SETUP: To begin the game, the user must select a color, and ' +
          'the difficulty/agressisveness of the computer players')
    print('Computer Options:')
    print('Easy: The computer plays the game at random')
    print('Hard: The computer calculates the best move to make each turn')
    print('Passive: The commputer will try not to knock any pieces during its turn')
    print('Aggressive: The computer will always try and knock pieces if possible')

    print('CARDS:')
    print('1: Move one pawn from START or move one pawn 1 space')
    print('2: Move one pawn from START and draw again or move 2 spaces and ' +
          'draw again. If you cannot move, still draw again.')
    print('3: Move a pawn forward 3 spaces')
    print('4: Move a pawn backward 4 spaces')
    print('5: Move a pawn forward 5 spaces')
    print('7: Move a pawn forward 7 spaces or split the move between any two pawns')
    print('8: Move a pawn forward 8 spaces')
    print('10: Move a pawn forward 10 spaces or move a pawn backward 1 space')
    print('11: Move a pawn forward 11 spaces or switch any of your pawns with any ' +
          'opponents. (If you cannot move 11, you do not have to switch places with ' +
          'an opponent)')
    print('12: Move a pawn forward 12 spaces')
    print('SORRY!: Take a pawn from START, place it on any space occupied by an opponent ' +
          'and bump the opponent back to start.')

    print('MOVEMENT: The game will show you what your options for movement are ' +
          'and you must click which option you would like. If at any time you can move, ' +
          'you must move, even if it puts you at a disadvantage.')

    print('BUMPING: If you land on a space occupied by an opponent, BUMP ' +
          'the opponents piece back to their START. Players cannot BUMP their own ' +
          'pieces, (unless in a SLIDE), and cannot occupy two pieces on the same space. If the player cannot move, the turn ' +
          'is forfeited.')

    print('SAFETY ZONE: Only you may enter your own color SAFETY ZONE. You cannot ' +
          'be BUMPED by other players in this zone. All rules still apply with movement.')

    print('SLIDE: If you land on the beginning of the slide of any color but your own, ' +
          'BUMP any pawns in your way (including your own). If you are on your ' +
          'color SLIDE, do not slide and stay on the beginning of the slide.')

    print('OPTIONS: This game allows the user to save the current state of the game ' +
          'and resume later by clicking the SAVE button. There is also a QUIT button ' +
          'which exits to the main menu.')

    #add button options to return to the game

#instructions()
