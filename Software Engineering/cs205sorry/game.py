"""
    CS205: Sorry! Final Project
    File name: game.py
    Main author: Chia-Chun Chao
    Author of chooseMove: Gavin Gunkle
    Author of write: Peter Macksey
"""

#from deck import Deck
import pygame
from player import Player
from playing import Playing
import random
import mysql.connector as MySQLdb
import datetime


class Game:
    def __init__(self, main):
        """
        Class constructor
        """
        self.main = main
        self.turn = 'bottom'

        #Create players at different position in the corresponding color
        #Store players in a list
        fourPosition = ['bottom', 'left', 'top', 'right']
        fourColor = ['red', 'blue', 'yellow', 'green']
        playerColorIndex = fourColor.index(self.main.color)

        playerNumDict = {'one': 2, 'two':3, 'three':4}
        self.playerNum = playerNumDict[self.main.numPlayers]
        playerSetting = [self.main.pc0difficulty, self.main.pc1difficulty, self.main.pc2difficulty, self.main.pc3difficulty]
        self.playerList = []
        for i in range(self.playerNum):
            #print("\nCreate a", fourColor[(playerColorIndex+i)%4], "player at", fourPosition[i], "side\n")
            self.playerList.append(Player(self.main, i, fourPosition[i], fourColor[(playerColorIndex+i)%4], playerSetting[i]))

        self.playing = Playing(self.main, self.turn, self.playerList[0], self.playerNum)


        #Add playing information to board object
        self.layer = 4
        self.main.activeObj.add(self)

        self.nextTurnBool = False

        pass

    def draw(self):
        self.rect = pygame.Rect(0,0,0,0)
        pass

    def onClick(self):
        pass

    def tick(self):
        if self.nextTurnBool == True:
            fourPosition = ['bottom', 'left', 'top', 'right']
            currentIndex = fourPosition.index(self.lastTurn)
            for pawn in self.playerList[currentIndex].pawnList:
                if pawn.finishMovingBool == False:
                    #Add this print function to slow down the program to avoid problems
                    #Really weird!! It might be the issue of race condition
                    #print("#######Pawn's still moving")
                    return
            nextIndex = fourPosition.index(self.turn)
            self.playing.nextTurn(self.turn, self.playerList[nextIndex])
            self.nextTurnBool = False

            if self.turn != 'bottom':
                self.computerMove()
        pass

    def drawCard(self):
        """
        Draw a card from the deck
        """
        #return int(input("How many steps to move:"))
        steps = self.main.deck.drawNext()
        if(steps == 'Sorry!'):
            steps = 0
        else:
            steps = int(steps)
            #print('moving ' + str(steps) + ' steps')
        return steps

    def nextTurn(self, allowed):
        """
        Change to next turn
        """
        self.checkEndGame()

        if allowed == True:
            if self.turn != 'bottom':
                self.main.processRendering()
                self.delayGame(10)

            self.lastTurn = self.turn

            fourPosition = ['bottom', 'left', 'top', 'right']
            positionList = fourPosition[:self.playerNum]
            currentIndex = positionList.index(self.turn)
            nextIndex = (currentIndex+1)%self.playerNum
            self.turn = positionList[nextIndex]

            self.nextTurnBool = True
            #self.playing.nextTurn(self.turn, self.playerList[nextIndex])

        pass

    def computerMove(self):
        """
        Computer plays automatically
        """
        self.playing.drawButton.onClick()

        move = self.chooseMove()

        self.main.processRendering()
        self.delayGame(5)


        if move == None:
            self.playing.skipButton.onClick()
            return

        if move['option'] == 1:
            self.playing.optionButton1.onClick()
        else:
            self.playing.optionButton2.onClick()

        firstPawn = move['firstPawn']
        secondPawn = move['secondPawn']

        #All cards but 7
        if self.playing.drawnCard != 7:
            if firstPawn != None:
                firstPawn.onClick()
            if secondPawn != None:
                secondPawn.onClick()
        #Card 7
        else:
            if move['option'] == 1:
                firstPawn.onClick()
            else:
                #The first pawn
                numberButtons = [None, self.playing.numButton1, self.playing.numButton2, self.playing.numButton3, self.playing.numButton4, self.playing.numButton5, self.playing.numButton6]
                firstPawn.onClick()
                numberButtons[move['move']].onClick()
                secondPawn.onClick()

        pygame.display.update()

        pass

    def delayGame(self, loop):
        for i in range(loop):
            pygame.display.update()
        pass

    def chooseRandomMove(self):
        """
        Randomly return a possible move
        """
        if len(self.playing.possibleList) == 0:
            return 0, None
        index = random.randrange(len(self.playing.possibleList))
        possibleMove = self.playing.possibleList[index]

        return possibleMove


    def bestMoveMeanSmart(self):
        score = -50
        if len(self.playing.possibleList) is 0:
            return None
        for i in range(0, len(self.playing.possibleList)):
            currentScore = self.playing.possibleList[i]['forward']
            print(self.playing.possibleList[i])
            if self.playing.possibleList[i]['destination']['type'] == 'track' and self.playing.possibleList[i]['firstPawn'].position['type'] == 'start':
                currentScore += 10

            elif self.playing.possibleList[i]['destination']['type'] == 'safetyZone' and self.playing.possibleList[i]['firstPawn'].position['type'] == 'track':
                currentScore += 10

            elif self.playing.possibleList[i]['destination']['type'] == 'home':
                currentScore += 30

            currentScore -= self.playing.possibleList[i]['bumpSelf'] * 50
            currentScore += self.playing.possibleList[i]['bumpOther'] * 30

            if currentScore > score:
                score = currentScore
                index = i

        return self.playing.possibleList[index]

    def bestMoveMeanDumb(self):
        score = -50
        if len(self.playing.possibleList) is 0:
            return None
        for i in range(0, len(self.playing.possibleList)):

            currentScore = self.playing.possibleList[i]['bumpOther'] * 30

            if currentScore > score:
                score = currentScore
                index = i

        return self.playing.possibleList[index]

    def bestMoveNiceSmart(self):
        score = -50
        if len(self.playing.possibleList) is 0:
            return None
        for i in range(0, len(self.playing.possibleList)):
            currentScore = self.playing.possibleList[i]['forward']

            if self.playing.possibleList[i]['destination']['type'] == 'track' and self.playing.possibleList[i]['firstPawn'].position['type'] == 'start':
                currentScore += 10

            elif self.playing.possibleList[i]['destination']['type'] == 'safetyZone' and self.playing.possibleList[i]['firstPawn'].position['type'] == 'track':
                currentScore += 10

            elif self.playing.possibleList[i]['destination']['type'] == 'home':
                currentScore += 30

            currentScore -= self.playing.possibleList[i]['bumpSelf'] * 50
            currentScore -= self.playing.possibleList[i]['bumpOther'] * 30

            if currentScore > score:
                score = currentScore
                index = i

        return self.playing.possibleList[index]

    def bestMoveNiceDumb(self):
        score = -50
        if len(self.playing.possibleList) is 0:
            return None
        for i in range(0, len(self.playing.possibleList)):

            currentScore = self.playing.possibleList[i]['bumpOther'] * 30

            if currentScore > score:
                score = currentScore
                index = i

        return self.playing.possibleList[index]

    def chooseMove(self):
        #determines which computers turn and their difficulty
        if self.turn == 'left':
            difficulty = self.main.pc1difficulty
        elif self.turn == 'top':
            difficulty = self.main.pc2difficulty
        elif self.turn == 'right':
            difficulty = self.main.pc3difficulty

        #returns function with proper difficulty
        if difficulty == 'meansmart':
            return self.bestMoveMeanSmart()
        elif difficulty == 'meandumb':
            return self.bestMoveMeanDumb()
        elif difficulty == 'nicesmart':
            return self.bestMoveNiceSmart()
        elif difficulty == 'nicedumb':
            return self.bestMoveNiceDumb()



    def checkEndGame(self):
        """
        Check if there's anyone winning the game
        """
        end = False
        homeCount = 0
        for i in range(self.playerNum):
            for j in range(4):
                if self.playerList[i].pawnList[j].position['type'] == 'home':
                    homeCount += 1
            if homeCount == 4 and not end:
                self.endGame(i)
                end = True
            else:
                homeCount = 0
        pass

    def write(self):
        print("Write")
        #get variables and store them as variables to insert
        db = MySQLdb.connect(host = "webdb.uvm.edu", user = "pmacksey_admin", password = "wSuDSSnRb0Bk", database = "PMACKSEY_cs205sorry")
        #db.query("""SELECT """)
        cursor = db.cursor()
        if self.main.pc1difficulty == "":
            AIleft = ""
        else:
            AIleft = self.main.pc1difficulty
        if self.main.pc2difficulty == "":
            AIup = ""
        else:
            AIup = self.main.pc2difficulty
        if self.main.pc3difficulty == "":
            AIright = ""
        else:
            AIright = self.main.pc3difficulty


        player_name = self.main.playerName
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        turns_taken = self.main.turnsTaken
        spaces_moved = self.main.spacesMoved
        players_bumped = self.main.playersBumped
        bumped_by_others = self.main.bumpedByOthers
        cards_drawn = self.main.cardsDrawn
        result = self.won


        #can use array instead of listing stuff out
        cursor.execute("""INSERT INTO stats (fldPlayername, fldDate, fldAIleft, fldAIup, fldAIright, fldTurns_taken, fldspaces_moved, fldplayers_bumped, fldbumped_by_others, fldcards_drawn, fldResult)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (player_name, date_time, AIleft, AIup, AIright, turns_taken, spaces_moved, players_bumped, bumped_by_others, cards_drawn, result))

        db.commit()
        db.close()
        print("Writing done")

    def endGame(self, playerIndex):
        """
        Finish this game
        """
        winner = self.playerList[playerIndex]
        print("Winner: ", winner.playerIndex)
        if winner.playerIndex == 0:
            self.won = "won"
        else:
            self.won = "lost"
        print("Win or lose?: ", self.won)
        #print("Winner")
        #print(winner.color)
        self.main.win(winner.color)
        self.write()

        pass




    # def save(self):
    #     #save button to call save file
    #     savebutton = menu.Button(self.main, 330, 860, "save", "images/stats.png", 1)
    #     Save.save(self)
