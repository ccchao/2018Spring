"""
    File name: playing.py
    Main author: Joe Embrey
    Author of resume: Peter Macksey
    Author of instructions: Gavin Gunkle
"""

import pygame
from board import Board
from instructions import Instructions
from database import Database
import sys
from game import Game
from save import Save
from load import Load
from deck import Deck


#this is created when the game is initialized,
class Menu:
    def __init__(self, main):
        self.main = main
        self.main.activeObj = set()
        #welcome image
        welcome = Button(self.main, 84, 68, "none", "images/welcome.png", 0.5)
        #buttons for main menu
        newGame = Button(self.main, 150, 380, "new", "images/newgame.png", 1)
        resumeGame = Button(self.main, 330, 380, "resume", "images/resumegame.png", 1)
        instructions = Button(self.main, 150, 450, "instructions", "images/instructions.png", 1)
        statistics = Button(self.main, 330, 450, "stats", "images/stats.png", 1)
        quit = Button(self.main, 240, 520, "quit", "images/quit.png", 1)

#created when the game ends, shows the end game summery
class WinScreen:
    def __init__(self, main, color):
        self.main = main
        self.main.activeObj = set()
        if color == self.main.color:
            Text(self.main, 150, 120, 40, 'Congratulations!')
        else:
            Text(self.main, 210, 90, 70, 'Sorry!')
        Text(self.main, 200, 200, 30, 'Winner:     ' + color)
        Text(self.main, 190, 280, 30, 'Game summary')
        Text(self.main, 150, 350, 22, 'Turns taken: ' + str(self.main.turnsTaken))
        Text(self.main, 150, 380, 22, 'Spaces moved: ' + str(self.main.spacesMoved))
        Text(self.main, 150, 410, 22, 'Bumped others: ' + str(self.main.playersBumped))
        Text(self.main, 150, 440, 22, 'Bumped by others: ' + str(self.main.bumpedByOthers))
        Text(self.main, 150, 470, 22, 'Cards drawn: ' + str(self.main.cardsDrawn))
        back = Button(self.main, 240, 520, "reset", "images/quit.png", 1)


