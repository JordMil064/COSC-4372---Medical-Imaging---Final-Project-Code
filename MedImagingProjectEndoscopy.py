import cv2
import numpy as np 
import time
import random

#user defined parameters for images' sizes
qOne = 5000
qTwo = 5000

# In an image in default mode
ImgFive = np.ones((qOne, qTwo, 3), np.uint8)
    
# Window name in which image is displayed
window_name = 'Image'

#user defined parameters
signalIntensityA = 128
posA1 = 50
posA2 = 100
lengthA1 = 50
lengthA2 = 50
signalIntensityB = 254
posB1 = 40
posB2 = 80
lengthB1 = .25
lengthB2 = .25
signalIntensityC = 2
posC1 = 75
posC2 = 75
lengthC1 = 12
lengthC2 = 18

startTime = 0
finishtime = 0
actualtime = 0

passed = 0
failed = 0
totalNum = 0

# repeats for 24 times
for h in range(0, 24):

#generates random pixel cooridantes to detect
    coorOne = random.randint(0, qOne)
    coorTwo = random.randint(0, qTwo)


# runs through image and creates 
# objects based on the user defined 
# paramaters
    for i in range(0, qOne):
        for j in range(0, qTwo):

            if((i == coorOne) and (j == coorTwo)):
                ImgFive[i,j] = 0 
       
            # runs through image and when not the abnormality, 
            # sets equal to the signal intensity of object A
            else:
                ImgFive[i,j] = signalIntensityA

    startTime = time.time()
    # runs through image and checks 3 x 3 area
    # of the image for the abnormality
    for i in range(1, qOne-1):
        for j in range(1, qTwo-1):

            if((i-1 == coorOne) and (j-1 == coorTwo)):
                finishtime = time.time()

            if((i == coorOne) and (j == coorTwo)):
                finishtime = time.time()

            if((i+1 == coorOne) and (j+1 == coorTwo)):
                finishtime = time.time()

            if((i+1 == coorOne) and (j-1 == coorTwo)):
                finishtime = time.time()

            if((i-1 == coorOne) and (j+1 == coorTwo)):
                finishtime = time.time()

            if((i == coorOne) and (j-1 == coorTwo)):
                finishtime = time.time()
            
            if((i-1 == coorOne) and (j == coorTwo)):
                finishtime = time.time()

            if((i == coorOne) and (j+1 == coorTwo)):
                finishtime = time.time()
            
            if((i+1 == coorOne) and (j == coorTwo)):
                finishtime = time.time()

    # calculates execution time         
    print(finishtime - startTime)     
    
    #totals and finds the average for the times to compare to
    totalNum = totalNum + (finishtime - startTime)
    average = totalNum / 24

    # sums ups both the passing and failing times
    if((finishtime - startTime) < average):
        passed = passed + 1
    elif((finishtime - startTime) >= average):
        failed = failed + 1

# outputs results
print("passed: ", passed)
print("failed: ", failed)
