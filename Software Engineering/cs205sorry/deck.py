"""
    CS205: Sorry! Final Project
    File name: deck.py
    Main author: Peter Macksey
"""

#drawNext()
#discard()
#shuffle()
import pygame
import random


class Deck:
    #class variables
    def __init__(self, main):
        #class constructor
        #The modern deck contains 45 cards: there are five
        #1 cards as well as four each of the other cards
        #(Sorry!, 2, 3, 4, 5, 7, 8, 10, 11 and 12)
        #13 = sorry card

        self.main = main

    def start_deck(self):
        self.i = 0
        self.current_card = ""
        self.card_index = 0
        self.last_card = ""

        #initialise empty array
        self.deck = []

        #counter  is the count to see how many cards there are total
        counter = 0
        #int is the card number (1-13)
        int = 1

        for x in range(1,46):
            #skips 6 and 9
            if int == 6 or int == 9:
                int+=1
            #makes sure to add 5 1s
            if counter < 5:
                int == 1
            #13 used as Sorry card space, may be changed here and transformed in another place
            if int <13:
                self.deck.append(int)
            else:
                self.deck.append("Sorry!")
            #changes int every 4 spaces
            if counter>1 and counter%4 == 0:
                int+=1

            counter+=1

        self.layer = 3
        self.main.activeObj.add(self)
        self.deckImg = pygame.image.load('images/deck.png').convert_alpha()
        self.deckImg = pygame.transform.rotozoom(self.deckImg, 0, self.main.scale)
        self.deckX = 220
        self.deckY = 200
        self.cardDownImg = pygame.image.load('images/topofcard_small.png').convert_alpha()
        self.cardDownImg = pygame.transform.rotozoom(self.cardDownImg, 270, 0.133)
        self.cardDownX = 260
        self.cardDownY = 204
        self.cardUpImg = pygame.image.load('images/cardSorry!_small.png').convert_alpha()
        self.cardUpImg = pygame.transform.rotozoom(self.cardUpImg, 90, 0.133)
        self.cardUpX = 260
        self.cardUpY = 365

        self.cardDisplay = pygame.image.load('images/cardSorry!_small.png').convert_alpha()
        self.cardDisplay = pygame.transform.rotozoom(self.cardDisplay, 0, 2)
        self.cardDisplayX = 745
        self.cardDisplayY = 100

        self.shuffle()
        # print(self.deck)
        # print(self.current_card)
        # print("Index: ", self.i)
        # self.drawNext()
        #
        # #DEBUGGING TESTS
        # print(self.current_card)
        # print(self.deck)



    def draw(self):
        self.rect = self.main.screen.blit(self.deckImg, (self.deckX, self.deckY))
        if(self.last_card != ""):
            self.cardDownImg = pygame.image.load('images/topofcard_small.png').convert_alpha()
            self.cardDownImg = pygame.transform.rotozoom(self.cardDownImg, 270, 0.133)
        self.main.screen.blit(self.cardDownImg, (self.cardDownX, self.cardDownY))
        if(self.current_card != ""):
            self.cardUpImg = pygame.image.load('images/card' + str(self.current_card) + '_small.png').convert_alpha()
            self.cardUpImg = pygame.transform.rotozoom(self.cardUpImg, 90, 0.133)
        self.main.screen.blit(self.cardUpImg, (self.cardUpX, self.cardUpY))
        """
        if(self.current_card != ""):
            self.cardDisplay = pygame.image.load('images/card' + str(self.current_card) + '_small.png').convert_alpha()
            self.cardDisplay = pygame.transform.rotozoom(self.cardDisplay, 0, 0.5)
        self.main.screen.blit(self.cardUpImg, (self.cardDisplayX, self.cardDisplayY))
        """

    def tick(self):
        pass

    def onClick(self):
        pass

    def shuffle(self):
        #function to shuffle deck
        random.shuffle(self.deck)

    def drawNext(self):
        #return the next card
        self.card_index = self.i
        self.last_card = self.current_card
        self.current_card = self.deck[self.i];
        # print("Card index: ", self.card_index)
        # print("Maybe card index: ", self.i)
        # print("Current card: ", self.current_card)
        self.i+=1
        if(self.i > 44):
            self.shuffle()
            self.i = 0
        from save import Save
        self.main.save = Save(self.main)
        self.main.save.save()
        return self.current_card
