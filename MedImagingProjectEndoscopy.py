import cv2
import numpy as np 
import time
import random

#user defined parameters for images' sizes
nOne = 100
nTwo = 100
lOne = 200
lTwo = 200
oOne = 500
oTwo = 500
pOne = 1000
pTwo = 1000
qOne = 5000
qTwo = 5000

# Reading an image in default mode
Img = np.ones((nOne, nTwo, 3), np.uint8)
ImgTwo = np.ones((lOne, lTwo, 3), np.uint8)
ImgThree = np.ones((oOne, oTwo, 3), np.uint8)
ImgFour = np.ones((pOne, pTwo, 3), np.uint8)
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

#generates random pixel cooridantes to detect
coorOne = random.randint(0, qOne)
coorTwo = random.randint(0, qTwo)


for h in range(0, 24):
# runs through image and creates 
# objects based on the user defined 
# paramaters
    for i in range(0, qOne):
        for j in range(0, qTwo):

            if((i == coorOne) and (j == coorTwo)):
                ImgFive[i,j] = 0 
       
            # runs through image and when not in either the rectangle or ellipse, sets equal to the signal intensity of object A
            else:
                ImgFive[i,j] = signalIntensityA

    startTime = time.time()
    #runs through image 
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
            
    print(finishtime - startTime)        

