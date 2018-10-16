"""
File name: mastermind.py
Students: Chia-Chun Chao
Deadline: Thursday, Feb. 15th
Course: CS205 Software Engineering

Warm-up Project
Simulation of the board game Mastermind
"""

#Convert character or word to number
colorToNum = {'R': 0, 'RED': 0, '0': 0,
              'B': 1, 'BLUE': 1, '1': 1,
              'P': 2, 'PINK': 2, '2': 2,
              'G': 3, 'GREEN': 3, '3': 3,
              'O': 4, 'ORANGE': 4, '4': 4,
              'Y': 5, 'YELLOW': 5, '5': 5}

#Convert number to word
numToColor = {0: 'RED',
              1: 'BLUE',
              2: 'PINK',
              3: 'GREEN',
              4: 'ORANGE',
              5: 'YELLOW',
              6: 'WHITE', #correct in both color and position
              7: 'BLACK'} #correct color code peg placed in the wrong position

#For convenience of printing
order = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 
         'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

from codecheck import code_check
from computerguess import computer_guess

import sys
import random
import datetime
import json

def check(guess, answer):
    """
    Return the key of the input guess based on the input answer
    """

    return code_check(guess, answer)


def list_to_string(inputList, width):
    """
    Print the input list, and each item is printed in the center of width
    Ex. [ RED    PINK  GREEN  YELLOW]
    """
    string = '['
    blankNum = len(inputList)-1
    
    for item in inputList:
        string += item.center(width)
        if blankNum > 0:
            string += ' '
            blankNum -= 1
    string += ']'
        
    return string
    

def user_mode():
    """
    The computer picks the initial code, and the user must guess
    """
    
    #Save the start time to calculate duration time
    startTime = datetime.datetime.now()
    
    #Generate the answer
    answer = random.sample(range(6), 4)
    
    hint = 0#The number of used hints
    
    print("\n\n******************* User guesses ******************\n")
    
    guessList = [] #Store all guesses
    keyList = [] #Store all keys
    
    
    #Run for 12 turns or until the user finds the answer
    for turn in range(12):
    
        print("Select four pegs in these colors:")
        print("[R] RED / [B] BLUE / [P] PINK / [G] GREEN / [O] ORANGE / [Y] YELLOW")
        print("[H] Hint: ask for a hint")
        print("[C] Clear: clear all pegs of this turn")
        print("[Q] Quit: quit to main menu\n")
        
        print("Either type in characters in separate lines or in one line but split them by spaces\n")
       
        guess = []
  
        #User inputs the color of each peg      
        while len(guess) < 4:
            peg = input("The " + order[len(guess)].upper() + " color of your " + "{} guess ({}/4): ".format(order[turn], len(guess)+1)).upper()
            
            if peg in colorToNum:
                guess.append(colorToNum[peg])
                
            elif peg == 'H' or peg == 'HINT':
                print("\nHint: The {0} color of the answer is {1}\n".format(order[hint%4].upper(), numToColor[answer[hint%4]]))
                hint += 1
                
            elif peg == 'Q' or peg == 'QUIT':
                return
            
            elif peg == 'C' or peg == 'CLEAR':
                guess.clear()
                print("\nRestart this guess\n")
            
            #User can also input multiple colors separated by blank
            elif len(guess) + len(peg.split()) <= 4:
                peg = peg.split()
                tmpPegList = []
                for eachPeg in peg:
                    if eachPeg in colorToNum:
                        tmpPegList.append(colorToNum[eachPeg])
                    else:
                        break
                #Only process when there are four elements in the input
                if len(peg) == len(tmpPegList):
                    guess.extend(tmpPegList)
                
            else:
                print("\nSelect four pegs in these colors:")
                print("[R] RED / [B] BLUE / [P] PINK / [G] GREEN / [O] ORANGE / [Y] YELLOW") 
                print("[H] Hint: ask for a hint")
                print("[C] Clear: clear all pegs of this turn")
                print("[Q] Quit: quit to main menu\n")
                print("Either type in characters in separate lines or in one line but split them by spaces\n")

        
        
        #Check the guess and return the key    
        key = check(guess, answer)
        #Store each guess and key to show previous guesses and results
        guessList.append(guess)
        keyList.append(key)
       
        
        #Print guess and key of each turn
        print("\n\n===================================================")
        print("Your guesses and keys ({}/12):".format(turn+1),'\n')
        for i in range(12): 
            #Show index, guess, and key
            if i <= turn:
                guessInWord = []
                for guessInNum in guessList[i]:
                    guessInWord.append(numToColor[guessInNum])
                    
                keyInWord = []
                for keyInNum in keyList[i]:
                    keyInWord.append(numToColor[keyInNum])
                
                print('{:3d}'.format(i+1), list_to_string(guessInWord, 6), list_to_string(keyInWord, 5))
            #Only show index
            else:
                print('{:3d}'.format(i+1))
                
        print("===================================================\n")

        #If all colors in key are black, the guess is correct
        if key.count(7) == 4:
            print("Congratulations! Your answer is correct!\n")
            
            #Store user name
            player = input("Type in your name: ")
            if player == '':
                player = 'anonym'
            
            #Store game time
            duration = (datetime.datetime.now() - startTime).total_seconds()
            
            print("\nHello, {0}\nYou spent {1:.2f} seconds to win\n\n\n".format(player, duration))
            
            #Store data in json file
            data = {'player': player,
                    'turns': turn+1,
                    'startTime': datetime.datetime.strftime(startTime, "%Y-%m-%d %H:%M:%S"),
                    'duration': duration,
                    'hints': hint}
            with open('stats.txt', 'a') as file:
                file.write(json.dumps(data))
                file.write('\n')
            
                    
            
            return
       
    print("Game over...")
    
    answerInWord = []
    for answerInNum in answer:
        answerInWord.append(numToColor[answerInNum])
    print("The answer is ", list_to_string(answerInWord, 6))
          
    pass
    
