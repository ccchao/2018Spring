"""
    File name: playing.py
    Main author: Chia-Chun Chao
    Co-author of moveOptionInfo: Joe Embrey
"""

import pygame

class Playing:

    def __init__(self, main, turn, player, playerNum):
        """
        Class constructor
        """
        ####################Player####################

        #Get player's information
        self.main = main
        self.playerIndex = player.playerIndex
        self.playerPosition = player.playerPosition
        self.color = player.color

        #Create a pawn image
        imagePath = 'images/pawn_' + self.color + '.png'
        self.pawn = pygame.image.load(imagePath).convert_alpha()
        self.pawn = pygame.transform.rotozoom(self.pawn, 0, 0.3)

        #Create a list of player's information
        self.playerInfoList = self.getPlayerInfoList(playerNum)

        ####################Card####################

        #Create a card area
        self.faceUpCardList = []
        self.faceDownCard = pygame.image.load('images/topofcard_small.png').convert_alpha()
        self.faceDownCard = pygame.transform.rotozoom(self.faceDownCard, 0, 0.09)
        cardList = ['Sorry!', 1, 2, 3, 4, 5, '', 7, 8, '', 10, 11, 12]

        self.faceUpCardList.append(pygame.image.load('images/cardSorry!_small.png').convert_alpha())
        self.faceUpCardList[0] = pygame.transform.rotozoom(self.faceUpCardList[0], 0, 0.09)
        for i in range(1,13):
            if i in [6, 9]:
                self.faceUpCardList.append('')
            else:
                self.faceUpCardList.append(pygame.image.load('images/card' + str(cardList[i]) + '_small.png').convert_alpha())
                self.faceUpCardList[i] = pygame.transform.rotozoom(self.faceUpCardList[i], 0, 0.09)

        self.card = self.faceDownCard

        ####################Objects####################

        #Add playing information to board object
        self.layer = 4
        self.main.activeObj.add(self)

        ####################Status####################

        #Show if this player has drawn a card
        self.drawCardBool = False
        #Show if this player == ready to pick a pawn
        self.readyToPickPawnBool = False
        #This player == ready to pick his/her pawns or an opponent's pawns
        self.pick = ''
        #Show if this player has picked a pawn
        self.pickedPawnBool = False
        #Show if player can enter relaxed start mode
        self.relaxedStartbool = True

        ####################Card####################

        #Show card information
        self.cardInfoList = []
        self.cardInfoList.append(Text(self.main, 750, 150, 14, 'Draw a card', False))

        ####################Messages####################

        #Show option information
        self.optionInfoList = []
        #Show information
        self.infoList = []

        ####################Buttons####################

        #Add needed buttons
        self.drawButton = PlayingButton(self.main, 750, 175, "draw", "images/draw.png", 0.8, True)
        self.optionButton1 = PlayingButton(self.main, 660, 250, "option1", "images/select.png", 0.8, False)
        self.optionButton2 = PlayingButton(self.main, 660, 300, "option2", "images/select.png", 0.8, False)
        #Add relaxed start button
        self.relaxedButton = PlayingButton(self.main, 670, 550, "relaxed", "images/relaxedstart.png", 0.8, True)
        #Add skip button
        self.skipButton = PlayingButton(self.main, 670, 500, "skip", "images/skip.png", 0.8, False)
        #Add quit button
        self.quitButton = PlayingButton(self.main, 805, 550, "quit", "images/quit.png", 0.8, True)
        #add save button
        self.saveButton = PlayingButton(self.main, 805, 500, "save", "images/save.png", 0.8, True)

        self.numButton1 = PlayingButton(self.main, 680, 400, "num1", "images/1.png", 0.8, False)
        self.numButton2 = PlayingButton(self.main, 720, 400, "num2", "images/2.png", 0.8, False)
        self.numButton3 = PlayingButton(self.main, 760, 400, "num3", "images/3.png", 0.8, False)
        self.numButton4 = PlayingButton(self.main, 800, 400, "num4", "images/4.png", 0.8, False)
        self.numButton5 = PlayingButton(self.main, 840, 400, "num5", "images/5.png", 0.8, False)
        self.numButton6 = PlayingButton(self.main, 880, 400, "num6", "images/6.png", 0.8, False)


        #Store all possible moves in a list
        self.possibleList = []

        pass

    def initialize(self):
        """
        Initialize all needed variables
        """
        self.card = self.faceDownCard

        #Show if this player == ready to pick a pawn
        self.readyToPickPawnBool = False
        #This player == ready to pick his/her pawns or an opponent's pawns
        self.pick = ''
        #Show if this player has picked a pawn
        self.pickedPawnBool = False

        #Show card information
        self.cardInfoList.clear()
        if self.drawCardBool == False:
            self.cardInfoList.append(Text(self.main, 750, 150, 14, 'Draw a card', False))
        else:
            self.cardInfoList.append(Text(self.main, 750, 150, 14, 'Draw the second card', False))
            #self.drawCardBool = False

        #Show option information
        self.optionInfoList.clear()

        #Show information
        self.infoList.clear()

        self.drawButton.visible = True
        self.optionButton1.visible = False
        self.optionButton2.visible = False

        self.drawnCard = None

        self.main.game.playing.numButton1.visible = False
        self.main.game.playing.numButton2.visible = False
        self.main.game.playing.numButton3.visible = False
        self.main.game.playing.numButton4.visible = False
        self.main.game.playing.numButton5.visible = False
        self.main.game.playing.numButton6.visible = False

        pass

    def draw(self):
        """
        Draw the playing information on the screen at the corresponding position
        """
        self.rect = self.main.screen.blit(self.pawn, (670, 60))
        self.rect = self.main.screen.blit(self.card, (660, 150))

        for playerInfo in self.playerInfoList[self.playerIndex]:
            playerInfo.draw()
        for cardInfo in self.cardInfoList:
            cardInfo.draw()
        for optionInfo in self.optionInfoList:
            optionInfo.draw()
        for info in self.infoList:
            info.draw()

        pass

    def onClick(self):
        pass

    def tick(self):
        pass

    def nextTurn(self, turn, player):
        """
        Show new information for the player of next turn
        """
        self.playerIndex = player.playerIndex
        self.playerPosition = player.playerPosition
        self.color = player.color

        if self.color == self.main.color:
            self.main.turnsTaken += 1
        else:
            for pawn in self.main.game.playerList[0].pawnList:
                pawn.pawn = pygame.image.load('images/pawn_' + pawn.color + '_small.png').convert_alpha()
                pawn.pawn = pygame.transform.rotozoom(pawn.pawn, 0, 1)

        #Create a pawn image
        imagePath = 'images/pawn_' + self.color + '.png'
        self.pawn = pygame.image.load(imagePath).convert_alpha()
        self.pawn = pygame.transform.rotozoom(self.pawn, 0, 0.3)

        self.initialize()

        #Check if the player can enter relaxed start mode
        if self.relaxedStartbool == True:
            for i in range(self.main.game.playerNum):
                for j in range(4):
                    if self.main.game.playerList[i].pawnList[j].position['type'] != 'start':
                        self.relaxedStartbool = False
                        self.relaxedButton.visible = False
                        break

        pass

    def getPlayerInfoList(self, playerNum):
        """
        Create a list of player's information
        """
        playerInfoList = []
        #Player
        playerInfoList.append(list())
        playerInfoList[0].append(Text(self.main, 750, 55, 14, 'Player: ' + self.main.playerName, True))
        playerInfoList[0].append(Text(self.main, 750, 77, 14, 'Position: Bottom', True))
        playerInfoList[0].append(Text(self.main, 750, 99, 14, 'Setting: Genius', True))
        #Computer
        setting = ['', self.main.pc1difficulty, self.main.pc2difficulty, self.main.pc3difficulty]
        print(setting)
        difficulty = {'nicesmart': 'Nice&Smart', 'meansmart': 'Mean&Smart', 'nicedumb': 'Nice&Dumb', 'meandumb': 'Mean&Dumb'}
        fourPosition = ['bottom', 'left', 'top', 'right']
        for i in range(1, playerNum):
            playerInfoList.append(list())
            playerInfoList[i].append(Text(self.main, 750, 55, 14, 'Player: Computer', True))

            position = fourPosition[i][0].upper() + fourPosition[i][1:]
            playerInfoList[i].append(Text(self.main, 750, 77, 14, 'Position: '+position, True))

            print(setting[i])
            try:
                playerInfoList[i].append(Text(self.main, 750, 99, 14, 'Setting: '+difficulty[setting[i]] , True))
            except KeyError:
                playerInfoList[i].append(Text(self.main, 750, 99, 14, '' , True))

        return playerInfoList

    def processOption(self, pawn):
        """
        Process option for the pawn
        """
        if self.drawnCard != 2 and self.drawCardBool == True:
            self.drawCardBool = False

        if self.drawnCard == 'Sorry!' or self.drawnCard == 0:
            #Select own pawn in START
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and pawn.position['type'] == 'start':
                self.pickedPawn = pawn
                self.pickedPawnBool = True
                self.readyToPickPawnBool = True
                self.pick = 'opponent'

                self.infoList.clear()
                self.main.game.playing.infoList.append(Text(self.main, 700, 370, 16, 'Select opponent\'s pawn', False))
            #Select opponent's pawn to BUMP to Start
            elif self.pick == 'opponent' and pawn.playerPosition != self.main.game.turn and self.pickedPawnBool == True and pawn.position['type'] == 'track':
                #Move own pawn the opponent's pawn's position
                tmp = {}
                tmp['type'] = pawn.position['type']
                tmp['side'] = pawn.position['side']
                tmp['index'] = pawn.position['index']

                pawn.position['type'] = 'start'
                pawn.position['side'] = pawn.playerPosition
                pawn.position['index'] = pawn.index

                self.pickedPawn.position = tmp

                if self.pickedPawn.playerIndex == 0:
                    self.main.playersBumped += 1
                if pawn.playerIndex == 0:
                    self.main.bumpedByOthers += 1

                #Check if it's on the triangle of a slide area
                step = self.pickedPawn.checkSlideStep(self.pickedPawn.position)
                self.pickedPawn.tryToMove(step, True)
                if step > 0:
                    self.pickedPawn.status = 'sliding'

                self.readyToPickPawnBool = False
                self.pick = ''
                self.pickedPawnBool = False

        elif self.drawnCard == 1:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn:
                if self.option == 1 and pawn.position['type'] == 'start':
                    pawn.tryToMove(1, True)
                    self.infoList.clear()
                elif self.option == 2 and pawn.position['type'] != 'start':
                    pawn.tryToMove(1, True)
                    self.infoList.clear()
        elif self.drawnCard == 2:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn:
                if self.option == 1 and pawn.position['type'] == 'start':
                    pawn.tryToMove(1, True)
                    self.initialize()
                    self.infoList.clear()
                elif self.option == 2 and pawn.position['type'] == 'track' or pawn.position['type'] == 'safetyZone':
                    pawn.tryToMove(2, True)
                    self.initialize()
                    self.infoList.clear()
                #For the player to draw again
                if pawn.playerPosition != self.main.game.turn and self.drawCardBool == True:
                    for i in range(self.main.game.playerNum - 1):
                        self.main.game.nextTurn(True)
        elif self.drawnCard == 3:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and pawn.position['type'] != 'start':
                pawn.tryToMove(3, True)
        elif self.drawnCard == 4:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and pawn.position['type'] != 'start':
                pawn.tryToMove(-4, True)
        elif self.drawnCard == 5:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and pawn.position['type'] != 'start':
                pawn.tryToMove(5, True)

        elif self.drawnCard == 7:
            #Select own pawn to move forward
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and self.option == 1 and pawn.position['type'] != 'start':
                pawn.tryToMove(7, True)
                self.infoList.clear()
            #Select first pawn to move
            elif self.pick == 'own' and pawn.playerPosition == self.main.game.turn and self.option == 2 and self.pickedPawnBool == False and pawn.position['type'] != 'start':
                self.pickedPawn = pawn
                self.pickedPawnBool = True
                self.readyToPickPawnBool = True
                self.pick = 'own'

                self.infoList.clear()
                self.main.game.playing.infoList.append(Text(self.main, 700, 370, 16, 'How many steps to move?', False))
                self.numButton1.visible = True
                self.numButton2.visible = True
                self.numButton3.visible = True
                self.numButton4.visible = True
                self.numButton5.visible = True
                self.numButton6.visible = True
            #Select second pawn to move
            elif self.pick == 'own' and pawn.playerPosition == self.main.game.turn and self.option == 2 and self.pickedPawnBool == True and pawn.position['type'] != 'start':
                pawn.tryToMove(7-self.pickedNum, True)

                #Fail to move
                if pawn.playerPosition == self.main.game.turn:
                    self.readyToPickPawnBool = False
                    self.pick = 'own'
                    self.pickedPawnBool = False
                    self.pickedPawn.position = self.originalPosition
                    self.infoList.clear()
                    self.optionButton2.processOption(7, 2)

        elif self.drawnCard == 8:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and pawn.position['type'] != 'start':
                pawn.tryToMove(8, True)
        elif self.drawnCard == 10:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn:
                if self.option == 1 and pawn.position['type'] != 'start':
                    pawn.tryToMove(10, True)
                    self.infoList.clear()
                elif self.option == 2 and pawn.position['type'] != 'start':
                    pawn.tryToMove(-1, True)
                    self.infoList.clear()

        elif self.drawnCard == 11:
            #Select own pawn to move forward
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and self.option == 1 and pawn.position['type'] != 'start':
                pawn.tryToMove(11, True)
                self.infoList.clear()
            #Select own pawn to switch
            elif self.pick == 'own' and pawn.playerPosition == self.main.game.turn and self.option == 2 and pawn.position['type'] != 'start':
                self.pickedPawn = pawn
                self.pickedPawnBool = True
                self.readyToPickPawnBool = True
                self.pick = 'opponent'

                self.infoList.clear()
                self.main.game.playing.infoList.append(Text(self.main, 700, 370, 16, 'Select opponent\'s pawn', False))
            #Select opponent's pawn to switch
            elif self.pick == 'opponent' and pawn.playerPosition != self.main.game.turn and self.option == 2 and self.pickedPawnBool == True and pawn.position['type'] == 'track':
                tmp = {'type': pawn.position['type'], 'side': pawn.position['side'], 'index': pawn.position['index']}
                pawn.position = self.pickedPawn.position

                self.pickedPawn.position = tmp

                #Check if it's on the triangle of a slide area
                step = self.pickedPawn.checkSlideStep(self.pickedPawn.position)
                self.pickedPawn.tryToMove(step, True)
                if step > 0:
                    self.pickedPawn.status = 'sliding'
                step = pawn.checkSlideStep(pawn.position)
                pawn.tryToMove(step, True)
                if step > 0:
                    pawn.status = 'sliding'


                #Check if it's on the triangle of a slide area
                step = self.pickedPawn.checkSlideStep(self.pickedPawn.position)
                self.pickedPawn.tryToMove(step, True)
                if step > 0:
                    self.pickedPawn.status = 'sliding'


                self.readyToPickPawnBool = False
                self.pick = ''
                self.pickedPawnBool = False

        elif self.drawnCard == 12:
            if self.pick == 'own' and pawn.playerPosition == self.main.game.turn and pawn.position['type'] != 'start':
                pawn.tryToMove(12, True)

        pass

    def checkPossibleMove(self, card):
        """
        Check if there's any possible move this player can take. If yes, store all moves in a list
        """
        self.possibleList.clear()
        player = self.main.game.playerList[self.playerIndex]
        bumpSelf = 0
        bumpOther = 0

        if self.drawnCard == 'Sorry!' or self.drawnCard == 0:
            #Loop for own pawns
            for firstPawn in player.pawnList:
                if firstPawn.position['type'] == 'start':
                    #Loop for opponents
                    for otherPlayer in self.main.game.playerList:
                        if otherPlayer != player:
                            #Loop for opponents' pawns
                            for secondPawn in otherPlayer.pawnList:
                                if secondPawn.position['type'] == 'track':
                                    bumpSelf = 0
                                    bumpOther = 1 #Bump the opponent's pawn
                                    step = firstPawn.fakeCheckSlideStep(secondPawn.position, firstPawn.playerPosition)
                                    destination = secondPawn.position
                                    #The pawn == on the triangle of a slide area
                                    if step != 0:
                                        for i in range(step):
                                            destination = firstPawn.fakeGetNext(destination, step)
                                            status, tmpBumpSelf, tmpBumpOther = firstPawn.fakeCheckCollision(destination, 'sliding')
                                            bumpSelf += tmpBumpSelf
                                            bumpOther += tmpBumpOther
                                    #Add this move to the list
                                    index = len(self.possibleList)
                                    self.appendPossibleMove(1, index, firstPawn, secondPawn, destination, bumpSelf, bumpOther, 0)
        elif self.drawnCard == 1:
            #Option 1 : Start a pawn
            for firstPawn in player.pawnList:
                if firstPawn.position['type'] == 'start':
                    destination, bumpSelf, bumpOther = firstPawn.fakeMove(1)
                    if destination != None:
                        index = len(self.possibleList)
                        self.appendPossibleMove(1, index, firstPawn, None, destination, bumpSelf, bumpOther, 1)
            #Option 2 : Move a pawn
            self.movePawnOption(1, player, 2)

        elif self.drawnCard == 2:
            #Option 1 : Start a pawn
            for firstPawn in player.pawnList:
                if firstPawn.position['type'] == 'start':
                    destination, bumpSelf, bumpOther = firstPawn.fakeMove(1)
                    if destination != None:
                        index = len(self.possibleList)
                        self.appendPossibleMove(1, index, firstPawn, None, destination, bumpSelf, bumpOther, 1)
            #Option 2 : Move a pawn
            self.movePawnOption(2, player, 2)

        elif self.drawnCard == 3:
            self.movePawnOption(3, player, 1)
        elif self.drawnCard == 4:
            self.movePawnOption(-4, player, 1)
        elif self.drawnCard == 5:
            self.movePawnOption(5, player, 1)

        elif self.drawnCard == 7:
            #Option 1 : Move a pawn
            self.movePawnOption(7, player, 1)
            #Option 2 : Move two pawns
            #Loop for first pawn
            for i in range(4):
                firstPawn = player.pawnList[i]
                if firstPawn.position['type'] == 'track' or firstPawn.position['type'] == 'safetyZone':
                    #For different selected steps from 1 to 6
                    for steps in range(1, 7):
                        #Store the first pawn's information
                        destination, bumpSelf, bumpOther = firstPawn.fakeMove(steps)
                        if destination != None:
                            distanceFromHome = self.distanceFromHome(destination, firstPawn.playerPosition)
                            forward = self.distanceFromHome(firstPawn.position, firstPawn.playerPosition) - distanceFromHome

                            #Loop for second pawn
                            for j in range(i+1,4):
                                index = len(self.possibleList)
                                secondPawn = player.pawnList[j]
                                if secondPawn.position['type'] == 'track' or secondPawn.position['type'] == 'safetyZone':
                                    destination2, bumpSelf2, bumpOther2 = secondPawn.fakeMove(7-steps)
                                    if destination2 != None:
                                        distanceFromHome2 = self.distanceFromHome(destination2, secondPawn.playerPosition)
                                        forward2 = self.distanceFromHome(secondPawn.position, secondPawn.playerPosition) - distanceFromHome2
                                        #Append dictionary to list
                                        possibleMove = {'option': 2, 'index': index, 'firstPawn': firstPawn, 'secondPawn': secondPawn, 'forward': forward+forward2, 'distanceFromHome': distanceFromHome+distanceFromHome2, 'destination': destination, 'bumpSelf': bumpSelf+bumpSelf2, 'bumpOther': bumpOther+bumpOther2, 'move': steps}
                                        self.possibleList.append(possibleMove)

        elif self.drawnCard == 8:
            self.movePawnOption(8, player, 1)
        elif self.drawnCard == 10:
            #Option 1 : Move a pawn forward
            self.movePawnOption(10, player, 1)
            #Option 2 : Move a pawn backward
            self.movePawnOption(-1, player, 2)
        elif self.drawnCard == 11:
            #Option 1 : Move a pawn
            self.movePawnOption(11, player, 1)
            #Option 2 : Switch a pawn
            for firstPawn in player.pawnList:
                if firstPawn.position['type'] == 'track':
                    #Loop for opponents
                    for otherPlayer in self.main.game.playerList:
                        if otherPlayer != player:
                            #Loop for opponents' pawns
                            for secondPawn in otherPlayer.pawnList:
                                if secondPawn.position['type'] == 'track':
                                    bumpSelf = 0
                                    bumpOther = 0
                                    secondPosition = {'type': secondPawn.position['type'], 'side': secondPawn.position['side'], 'index': secondPawn.position['index']}
                                    secondPawn.position = {'type': firstPawn.position['type'], 'side': firstPawn.position['side'], 'index': firstPawn.position['index']}
                                    step = firstPawn.fakeCheckSlideStep(secondPosition, firstPawn.playerPosition)
                                    destination = secondPosition
                                    #The pawn == on the triangle of a slide area
                                    if step != 0:
                                        for i in range(step):
                                            destination = firstPawn.fakeGetNext(destination, step)
                                            status, tmpBumpSelf, tmpBumpOther = firstPawn.fakeCheckCollision(destination, 'sliding')
                                            bumpSelf += tmpBumpSelf
                                            bumpOther += tmpBumpOther
                                    #Add this move to the list
                                    index = len(self.possibleList)
                                    self.appendPossibleMove(2, index, firstPawn, secondPawn, destination, bumpSelf, bumpOther, 11)
                                    """This == still wrong, so I commented it out
                                    #Check if second pawn == on the triangle of a slide area
                                    step = secondPawn.fakeCheckSlideStep(secondPawn.position, secondPawn.playerPosition)
                                    if step != 0:
                                        destination = secondPawn.position
                                        for i in range(step):
                                            destination = secondPawn.fakeGetNext(destination, step)
                                            status, tmpBumpSelf, tmpBumpOther = secondPawn.fakeCheckCollision(destination, 'sliding')
                                            bumpSelf += tmpBumpSelf
                                            bumpOther += tmpBumpOther
                                    """
                                    secondPawn.position = secondPosition

        elif self.drawnCard == 12:
            self.movePawnOption(12, player, 1)

        #Print all possible moves
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        #pp.pprint(self.possibleList)


        pass

    def appendPossibleMove(self, option, index, firstPawn, secondPawn, destination, bumpSelf, bumpOther, move):
        """
        Append all information of this possible move to the list
        """
        if firstPawn == None:
            pawn = secondPawn
        else:
            pawn = firstPawn
        #Calculate distance
        distanceFromHome = self.distanceFromHome(destination, pawn.playerPosition)
        forward = self.distanceFromHome(pawn.position, pawn.playerPosition) - distanceFromHome

        #Append dictionary to list
        possibleMove = {'option': option, 'index': index, 'firstPawn': firstPawn, 'secondPawn': secondPawn, 'forward': forward, 'distanceFromHome': distanceFromHome, 'destination': destination, 'bumpSelf': bumpSelf, 'bumpOther': bumpOther, 'move': move}
        self.possibleList.append(possibleMove)

        pass

    def movePawnOption(self, steps, player, option):
        """
        The option == to move a pawn
        """
        bumpSelf = 0
        bumpOther = 0
        for firstPawn in player.pawnList:
                if firstPawn.position['type'] == 'track' or firstPawn.position['type'] == 'safetyZone':
                    destination, bumpSelf, bumpOther = firstPawn.fakeMove(steps)
                    if destination != None:
                        index = len(self.possibleList)
                        self.appendPossibleMove(option, index, firstPawn, None, destination, bumpSelf, bumpOther, steps)

        pass

    def distanceFromHome(self, position, playerPosition):
        """
        Calculate the distance between the original position and the destination position
        """
        if position['type'] == 'home':
            distance = 0
        elif position['type'] == 'safetyZone':
            distance = 5 - position['index']
        elif position['type'] == 'start':
            distance = 65
        elif position['type'] == 'track':
            if position['side'] == playerPosition:
                if position['index'] <= 2:
                    #distance = 3 - position['index'] + 5
                    distance = 8 - position['index']
                else:
                    #distance = 15 - position['index'] + 15*3 + 8
                    distance = 68 - position['index']
            else:
                fourPosition = ['bottom', 'left', 'top', 'right']

                index = (fourPosition.index(position['side']) + 1) % 4
                distance = 15 - position['index']

                while (fourPosition[index] != playerPosition):
                    distance += 15
                    index = (index+1) % 4
                distance += 8

        return distance