class Button:
    def __init__(self, main, x, y, action, img, scale):
        self.action = action
        self.main = main
        self.x, self.y = x, y
        self.layer = 0
        self.main.activeObj.add(self)
        self.scale = scale
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, self.scale)

    def draw(self):
        self.rect = self.main.screen.blit(self.img, (self.x, self.y))

    def tick(self):
        pass

    def onClick(self):
        if self.action == "new":
            self.newGame()
        if self.action == "pickcolor":
            self.pickColor()
        if self.action == "instructions":
            self.instructions()
        if self.action == "back":
            self.back()
        if self.action == "backInstructions":
            self.backInstructions()
        if self.action == "setUpInstructions":
            self.setUpInstructions()
        if self.action == "gameplayInstructions":
            self.gameplayInstructions()
        if self.action == "cardInstructions":
            self.cardInstructions()
        if self.action == "stats":
            self.stats()
        if self.action == "resume":
            self.resume()
        if self.action == "red" or self.action == "blue" or self.action == "yellow" or self.action == "green":
            self.pickNumPlayers()
        if self.action == "numplayersone" or self.action == "numplayerstwo" or self.action == "numplayersthree":
            self.setDifficulty()
        if self.action == "nicedumb" or self.action == "nicesmart" or self.action == "meandumb" or self.action == "meansmart":
            self.setUpBoard()
        if self.action[:3] == "pc1" or self.action[:3] == "pc2" or self.action[:3] == "pc3":
            self.setPC()
        if self.action == "done":
            self.setUpBoard()
        if self.action == "quit":
            sys.exit()
        if self.action == "reset":
            self.main.quit()

    def newGame(self):
        self.main.activeObj = set()
        enterNameTxt = Text(self.main, 176, 250, 30, 'Please enter a name:')
        nameTxt = NameText(self.main, 200, 310, 26)
        self.main.textInput = True
        self.main.activeObj.add(Button(self.main, 190, 300, "", "images/textbox.png", 1))
        self.main.activeObj.add(Button(self.main, 240, 400, "pickcolor", "images/done.png", 1))

    def pickColor(self):
        if self.main.playerName != '':
            self.textInput = False
            self.main.activeObj = set()
            pickColorTxt = Text(self.main, 176, 250, 30, 'Please pick a color:')
            self.main.activeObj.add(Button(self.main, 120, 300, "red", "images/pawn_red.png", 0.5))
            self.main.activeObj.add(Button(self.main, 220, 300, "blue", "images/pawn_blue.png", 0.5))
            self.main.activeObj.add(Button(self.main, 320, 300, "yellow", "images/pawn_yellow.png", 0.5))
            self.main.activeObj.add(Button(self.main, 420, 300, "green", "images/pawn_green.png", 0.5))

    def pickNumPlayers(self):
        print('Player color is ' + self.action)
        self.main.color = self.action
        self.main.activeObj = set()
        pickNumPlayersTxt = Text(self.main, 110, 250, 30, 'How many computer players?')
        self.main.activeObj.add(Button(self.main, 130, 300, "numplayersone", "images/one.png", 0.5))
        self.main.activeObj.add(Button(self.main, 265, 300, "numplayerstwo", "images/two.png", 0.5))
        self.main.activeObj.add(Button(self.main, 410, 300, "numplayersthree", "images/three.png", 0.5))

    def setDifficulty(self):
        if self.action == "numplayersone":
            self.main.numPlayers = "one"
        if self.action == "numplayerstwo":
            self.main.numPlayers = "two"
        if self.action == "numplayersthree":
            self.main.numPlayers = "three"
        print('Number of PC players: ' + self.main.numPlayers)
        self.main.activeObj = set()
        pickDifficultyTxt = Text(self.main, 140, 100, 30, 'How hard should this be?')
        pc1Text = Text(self.main, 70, 185, 30, 'PC1')
        self.main.activeObj.add(Button(self.main, 140, 150, "pc1nicedumb", "images/nicedumb.png", 0.5))
        self.main.activeObj.add(Button(self.main, 250, 150, "pc1nicesmart", "images/nicesmart.png", 0.5))
        self.main.activeObj.add(Button(self.main, 360, 150, "pc1meandumb", "images/meandumb.png", 0.5))
        self.main.activeObj.add(Button(self.main, 470, 150, "pc1meansmart", "images/meansmart.png", 0.5))
        if self.action == "numplayerstwo" or self.action == "numplayersthree":
            pc2Text = Text(self.main, 70, 305, 30, 'PC2')
            self.main.activeObj.add(Button(self.main, 140, 270, "pc2nicedumb", "images/nicedumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 250, 270, "pc2nicesmart", "images/nicesmart.png", 0.5))
            self.main.activeObj.add(Button(self.main, 360, 270, "pc2meandumb", "images/meandumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 470, 270, "pc2meansmart", "images/meansmart.png", 0.5))
        if self.action == "numplayersthree":
            pc3Text = Text(self.main, 70, 425, 30, 'PC3')
            self.main.activeObj.add(Button(self.main, 140, 390, "pc3nicedumb", "images/nicedumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 250, 390, "pc3nicesmart", "images/nicesmart.png", 0.5))
            self.main.activeObj.add(Button(self.main, 360, 390, "pc3meandumb", "images/meandumb.png", 0.5))
            self.main.activeObj.add(Button(self.main, 470, 390, "pc3meansmart", "images/meansmart.png", 0.5))
        self.main.activeObj.add(Button(self.main, 250, 520, "done", "images/done.png", 1))

    def setPC(self):
        pc = 0
        if self.action[:3] == "pc1":
            self.main.pc1difficulty = self.action[3:]
        if self.action[:3] == "pc2":
            self.main.pc2difficulty = self.action[3:]
        if self.action[:3] == "pc3":
            self.main.pc3difficulty = self.action[3:]
        for obj in self.main.activeObj:
            if obj.y >= 150 and obj.y <= 390 and obj.x >= 140:
                if obj.action[:3] == self.action[:3]:
                    if obj.action[3:] != self.action[3:]:
                        obj.img = pygame.image.load("images/" + obj.action[3:] + ".png").convert_alpha()
                        obj.img = pygame.transform.rotozoom(obj.img, 0, obj.scale)
                    else:
                        obj.img = pygame.image.load("images/" + obj.action[3:] + "_pressed.png").convert_alpha()
                        obj.img = pygame.transform.rotozoom(obj.img, 0, obj.scale)


    def instructions(self):
        self.main.activeObj = set()
        pickColorTxt = Text(self.main, 230, 70, 30, 'Instructions')
        setUpInstructions = Button(self.main, 240, 150, "setUpInstructions", "images/setup.png", 1)
        cardInstructions = Button(self.main, 240, 225, "cardInstructions", "images/cards.png", 1)
        gameplayInstructions = Button(self.main, 240, 300, "gameplayInstructions", "images/gameplay.png", 1)
        back = Button(self.main, 240, 375, "back", "images/back.png", 1)


    def setUpInstructions(self):
        self.main.activeObj = set()
        content0 = Text(self.main, 175, 70, 30, 'Set Up Instructions')
        content1 = Text(self.main, 70, 140, 15, 'SETUP: To begin the game, the user must select a color, and the')
        content2 = Text(self.main, 70, 165, 15, 'difficulty/agressisveness of the computer players')
        space = Text(self.main, 70, 190, 15, '***************************************************************************')
        content3 = Text(self.main, 70, 215, 15, 'Computer Options:')
        content4 = Text(self.main, 70, 240, 15, 'Easy: The computer plays the game at random')
        content5 = Text(self.main, 70, 265, 15, 'Hard: The computer calculates the best move to make each turn')
        content6 = Text(self.main, 70, 290, 15, 'Passive: The computer will try not to knock any pieces during its turn')
        content7 = Text(self.main, 70, 315, 15, 'Aggressive: The computer will always try and knock pieces if possible')
        backInstruction = Button(self.main, 240, 340, "backInstructions", "images/instructions.png", 1)


    def cardInstructions(self):
        self.main.activeObj = set()
        title = Text(self.main, 175, 70, 30, 'Card Instructions')
        content0 = Text(self.main, 50, 115, 15, 'Card 1: Move one pawn from START or move one pawn 1 space')
        content1 = Text(self.main, 50, 140, 15, 'Card 2: Move one pawn from START and draw again or move 2 spaces and')
        content2 = Text(self.main, 50, 165, 15, 'draw again. If you cannot move, still draw again.')
        content3 = Text(self.main, 50, 190, 15, 'Card 3: Move a pawn forward 3 spaces')
        content4 = Text(self.main, 50, 215, 15, 'Card 4: Move a pawn backward 4 spaces')
        content5 = Text(self.main, 50, 240, 15, 'Card 5: Move a pawn forward 5 spaces')
        content6 = Text(self.main, 50, 265, 15, 'Card 7: Move a pawn forward 7 spaces or split the move between any')
        content7 = Text(self.main, 50, 290, 15, 'two pawns')
        content8 = Text(self.main, 50, 315, 15, 'Card 8: Move a pawn forward 8 spaces')
        content9 = Text(self.main, 50, 340, 15, 'Card 10: Move a pawn forward 10 spaces or move a pawn backward 1 space')
        content10 = Text(self.main, 50, 365, 15, 'Card 11: Move a pawn forward 11 spaces or switch any of your pawns')
        content11 = Text(self.main, 50, 390, 15, 'with any opponent. (If you cannot move 11, you do not have to switch')
        content12 = Text(self.main, 50, 415, 15, 'places with an opponent)')
        content13 = Text(self.main, 50, 440, 15, 'Card 12: Move a pawn forward 12 spaces')
        content14 = Text(self.main, 50, 465, 15, 'SORRY!: Take a pawn from START, place it on any space occupied by an')
        content15 = Text(self.main, 50, 490, 15, 'opponent and bump the opponent back to start.')
        backInstruciton = Button(self.main, 240, 510, "backInstructions", "images/instructions.png", 1)

    def gameplayInstructions(self):
        self.main.activeObj = set()
        title = Text(self.main, 170, 60, 30, 'Gameplay Instructions')
        content0 = Text(self.main, 50, 115, 15, 'MOVEMENT: The game will show you what your options for movement are')
        content1 = Text(self.main, 50, 140, 15, 'and you must click which option you would like. If at any time you')
        content2 = Text(self.main, 50, 165, 15, 'can move, you must move, even if it puts you at a disadvantage.')
        content3 = Text(self.main, 50, 190, 15, '*******************************************************************')
        content4 = Text(self.main, 50, 215, 15, 'BUMPING: If you land on a space occupied by an opponent, BUMP')
        content5 = Text(self.main, 50, 240, 15, 'the opponents piece back to their START. Players cannot BUMP their own')
        content6 = Text(self.main, 50, 265, 15, 'pieces, (unless in a SLIDE), and cannot occupy two pieces on the same ')
        content7 = Text(self.main, 50, 290, 15, 'space. If the player cannot move, the turn is forfeited.')
        content8 = Text(self.main, 50, 315, 15, '*******************************************************************')
        content9 = Text(self.main, 50, 340, 15, 'SAFETY ZONE: Only you may enter your own color SAFETY ZONE. You cannot')
        content10 = Text(self.main, 50, 365, 15, 'be BUMPED by other players in this zone. All rules still apply with movement.')
        content11 = Text(self.main, 50, 390, 15, '*******************************************************************')
        content12 = Text(self.main, 50, 415, 15, 'SLIDE: If you land on the beginning of the slide of any color but your own,')
        content13 = Text(self.main, 50, 440, 15, 'BUMP any pawns in your way (including your own). If you are on your')
        content14 = Text(self.main, 50, 465, 15, 'color SLIDE, do not slide and stay on the beginning of the slide.')
        content15 = Text(self.main, 50, 490, 15, '*******************************************************************')
        content13 = Text(self.main, 50, 515, 15, 'OPTIONS: This game allows the user to save the current state of the game')
        content14 = Text(self.main, 50, 540, 15, 'and resume later by clicking the SAVE button. There is also a QUIT button')
        content15 = Text(self.main, 50, 565, 15, 'which exits to the main menu.')
        backInstruciton = Button(self.main, 280, 555, "backInstructions", "images/instructions.png", 1)


    def back(self):
        Menu(self.main)

    def backInstructions(self):
        self.instructions()

    def stats(self):
        data = Database.read(self)
        self.main.activeObj = set()
        back = Button(self.main, 240, 500, "back", "images/back.png", 1)
        Text(self.main, 200, 110, 30, 'Game statistics:')
        Text(self.main, 100, 170, 22, 'Total games played: ' + str(data[0]))
        Text(self.main, 100, 210, 22, 'Total games won: ' + str(data[1]))
        Text(self.main, 100, 250, 22, 'Win ratio: ' + str(data[2]))
        Text(self.main, 100, 290, 22, 'Avg. turns per game: ' + str(data[3]))
        Text(self.main, 100, 330, 22, 'Avg. spaces moved per game: ' + str(data[4]))
        Text(self.main, 100, 370, 22, 'Avg. times PC bumped the player: ' + str(data[5]))
        Text(self.main, 100, 410, 22, 'Avg. times player bumped the PC: ' + str(data[6]))
        Text(self.main, 100, 450, 22, 'Avg. cards drawn per game: ' + str(data[7]))

    def resume(self):
        self.resume_check = True
        self.main.activeObj = set()
        print("LOADING THE GAME")
        load_game = Load(self.main)
        load_game.load()
        print(self.resume_check)
        #need to get values for these to actually work
        self.main.color = load_game.getColor()
        self.main.numPlayers = load_game.getNumPlayers()
        self.main.activeObj = set()
        self.main.board = Board(self.main)
        self.main.game = Game(self.main)
        self.main.deck = Deck(self.main)
        self.main.deck.start_deck()
        load_game.set_values()
        self.main.game.playing.playerInfoList = self.main.game.playing.getPlayerInfoList(self.main.game.playerNum)
        self.main.game.playing.relaxedButton.visible = False
        # print("6")
        # self.main.save = Save(self.main)
        # print("7")
        # self.main.save.save()
        print("DONE LOADING")
        self.main.gameStarted = True


    def setUpBoard(self):
        finished = True
        if self.main.numPlayers == "one" and self.main.pc1difficulty == '':
            finished = False
        if self.main.numPlayers == "two" and (self.main.pc1difficulty == '' or self.main.pc2difficulty == ''):
            finished = False
        if self.main.numPlayers == "three" and (self.main.pc1difficulty == '' or self.main.pc2difficulty == '' or self.main.pc3difficulty == ''):
            finished = False
        if finished:

            self.main.activeObj = set()
            self.main.board = Board(self.main)
            self.main.game = Game(self.main)
            self.main.deck = Deck(self.main)
            self.main.deck.start_deck()
            self.main.save = Save(self.main)
            #commented out because this was casuing an error
            self.main.save.save()
            self.main.gameStarted = True

#class for displaying static text on screen
class Text:
    def __init__(self, main, x, y, size, text):
        self.main = main
        self.x, self.y = x, y
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.layer = 0
        self.main.activeObj.add(self)

    def draw(self):
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.main.screen.blit(self.textSurface, (self.x, self.y))

    def tick(self):
        pass

    def onClick(self):
        pass

#class used to dynamically show inputted text on screen
class NameText:
    def __init__(self, main, x, y, size):
        self.main = main
        self.x, self.y = x, y
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.textSurface = self.font.render(self.main.playerName, True, (0, 0, 0))
        self.layer = 1
        self.main.activeObj.add(self)

    def draw(self):
        if len(self.main.playerName) < self.main.maxNameLength:
            self.textSurface = self.font.render(self.main.playerName + self.main.next_blink, True, (0, 0, 0))
        else:
            self.textSurface = self.font.render(self.main.playerName, True, (0, 0, 0))
        self.rect = self.main.screen.blit(self.textSurface, (self.x, self.y))

    def tick(self):
        pass

    def onClick(self):
        pass
