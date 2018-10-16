"""
File name: hw3a.py
Students: Chia-Chun Chao
Deadline: Tuesday, Feb. 27th
Course: CS205 Software Engineering

Assignment 3a
What does this code do?  It's solving a simple problem.  
Rewrite it as good code, in the language of your choice.

This code calculates the probability that 
three randomly generated numbers are in the range [0.0, 1/3), [1/3, 2/3), and [2/3, 1) separately.
"""

import random

count = 0 #Times of the situation happens
numList = [] #Store generated numbers 

for total in range(1,10000+1):#Run for 10000 times

    #Generate 3 floating numbers
    for num in range(3):
        numList.append(random.random())
        
    #Sort numbers for comparing
    numList.sort()
    
    #Increase the count when the numbers are in the range [0.0, 1/3), [1/3, 2/3), and [2/3, 1)
    if numList[0] < 1/3 and (numList[1] >= 1/3 and numList[1] < 2/3) and numList[2] >= 2/3:
        count += 1
    
    #Reset the list    
    numList.clear()
 
    
print("Calculate the probability that three randomly generated numbers are in the range [0.0, 1/3), [1/3, 2/3), and [2/3, 1) separately.")
print("\nProbability: {:.2f}%".format( 100.0 * count / 10000))