class PlayingButton:
    def __init__(self, main, x, y, action, img, scale, visible):
        """
        Class constructor
        """
        self.action = action
        self.main = main
        self.x, self.y = x, y
        self.layer = 4
        self.main.activeObj.add(self)
        self.scale = scale
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, self.scale)
        self.visible = visible

    def draw(self):
        if self.visible == True:
            self.rect = self.main.screen.blit(self.img, (self.x, self.y))
        else:
            self.rect = self.main.screen.blit(self.main.game.playing.pawn, (670, 60))

        pass


    def tick(self):
        pass

    def onClick(self):
        if self.visible == True:
            if self.action == "draw":
                self.drawCard()
            elif self.action == "option1":
                self.main.game.playing.infoList.clear()
                self.main.game.playing.option = 1
                self.processOption(self.main.game.playing.drawnCard, 1)
            elif self.action == "option2":
                self.main.game.playing.infoList.clear()
                self.main.game.playing.option = 2
                self.processOption(self.main.game.playing.drawnCard, 2)
            elif self.action == "skip":
                self.main.game.playing.drawCardBool = False
                self.main.game.nextTurn(True)
                self.main.game.playing.skipButton.visible = False
            elif self.action == "relaxed":
                for i in range(self.main.game.playerNum):
                    self.main.game.playerList[i].pawnList[0].position['type'] = 'track'
                    self.main.game.playerList[i].pawnList[0].position['index'] = 4
                    self.visible = False
            elif self.action == "quit":
                self.main.quit()
            elif self.action == "save":
                self.main.save.save()
            elif self.action == "num1":
                self.processCard7(1)
            elif self.action == "num2":
                self.processCard7(2)
            elif self.action == "num3":
                self.processCard7(3)
            elif self.action == "num4":
                self.processCard7(4)
            elif self.action == "num5":
                self.processCard7(5)
            elif self.action == "num6":
                self.processCard7(6)
        pass

    def drawCard(self):
        """
        Draw a card, change the image, and show card information
        """
        card = self.main.game.drawCard()

        self.main.game.playing.drawnCard = card
        if card == 'Sorry!' or card == 0:
            self.main.game.playing.card = self.main.game.playing.faceUpCardList[0]
        else:
            self.main.game.playing.card = self.main.game.playing.faceUpCardList[card]

        #This player has drawn a card
        self.main.game.playing.drawCardBool = True
        self.visible = False

        #Show card information
        self.main.game.playing.cardInfoList.clear()
        self.getCardInfo(card)

        #Let player to choose an option to move
        self.main.game.playing.optionInfoList.clear()
        self.moveOptionInfo(card)

        #Check if there's any move this player can take
        self.main.game.playing.checkPossibleMove(card)
        if len(self.main.game.playing.possibleList) == 0:
            self.main.game.playing.skipButton.visible = True
        else:
            self.main.game.playing.skipButton.visible = False

        if self.main.game.turn == 'bottom':
            self.main.cardsDrawn += 1
            #print('Cards drawn: ' + str(self.main.cardsDrawn))

        return card

    def moveOptionInfo(self, card):
        """
        Let player to choose an option to move
        """
        if card == 'Sorry!' or card == 0:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/selectpawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
            #self.main.game.playing.optionButton2.visible = True
            #self.main.game.playing.optionInfoList.append(Text(self.main, 790, 312, 14, 'Skip', False))
        elif card == 1:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/startpawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionButton2.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton2.img = pygame.transform.rotozoom(self.main.game.playing.optionButton2.img, 0, self.main.game.playing.optionButton2.scale)
            self.main.game.playing.optionButton2.visible = True
        elif card == 2:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/startpawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionButton2.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton2.img = pygame.transform.rotozoom(self.main.game.playing.optionButton2.img, 0, self.main.game.playing.optionButton2.scale)
            self.main.game.playing.optionButton2.visible = True
        elif card == 3:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
        elif card == 4:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
        elif card == 5:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
        elif card == 7:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionButton2.img = pygame.image.load('images/movetwopawns.png').convert_alpha()
            self.main.game.playing.optionButton2.img = pygame.transform.rotozoom(self.main.game.playing.optionButton2.img, 0, self.main.game.playing.optionButton2.scale)
            self.main.game.playing.optionButton2.visible = True
        elif card == 8:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
        elif card == 10:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawnforwards.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionButton2.img = pygame.image.load('images/movepawnbackwards.png').convert_alpha()
            self.main.game.playing.optionButton2.img = pygame.transform.rotozoom(self.main.game.playing.optionButton2.img, 0, self.main.game.playing.optionButton2.scale)
            self.main.game.playing.optionButton2.visible = True
        elif card == 11:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True
            self.main.game.playing.optionButton2.img = pygame.image.load('images/switchpawn.png').convert_alpha()
            self.main.game.playing.optionButton2.img = pygame.transform.rotozoom(self.main.game.playing.optionButton2.img, 0, self.main.game.playing.optionButton2.scale)
            self.main.game.playing.optionButton2.visible = True
        elif card == 12:
            self.main.game.playing.optionButton1.img = pygame.image.load('images/movepawn.png').convert_alpha()
            self.main.game.playing.optionButton1.img = pygame.transform.rotozoom(self.main.game.playing.optionButton1.img, 0, self.main.game.playing.optionButton1.scale)
            self.main.game.playing.optionButton1.visible = True

        pass

    def processOption(self, card, option):
        """
        Process this option if player has to choose two pawns
        """
        if card == 'Sorry!' or card == 0:
            if option == 1:
                self.main.game.playing.readyToPickPawnBool = True
                self.main.game.playing.pick = 'own'
            #else:
            #self.main.game.nextTurn(True)

        elif card in [1,2,3,4,5,7,8,10,11,12]:
            if card == 7 and self.main.game.playing.pickedPawnBool == True:
                #Return from option 2 to option 1
                self.main.game.playing.pickedPawnBool = False
                self.main.game.playing.pickedPawn.position = self.main.game.playing.originalPosition
            self.main.game.playing.readyToPickPawnBool = True
            self.main.game.playing.pick = 'own'

        if card == 7 and option == 2:
            self.main.game.playing.infoList.append(Text(self.main, 720, 370, 16, 'Select the first pawn', False))
        else:
            self.main.game.playing.infoList.append(Text(self.main, 750, 370, 16, 'Select a pawn', False))
            for move in self.main.game.playing.possibleList:
                if move['firstPawn'].playerIndex == 0:
                    move['firstPawn'].pawn = pygame.image.load('images/pawn_' + move['firstPawn'].color + '_small_highlight.png').convert_alpha()
                    move['firstPawn'].pawn = pygame.transform.rotozoom(move['firstPawn'].pawn, 0, 1)
                #print(move['firstPawn'])

        pass

    def processCard7(self, number):
        """
        Store original position, move the first pawn, and hide number buttons
        """
        self.main.game.playing.pickedNum = number

        #Store the original position
        position = self.main.game.playing.pickedPawn.position
        self.main.game.playing.originalPosition = {'type': position['type'], 'side': position['side'], 'index': position['index']}
        self.main.game.playing.originalPawn = self.main.game.playing.pickedPawn

        self.main.game.playing.pickedPawn.tryToMove(number, False)

        #If the pawn can move successfully, then player can select the next pawn
        if self.main.game.playing.pickedPawn.moveStep != 0:
            self.main.game.playing.infoList.clear()
            self.main.game.playing.infoList.append(Text(self.main, 660, 370, 16, 'Select the second pawn to move '+str(7-number), False))
            self.main.game.playing.numButton1.visible = False
            self.main.game.playing.numButton2.visible = False
            self.main.game.playing.numButton3.visible = False
            self.main.game.playing.numButton4.visible = False
            self.main.game.playing.numButton5.visible = False
            self.main.game.playing.numButton6.visible = False

        pass

    def getCardInfo(self, card):
        """
        Show card information
        """
        if card == 'Sorry!' or card == 0:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Take one pawn from your START,', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'place it on any space that is', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'occupied by any opponent, and', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 210, 13, 'BUMP that opponent’spawn', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 230, 13, 'back to its START.', False))
        elif card == 1:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either start a pawn OR move', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'one pawn forward 1 space.', False))
        elif card == 2:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either start a pawn OR move one', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'pawn forward 2 spaces. Whichever', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'you do or even if you couldn’t', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 210, 13, 'move—DRAW GAIN and move', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 230, 13, 'accordingly.', False))
        elif card == 3:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 3 spaces.', False))
        elif card == 4:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn backward 4 spaces.', False))
        elif card == 5:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 5 spaces.', False))
        elif card == 7:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either move one pawn forward 7', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'spaces—OR split the forward', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'move between any two pawns.', False))
        elif card == 8:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 8 spaces.', False))
        elif card == 10:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Either move one pawn forward 10', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, 'spaces—OR move one pawn', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'backward 1 space.', False))

        elif card == 11:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 11 spaces', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 170, 13, '—OR switch any one of your pawns', False))
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 190, 13, 'with one of any opponent’s.', False))
        elif card == 12:
            self.main.game.playing.cardInfoList.append(Text(self.main, 720, 150, 13, 'Move one pawn forward 12 spaces', False))

        pass

class Text:
    def __init__(self, main, x, y, size, text, underLine):
        self.main = main
        self.x, self.y = x, y
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.font.set_underline(underLine)
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.layer = 4

    def draw(self):
        self.textSurface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.main.screen.blit(self.textSurface, (self.x, self.y))

    def tick(self):
        pass

    def onClick(self):
        pass
