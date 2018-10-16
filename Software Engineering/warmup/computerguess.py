"""
File name: computerguess.py
Students: Junxiao Chen
Deadline: Thursday, Feb. 15th

Warm-up Project
Simulation of the board game Mastermind
"""
from codecheck import code_check
import datetime
import json

colorToNum = {'R': 0, 'RED': 0, '0': 0,
              'B': 1, 'BLUE': 1, '1': 1,
              'P': 2, 'PINK': 2, '2': 2,
              'G': 3, 'GREEN': 3, '3': 3,
              'O': 4, 'ORANGE': 4, '4': 4,
              'Y': 5, 'YELLOW': 5, '5': 5}

numToColor = {0: 'RED',
              1: 'BLUE',
              2: 'PINK',
              3: 'GREEN',
              4: 'ORANGE',
              5: 'YELLOW',
              6: 'WHITE', #correct in both color and position
              7: 'BLACK'} #correct color code peg placed in the wrong position

              
def list_to_string(inputList, width):
    """
    Print the input list, and each item is printed in the center of width
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

def computer_guess(answer_code):
    """ 
    :type answer_code: must be a string to avoid compare error.
    computer guess the user coding
    """
    if(type(answer_code) != type('') or len(answer_code) != 4):
        print('Wrong type of code might result the computer guess fail.')
        return
    
    guess_code = "0011"
    pool = generate_pool()
    candidate_list = list(pool)
    num_turn = 0
    used = set()
    
     
    #Store each guess and key to show previous guesses and results
    guessList = []
    keyList = []
    startTime = datetime.datetime.now()

    
    while num_turn < 12:
        num_turn += 1
        used.add(guess_code)
        
        guessList.append([int(peg) for peg in guess_code])
        
        #print("Guess number {}: {}".format(num_turn, guess_code))
        result_list = code_check(guess_code, answer_code)
        
        keyList.append(result_list)
        
        #print("Result is: ")
        #print(result_list)
        
        if result_list == [7, 7, 7, 7]:
            #print("Wow, computer just won this game!")
            break
        candidate_list = eliminate_impossible(candidate_list, guess_code, result_list)
        if len(candidate_list) == 1:
            guess_code = candidate_list[0]
        else:
            guess_code = get_next_guess(pool, used, candidate_list)
   

    #Print guess and key of each turn

    print("\n\n===================================================")
    print("Computer's guesses and keys ({}/12):".format(num_turn),'\n')
    for i in range(12): 
        #Show index, guess, and key
        if i < num_turn:
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
    if result_list.count(7) == 4:
        print("Wow, computer just won this game!\n")
        
        
        #Store game time
        duration = (datetime.datetime.now() - startTime).total_seconds()
        
        print("\nComputer took {0} seconds and {1} steps to win\n\n".format(duration, num_turn))
        
        #Store data in json file
        data = {'turns': num_turn,
                'startTime': datetime.datetime.strftime(startTime, "%Y-%m-%d %H:%M:%S"),
                'duration': duration}
        with open('comp_stats.txt', 'a') as file:
            file.write(json.dumps(data))
            file.write('\n')
     
    else:
        print("Computer failed on this game\n")
                    
    pass
    
    
    
        
def generate_pool():
    
    """
    :rtype pool: list   0 - 1295 based 5
    
    Generate the pool of all possible candiates
    """
    pool = []
    for i in range(1296):
        pool.append(convert_base(i))
    return pool

def convert_base(num, base=6):
    """
    :type num:  int     decimal number
    :type base: int     the base of number that need to convert to
    :rtype ans: list    0 - 1295 based 5
    
    Convert any number into any specified base
    """
    sign = 1
    ans = ''
    if num == 0:
        return '0000'
    elif num < 0:
        sign = -1
    num *= sign
    while num > 0:
        ans = str(num % base) + ans
        num //= base
    while len(ans) < 4:
        ans = '0' + ans
    if sign < 0:
        ans = '-' + ans
    return ans

def eliminate_impossible(candidate_list, last_guess, result_list):
    """
    Eliminate impossible candidates that can't produce the same result
    """
    new_candidate_list = []
    for candidate in candidate_list:
        if code_check(last_guess, candidate) == result_list:
            new_candidate_list.append(candidate)
    return new_candidate_list

def get_next_guess(pool, used, candidate_list):
    """  
    Get the index of the next guess
    """
    max_score = -100
    res = ""
    for guess in pool:
        if guess in used:
            continue
        res_dict = {}
        for candidate in candidate_list:
            result_list = code_check(guess, candidate)
            right_pos = 0
            wrong_pos = 0
            for num in result_list:
                if num == 6:
                    wrong_pos += 1
                elif num == 7:
                    right_pos += 1
            try:
                res_dict[right_pos * 10 + wrong_pos] += 1
            except KeyError:
                res_dict[right_pos * 10 + wrong_pos] = 1
        max_hit = -100
        for key in res_dict:
            if res_dict[key] > max_hit:
                max_hit = res_dict[key]
        score = len(candidate_list) - max_hit
        if max_score < score:
            res = guess
            max_score = score
    return res

#computer_guess('2351')