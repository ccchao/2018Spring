"""
1. pick a list of 100 random integers in the range -500 to 500
2. find the largest and smallest values in the list
3. find the second-largest and second-smallest values in the list
4. calculate the median value of the elements in the list
"""

import random

#Generate a list containing 100 randomly generated integers ranged between -500 and 500
intList = []
for i in range(100):
    intList.append(random.randint(-500,500))
    
#Sort the list to find the largest two, the smallest two, and the median values
intList.sort()

#Show the result
print("The largest value in the list:", intList[0])
print("The smallest value in the list:", intList[-1])
print("The second-largest value in the list:", intList[1])
print("The second-smallest value in the list:", intList[-2])
print("the median value of the elements in the list:", (intList[49]+intList[50])/2)
