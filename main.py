"""
main.py
Author: Brando 

Problem: 
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
size = 0
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

xPointArray[0] = arrayX # "Starting at the point X (1,1)"
size = xPointArray.shape[0] # Get the number of rows of the array 
while indexArray < size:
    tempArray = np.array([0,0]) # reset 
    randomValue = np.random.randint(1,7) # Get random number 

    # Assign A, B, or C according to the random dice roll 
    if randomValue == 1 or randomValue == 2:
        tempArray = arrayA 
    elif randomValue == 3 or randomValue == 4:
        tempArray = arrayB 
    else:
        tempArray = arrayC  

    # Calculate midpoint
    xPointArray[indexArray] = (tempArray + xPointArray[indexArray - 1]) / 2

    indexArray = indexArray + 1

plt.plot(xPointArray[0:, xAxis], xPointArray[0:, yAxis], '.', color='black')
plt.show()