def computer_mode():
    """
    The user picks the initial code, and the computer guesses
    """
    
    print("\n\n***************** Computer guesses ****************\n")
    

    print("\nPossible colors of each peg:")
    print("[R] RED / [B] BLUE / [P] PINK / [G] GREEN / [O] ORANGE / [Y] YELLOW")
    print("[C] Clear: clear all pegs of code")
    print("[Q] Quit: quit to main menu\n")
    print("Either type in characters in separate lines or in one line but split them by spaces\n")
 
    #Input the code
    code = []
    while len(code) < 4:
        peg = input("The " + order[len(code)].upper() + " color of your code ({}/4): ".format(len(code)+1)).upper()
        
        if peg in colorToNum:
            code.append(colorToNum[peg])
            
        elif peg == 'Q' or peg == 'QUIT':
            return
        
        elif peg == 'C' or peg == 'CLEAR':
            code.clear()
            print("Restart this code")
        
        #User can also input multiple colors separated by blank
        elif len(code) + len(peg.split()) <= 4:
            peg = peg.split()
            tmpPegList = []
            for eachPeg in peg:
                if eachPeg in colorToNum:
                    tmpPegList.append(colorToNum[eachPeg])
                else:
                    break
            if len(code) + len(tmpPegList) <= 4:
                code.extend(tmpPegList) 
        else:
            print("\nSelect four pegs in these colors:")
            print("[R] RED / [B] BLUE / [P] PINK / [G] GREEN / [O] ORANGE / [Y] YELLOW") 
            print("[C] Clear: clear all pegs of this turn")
            print("[Q] Quit: quit to main menu\n") 
            print("Either type in characters in separate lines or in one line but split them by spaces\n")
    
    
    #Print the answer code
    answerInWord = []
    for answerInNum in code:
        answerInWord.append(numToColor[answerInNum])
    print("The answer code:", list_to_string(answerInWord, 6))
    
    
    #convert the list to string
    code_to_string = ''
    for ele in code:
        code_to_string += str(ele)
    
    #computer guessing
    #print("\n The code is: {}\n".format(code_to_string))
    computer_guess(code_to_string)
    
    #finish the computer guess new choice
    #import sys
    """
    next_action = input("Play again input 'A or again' or input orthers to return main menu : ").upper()
    
    if next_action == 'A' or 'AGAIN':
        computer_mode()
    else:
        return
    
    """
    
    pass
    
