"""
    CS205: Sorry! Final Project
    File name: load.py
    Main author: Peter Macksey
"""

#code to load file in and resume game by making all needed variables equal to what they are in file
import pickle


class Load:


    def __init__(self, main):
        self.main = main


    def load(self):

        pickle_in = open("save.txt", "rb")
        info = pickle.load(pickle_in)

        #game info
        self.player_name = info["player_name"]
        self.current_player = info["current_player"]
        self.num_players = info["num_players"]
        self.turns_taken = info["turns_taken"]
        self.spaces_moved = info["spaces_moved"]
        self.players_bumped = info["players_bumped"]
        self.bumped_by_others = info["bumped_by_others"]
        self.cards_drawn = info["cards_drawn"]

        print("Player name: ", self.player_name)
        print("Current player: ", self.current_player)
        print("Number of computer players: ", self.num_players)
        print("Turns taken: ", self.turns_taken)
        print("Spaces moved: ", self.spaces_moved)
        print("Players bumped: ", self.players_bumped)
        print("Bumped by others: ", self.bumped_by_others)
        print("Cards drawn: ", self.cards_drawn)


        #player 1 data
        self.player1_index = info["player1_index"]
        self.player1_color = info["player1_color"]
        self.player1_location = info["player1_location"]
        self.player1_pawn1_info = info["player1_pawn1_info"]
        self.player1_pawn2_info = info["player1_pawn2_info"]
        self.player1_pawn3_info = info["player1_pawn3_info"]
        self.player1_pawn4_info = info["player1_pawn4_info"]

        #player 1
        print("Player 1 index: ", self.player1_index)
        print("Player 1 color: ", self.player1_color)
        print("Player 1 location: ", self.player1_location)
        print("Player 1 pawn 1 info: ", self.player1_pawn1_info)
        print("Player 1 pawn 2 info: ", self.player1_pawn2_info)
        print("Player 1 pawn 3 info: ", self.player1_pawn3_info)
        print("Player 1 pawn 4 info: ", self.player1_pawn4_info)
        print("")

        # #player 2 data
        self.player2_AI = info["player2_AI"]
        self.player2_index = info["player2_index"]
        self.player2_color = info["player2_color"]
        self.player2_location = info["player2_location"]
        self.player2_pawn1_info = info["player2_pawn1_info"]
        self.player2_pawn2_info = info["player2_pawn2_info"]
        self.player2_pawn3_info = info["player2_pawn3_info"]
        self.player2_pawn4_info = info["player2_pawn4_info"]


        #player 2 print data
        print("Player 2 AI: ", self.player2_AI)
        print("Player 2 index: ", self.player2_index)
        print("Player 2 color: ", self.player2_color)
        print("Player 2 location: ", self.player2_location)
        print("Player 2 pawn 1 info: ", self.player2_pawn1_info)
        print("Player 2 pawn 2 info: ", self.player2_pawn2_info)
        print("Player 2 pawn 3 info: ", self.player2_pawn3_info)
        print("Player 2 pawn 4 info: ", self.player2_pawn4_info)
        print("")

        if self.num_players > 1:
            # #player 3 data
            self.player3_AI = info["player3_AI"]
            self.player3_index = info["player3_index"]
            self.player3_color = info["player3_color"]
            self.player3_location = info["player3_location"]
            self.player3_pawn1_info = info["player3_pawn1_info"]
            self.player3_pawn2_info = info["player3_pawn2_info"]
            self.player3_pawn3_info = info["player3_pawn3_info"]
            self.player3_pawn4_info = info["player3_pawn4_info"]

            #player 3 print data
            print("Player 3 AI: ", self.player3_AI)
            print("Player 3 index: ", self.player3_index)
            print("Player 3 color: ", self.player3_color)
            print("Player 3 location: ", self.player3_location)
            print("Player 3 pawn 1 info: ", self.player3_pawn1_info)
            print("Player 3 pawn 2 info: ", self.player3_pawn2_info)
            print("Player 3 pawn 3 info: ", self.player3_pawn3_info)
            print("Player 3 pawn 4 info: ", self.player3_pawn4_info)
            print("")
        #
        if self.num_players > 2:
            # #player 4 data
            self.player4_AI = info["player4_AI"]
            self.player4_index = info["player4_index"]
            self.player4_color = info["player4_color"]
            self.player4_location = info["player4_location"]
            self.player4_pawn1_info = info["player4_pawn1_info"]
            self.player4_pawn2_info = info["player4_pawn2_info"]
            self.player4_pawn3_info = info["player4_pawn3_info"]
            self.player4_pawn4_info = info["player4_pawn4_info"]

            #player 4 print data
            print("Player 4 AI: ", self.player4_AI)
            print("Player 4 index: ", self.player4_index)
            print("Player 4 color: ", self.player4_color)
            print("Player 4 location: ", self.player4_location)
            print("Player 4 pawn 1 info: ", self.player4_pawn1_info)
            print("Player 4 pawn 2 info: ", self.player4_pawn2_info)
            print("Player 4 pawn 3 info: ", self.player4_pawn3_info)
            print("Player 4 pawn 4 info: ", self.player4_pawn4_info)
            print("")



        #deck data
        self.deck_order = info["deck_order"]
        self.card_index = info["card_index"]
        self.current_card = info["current_card"]

        #deck
        print("Deck order: ", self.deck_order)
        print("Current card: ", self.current_card)
        print("Card Index: ", self.card_index)


    def getColor(self):
        return self.player1_color

    def getNumPlayers(self):
        self.num = self.num_players
        if self.num == 1:
            return "one"
        if self.num == 2:
            return "two"
        if self.num == 3:
            return "three"

    def set_values(self):
        #SETTING VALUES
        self.playerList = self.main.game.playerList

        #game info
        self.main.playerName = self.player_name
        self.main.color = self.player1_color
        self.main.game.turn = self.current_player
        self.main.numPlayers = self.num_players
        self.main.turnsTaken = self.turns_taken
        self.main.spacesMoved = self.spaces_moved
        self.main.playersBumped = self.players_bumped
        self.main.bumpedByOthers = self.bumped_by_others
        self.main.cardsDrawn = self.cards_drawn

        #deck information
        self.main.deck.deck = self.deck_order
        #self.main.deck.deck
        self.main.deck.current_card = self.current_card
        #self.main.deck.current_card
        self.main.deck.i = self.card_index
        #self.main.deck.i


        #player 1 info
        self.playerList[0].playerIndex = self.player1_index
        self.playerList[0].color = self.player1_color
        self.playerList[0].playerPosition = self.player1_location
        # #player1 pawn info.
        self.playerList[0].pawnList[0].position = self.player1_pawn1_info
        self.playerList[0].pawnList[1].position = self.player1_pawn2_info
        self.playerList[0].pawnList[2].position = self.player1_pawn3_info
        self.playerList[0].pawnList[3].position = self.player1_pawn4_info



        #player 2 information
        self.main.pc1difficulty = self.player2_AI
        self.playerList[1].playerIndex = self.player2_index
        self.playerList[1].color = self.player2_color
        self.playerList[1].playerPosition = self.player2_location
        # #player1 pawn info.
        self.playerList[1].pawnList[0].position = self.player2_pawn1_info
        self.playerList[1].pawnList[1].position = self.player2_pawn2_info
        self.playerList[1].pawnList[2].position = self.player2_pawn3_info
        self.playerList[1].pawnList[3].position = self.player2_pawn4_info

        if self.num_players > 1:
            #player 3 information
            self.main.pc2difficulty = self.player3_AI
            self.playerList[2].playerIndex = self.player3_index
            self.playerList[2].color = self.player3_color
            self.playerList[2].playerPosition = self.player3_location
            # #player1 pawn info.
            self.playerList[2].pawnList[0].position = self.player3_pawn1_info
            self.playerList[2].pawnList[1].position = self.player3_pawn2_info
            self.playerList[2].pawnList[2].position = self.player3_pawn3_info
            self.playerList[2].pawnList[3].position = self.player3_pawn4_info


        if self.num_players > 2:
            #player 4 information
            self.main.pc3difficulty = self.player4_AI
            self.playerList[3].playerIndex = self.player4_index
            self.playerList[3].color = self.player4_color
            self.playerList[3].playerPosition = self.player4_location
            # #player1 pawn info.
            self.playerList[3].pawnList[0].position = self.player4_pawn1_info
            self.playerList[3].pawnList[1].position = self.player4_pawn2_info
            self.playerList[3].pawnList[2].position = self.player4_pawn3_info
            self.playerList[3].pawnList[3].position = self.player4_pawn4_info


        print("Current player: ", self.current_player)
        print("Number of computer players: ", self.num_players)
        #player 1
        print("Player 1 index: ", self.player1_index)
        print("Player 1 color: ", self.player1_color)
        print("Player 1 location: ", self.player1_location)
        print("Player 1 pawn 1 info: ", self.player1_pawn1_info)
        print("Player 1 pawn 2 info: ", self.player1_pawn2_info)
        print("Player 1 pawn 3 info: ", self.player1_pawn3_info)
        print("Player 1 pawn 4 info: ", self.player1_pawn4_info)
        print("")
        #player 2 print data
        print("Player 2 AI: ", self.player2_AI)
        print("Player 2 index: ", self.player2_index)
        print("Player 2 color: ", self.player2_color)
        print("Player 2 location: ", self.player2_location)
        print("Player 2 pawn 1 info: ", self.player2_pawn1_info)
        print("Player 2 pawn 2 info: ", self.player2_pawn2_info)
        print("Player 2 pawn 3 info: ", self.player2_pawn3_info)
        print("Player 2 pawn 4 info: ", self.player2_pawn4_info)
        print("")

        if self.num_players > 1:

            #player 3 print data
            print("Player 3 AI: ", self.player3_AI)
            print("Player 3 index: ", self.player3_index)
            print("Player 3 color: ", self.player3_color)
            print("Player 3 location: ", self.player3_location)
            print("Player 3 pawn 1 info: ", self.player3_pawn1_info)
            print("Player 3 pawn 2 info: ", self.player3_pawn2_info)
            print("Player 3 pawn 3 info: ", self.player3_pawn3_info)
            print("Player 3 pawn 4 info: ", self.player3_pawn4_info)
            print("")
        if self.num_players > 2:


            #player 4 print data
            print("Player 4 AI: ", self.player4_AI)
            print("Player 4 index: ", self.player4_index)
            print("Player 4 color: ", self.player4_color)
            print("Player 4 location: ", self.player4_location)
            print("Player 4 pawn 1 info: ", self.player4_pawn1_info)
            print("Player 4 pawn 2 info: ", self.player4_pawn2_info)
            print("Player 4 pawn 3 info: ", self.player4_pawn3_info)
            print("Player 4 pawn 4 info: ", self.player4_pawn4_info)
            print("")
        #deck
        print("Deck order: ", self.deck_order)
        print("Current card: ", self.current_card)
        print("Card Index: ", self.card_index)
