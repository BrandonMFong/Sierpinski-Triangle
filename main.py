# main.py
# Brando 1/26/2021
# 
"""
Generate the data of the following task:

Using the three points A(0,0), B(1,2) and C(2,0).

Starting at the point X (1,1) repeat the following steps 10,000 times

1. roll a dice (random number generator) and allocate each number with one of the points

2. update the point X as the midpoint between X and the associated point, e.g.. A if the roll was 1 or 2, B if the roll was 3 or 4, C otherwise

Keep track of the updated Xs and plot where the points in a scatterplot
"""

### Modules ###
import pandas as pb
import numpy as np 
import matplotlib.pyplot as plt 

### Variables ### 
xAxis = 0
yAxis = 1
indexArray = 1
loopLimit = 10000
arrayA = np.array([0,0])
arrayB = np.array([1,2])
arrayC = np.array([2,0])
arrayX = np.array([1,1])
tempArray = np.array([0,0])
xPointArray = np.zeros([loopLimit,2])

print("\nWeek 1\n=====================\n")

# "Starting at the point X (1,1)"
xPointArray[0] = arrayX

print("\nX Point values before:\n")
print(xPointArray)

while indexArray < loopLimit:
    tempArray = np.array([0,0])
    randomValue = np.random.randint(1,6) # Get random number 

    # Assign A, B, or C according to the random dice roll 
    if randomValue == 1 or randomValue == 2:
        tempArray = arrayA 
    elif randomValue == 3 or randomValue == 4:
        tempArray = arrayB 
    else:
        tempArray = arrayC  

    # print("Midpoint of ", tempArray, " and ", xPointArray[indexArray - 1])
    # Calculate midpoint
    xPointArray[indexArray, xAxis] = (tempArray[xAxis] + xPointArray[indexArray - 1, xAxis]) / 2
    xPointArray[indexArray, yAxis] = (tempArray[yAxis] + xPointArray[indexArray - 1, yAxis]) / 2

    indexArray = indexArray + 1

print("\nX Point values after:\n")
print(xPointArray)

# Expected outcome: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#/media/File:Sierpinski_triangle.svg 
# TODO figure out why outcome is not looking right  
plt.plot(xPointArray[0:, xAxis], xPointArray[0:, yAxis], 'o', color='black')
plt.show()
