"""
File name: hw3b.py
Students: Chia-Chun Chao
Deadline: Tuesday, Feb. 27th
Course: CS205 Software Engineering

Assignment 3b
This code solves a simple problem.  What problem?  
Rewrite this as good code, in the language of your choice.

This code calculates the probability that 
in a 3*3 square, a point locates in the inscribed circle of the square.
"""

import random

count = 0 #Times of the situation happens

for total in range(1,10000+1):#Run for 10000 times

    #Randomly generate x-coordinate and y-coordinate and make x and y in the range from 0 to 3
    x = 3 * random.random()
    y = 3 * random.random()
    
    #Move the position of the origin and make x and y in the range from -1.5 to 1.5 
    x -= 1.5
    y -= 1.5
    
    #Calculate the distance from the origin to the point
    #The actual distance is (x^2+y^2)^(1/2). Simplify it as x^2+y^2
    distance = x*x + y*y
    
    #1.5^2 = 2.25
    #All points, where the distance is 2.25, form a circle. The radius of the circle is 1.5
    
    #Increase the count when the generated point locates in the circle
    if distance < 2.25:
        count += 1


print("Calculate the probability that in a 3*3 square, a point locates in the inscribed circle of the square.")
print("\nProbability: {:.2f}%".format( 100.0 * count / 10000))
