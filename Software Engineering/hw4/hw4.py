"""
File name: hw4.py
Students: Chia-Chun Chao
Deadline: Thursday, March 29, 2018
Course: CS205 Software Engineering

Assignment 4: Birthdays
Now that we've talked about numerical simulations, 
you can write a program to analyze the probability that 
two people in a group of people share a common birthday (month + day).

In a group of five people, what's the approximate probability that two of them share a birthday?

In a group of fifteen people, what's the approximate probability that two of them share a birthday?

How big does the group have to be in order for the probability to be > 50%?
"""


import random
from collections import Counter

############################################################

"""
Generate a list of birthday with `total` elements, and return 1 if two of them share a birthday and 0 if none
"""
def same_bday_bool(total):
    birthList = []#Store birthday of each person
    
    for person in range(total):
        day = random.randint(1,365) #Generate a random birthday
        
        #If there's already a person have the birthday, return 1, or keep calculating
        if day in birthList:
            return 1 
        else:
            birthList.append(random.randint(1,365))
    
    return 0 #There are not two people sharing a birthday in the group of `total` people

############################################################
    
"""
Loop for `loop` times and calculate the probability that two people in a group of `group` people share a birthday
"""
def prob_share(loop, group):
    #Add 1 if there are two people sharing a birthday and 0 if not
    shareBDay = 0
    for times in range(loop):
        shareBDay += same_bday_bool(group) #Calculate how many times there are two people sharing a birthday
    
    prob = 100.0 * shareBDay / loop
    #print("\nProbability of {:d} people: {:.2f}%".format(group, prob))
    
    return prob

############################################################

"""
Print the probability with the size of group
"""
def print_prob(group, prob):
    print("\nProbability of {:d} people: {:.2f}%".format(group, prob))


############################################################

loop = 20000
print("\nLoop for {} times to find the probability".format(loop))
print('-----------------------------------')

print('In a group of five people, what\'s the approximate probability that two of them share a birthday?')
print_prob(5, prob_share(loop, 5))

print('-----------------------------------')

print('In a group of fifteen people, what\'s the approximate probability that two of them share a birthday?')
print_prob(15, prob_share(loop, 15))

print('-----------------------------------')

print('How big does the group have to be in order for the probability to be > 50%?')

#Find the group number with the probability larger than 50%
lastProb = 0
for group in range(20, 366):
    prob = prob_share(loop, group)
    
    if prob >= 50:
        #Find the previous one
        print_prob(group-1, lastProb) #Less than 50%
        #Find the exact one
        print_prob(group, prob) #Larger than 50%
        #Find the next
        prob = prob_share(loop, group+1)
        print_prob(group+1, prob) #Larger than 50%
        
        break
    
    else:
        lastProb = prob

print("\nIn about half cases, a group of 23 has the probability larger than 50%, so 24 is more reliable.")

"""
total = 0
loop2 = 1000
for times in range(loop2):
    if prob_share(loop, 23) >= 50:
        total += 1
print(100.0 * total / loop2)
"""