def statistics():
    """
    Gather some statistics of interest and report them (for example: average #turns required to solve the pattern)
    """
    #print("\n\n******************** Statistics *******************\n")

    try:
        #Read json data from txt file
        statList = [] 
        with open('stats.txt') as file:
            for line in file:
                data = json.loads(line)
                statList.append(data)
 
                              
        #Overall
        dataNum = len(statList)
        playerName = {}
        totalTurns = 0
        totalDuration = 0
        minTurns = 13
        minDuration = 100000000
        
        #Player
        playerDict = {}
  
   
        for data in statList:
            #Analyze overall data
            totalTurns += data['turns']
            totalDuration += float(data['duration'])
                                
            if data['turns'] < minTurns:
                minTurns = data['turns']
                minTurnsData = data
            if float(data['duration']) < minDuration:
                minDuration = float(data['duration'])
                minDurationData = data
                
            #Analyze each player's data 
            player = data['player']
            try:
                playerDict[player]['dataNum'] += 1
                playerDict[player]['totalTurns'] += data['turns']
                playerDict[player]['totalDuration'] += float(data['duration'])
                if data['turns'] < playerDict[player]['minTurns']:
                    playerDict[player]['minTurns'] = data['turns']
                if float(data['duration']) < playerDict[player]['minDuration']:
                    playerDict[player]['minDuration'] = float(data['duration'])
                    
            except KeyError:
                playerDict[player] = {}
                playerDict[player]['dataNum'] = 1
                playerDict[player]['totalTurns'] = data['turns']
                playerDict[player]['totalDuration'] = float(data['duration'])
                playerDict[player]['minTurns'] = data['turns']
                playerDict[player]['minDuration'] = float(data['duration'])

                   
        #Select a mode
        while True: 
            print("\n\n******************** Statistics *******************\n")
            print("[O] Overall: show overall user statistics")
            print("[C] Computer: show overall computer statistics")
            print("[P] Player: show every player's statistics")
            print("[T] Turns: show at most 10 winning user history sorted by turns to win")
            print("[D] Duration: show at most 10 winning user history sorted by duration of a game")
            print("[H] History: show all user history")
            print("[Q] Quit: quit to main menu\n")
              
            mode = input("Select a mode (O/C/P/T/D/H/Q): ").upper()
            
            if mode == 'O' or mode == 'OVERALL':              
                #Print overall data
                
                print("===================================================\n")
                print("The number of data in user history:", dataNum)
                print("The number of players in user history:", len(playerDict))
                
                print("\nAverage turns to win:", totalTurns/dataNum)
                print("Average time to win:", totalDuration/dataNum)
                
                
                print("\nThe minimum turns to win:", minTurns)
                print(minTurnsData['startTime'])
                print("{0} used {1} turns and spent {2:.2f} seconds to win".format(minTurnsData['player'], minTurnsData['turns'], minTurnsData['duration']))
                print("\nThe minimum time to win:", minDuration)
                print(minDurationData['startTime'])
                print("{0} used {1} turns and spent {2:.2f} seconds to win\n".format(minTurnsData['player'], minTurnsData['turns'], minTurnsData['duration']))
    
                print("===================================================\n")
                
                
            elif mode == 'C' or mode == 'COMPUTER':
                try:
                    #Read json data from txt file
                    compStatList = [] 
                    with open('comp_stats.txt') as file:
                        for line in file:
                            data = json.loads(line)
                            compStatList.append(data)
                                                  
                    #Overall
                    compDataNum = len(compStatList)
                    compTotalTurns = 0
                    compTotalDuration = 0
                    compMinTurns = 13
                    compMinDuration = 100000000
                    
                    #Analyze overall data
                    for data in compStatList:
                        compTotalTurns += data['turns']
                        compTotalDuration += float(data['duration'])
                                            
                        if data['turns'] < compMinTurns:
                            compMinTurns = data['turns']
                            compMinTurnsData = data
                        if float(data['duration']) < compMinDuration:
                            compMinDuration = float(data['duration'])
                            compMinDurationData = data
                     
                        
                    print("===================================================\n")
                    print("The number of data in computer history:", compDataNum)
                    
                    print("\nAverage turns to win:", compTotalTurns/compDataNum)
                    print("Average time to win:", compTotalDuration/compDataNum)
                    
                    
                    print("\nThe minimum turns to win:", compMinTurns)
                    print(compMinTurnsData['startTime'])
                    print("Computer spent {} seconds to win".format(minTurnsData['duration']))

                    print("\nThe minimum time to win:", compMinDuration)
                    print(compMinDurationData['startTime'])
                    print("Computer used {} turns to win\n".format(minTurnsData['turns']))
        
                    print("===================================================\n")
                                
                except FileNotFoundError:
                    print("\n\n******************** Statistics *******************\n")
                    print("Empty history\nTry again after computer plays at least once")
            
            
            elif mode == 'P' or mode == 'PLAYER':
                #Print data based on every player
                
                for player in playerDict:
                    data = playerDict[player]
                    
                    print("\n===================================================\n")
                    print("Player name:", player)
                    print("The number of data in history:", data['dataNum'])
                    
                    print("\nAverage turns to win:", data['totalTurns']/data['dataNum'])
                    print("Average time to win:", data['totalDuration']/data['dataNum'])
                    
                    
                    print("\nThe minimum turns to win:", data['minTurns'])
 
                    print("The minimum time to win:", data['minDuration'])
                    
                print("\n===================================================\n")
                       
                
            elif mode == 'T' or mode == 'TURNS':
                #Print at most 10 data sorted by turns                
                print("\n===================================================\n")
                
                sortTurns = sorted([ (data['turns'], data['duration'], data['startTime'], data['player']) for data in statList ])
                                
                topSortTurns = sortTurns[:10]

                print("Turns".center(5), "Player".center(15), "Time".center(12), '\n', sep='')
                for i in range(len(topSortTurns)):
                    print("{}".format(topSortTurns[i][0]).center(5), end='')
                    print("{}".format(topSortTurns[i][3]).center(15), end='')
                    print("{:.2f}".format(topSortTurns[i][1]).center(12))
                    
                print("\n===================================================\n")
                

            elif mode == 'D' or mode == 'DURATION':
                #Print at most 10 data sorted by duration               
                print("\n===================================================\n")
                
                sortDuration = sorted([ (data['duration'], data['turns'], data['startTime'], data['player']) for data in statList ])
                                
                topSortDuration = sortDuration[:10]

                print("Time".center(12), "Player".center(15), "Turns".center(5), '\n', sep='')
                for i in range(len(topSortDuration)):
                    print("{:.2f}".format(topSortDuration[i][0]).center(12), end='')
                    print("{}".format(topSortDuration[i][3]).center(15), end='')
                    print("{}".format(topSortDuration[i][1]).center(5))
                    
                print("\n===================================================\n")
                
                
            elif mode == 'H' or mode == 'HISTORY':
                #Print all game history               
                print("\n===================================================\n")
                
                print("Player".center(15), "Turns".center(6), "Hints".center(7), "Time".center(12), '\n', sep='')
                for data in statList:
                    print("{}".format(data['player']).center(15), end='')
                    print("{}".format(data['turns']).center(6), end='')
                    print("{}".format(data['hints']).center(7), end='')
                    print("{:.2f}".format(data['duration']).center(12), end='')
                    print(data['startTime'])
                
                print("\n===================================================\n")
                
                
            elif mode == 'Q' or mode == 'Quit':
                break
            
                      
    except FileNotFoundError:
        print("\n\n******************** Statistics *******************\n")
        print("Empty history\nTry again after you play at least once")
            
    
    pass


while(True):
    print("\n\n********************* Main menu *******************\n")
    print("Welcome to Mastermind!\n")
    print("[U] User guesses: the computer picks the initial code, and the user must guess")
    print("[C] Computer guesses: the user picks the initial code, and the computer guesses")
    print("[S] Statistics: statistics of winning history")
    print("[Q] Quit: quit the game")
    
    mode = input("Select a mode (U/C/S/Q): ").upper()
    
    if mode == 'U' or mode == 'USER GUESSES':
        user_mode()
    elif mode == 'C' or mode == 'COMPUTER GUESSES':
        computer_mode()
    elif mode == 'S' or mode == 'STATISTICS':
        statistics()
    elif mode == 'Q' or mode == 'QUIT':
        print("\nGoodbye!\n")
        print("***************************************************\n\n")
        sys.exit(0)

    
    
    
