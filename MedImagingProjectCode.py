import cv2
import numpy as np 
import time

#user defined parameters for image size
nOne = 100
nTwo = 100
lOne = 200
lTwo = 200
oOne = 500
oTwo = 500
pOne = 1000
pTwo = 1000
qOne = 10000
qTwo = 10000

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
# runs through image and creates 
# objects based on the user defined 
# paramaters
startTime = time.time()
for i in range(0, nOne):
    for j in range(0, nTwo):
        
        # runs through image and creates rectangle object when running through position where rectangle is at 
        if((((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB2, 2)/((lengthB2/2 * lengthB2/2))) and ((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB1, 2)/(lengthB1/2 * lengthB1/2)):
            Img[i,j] = signalIntensityB

        # runs through image and creates ellipse object when running through position where ellipse is at
        elif((((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC2, 2)/((lengthC2/2 * lengthC2/2))) and ((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC1, 2)/(lengthC1/2 * lengthC1/2)):
            Img[i,j] = signalIntensityC

        # runs through image and when not in either the rectangle or ellipse, sets equal to the signal intensity of object A
        else:
            Img[i,j] = signalIntensityA

finishtime = time.time()

print(finishtime - startTime)

# Displaying the actual image (100 x 100)
cv2.imshow(window_name, Img)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized = cv2.resize(Img, (500,500), interpolation = cv2.INTER_AREA)    
#resizes image to be more visible
cv2.imshow(window_name, resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


signalIntensityA = 128
posA1 = 50 * 2
posA2 = 100 * 2
lengthA1 = 50 * 2
lengthA2 = 50 * 2
signalIntensityB = 254
posB1 = 15 * 2
posB2 = 35 * 2
lengthB1 = .25 * 2
lengthB2 = .25 * 2
signalIntensityC = 2
posC1 = 75 * 2
posC2 = 75 * 2
lengthC1 = 12 * 2
lengthC2 = 18 * 2

startTime = 0
finishtime = 0
actualtime = 0
# runs through image and creates 
# objects based on the user defined 
# paramaters
startTime = time.time()
for i in range(0, lOne):
    for j in range(0, lTwo):
        
        # runs through image and creates rectangle object when running through position where rectangle is at 
        if((((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB2, 2)/((lengthB2/2 * lengthB2/2))) and ((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB1, 2)/(lengthB1/2 * lengthB1/2)):
            ImgTwo[i,j] = signalIntensityB

        # runs through image and creates ellipse object when running through position where ellipse is at
        elif((((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC2, 2)/((lengthC2/2 * lengthC2/2))) and ((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC1, 2)/(lengthC1/2 * lengthC1/2)):
            ImgTwo[i,j] = signalIntensityC

        # runs through image and when not in either the rectangle or ellipse, sets equal to the signal intensity of object A
        else:
            ImgTwo[i,j] = signalIntensityA

finishtime = time.time()

print(finishtime - startTime)
# Displaying the actual image (100 x 100)
cv2.imshow(window_name, ImgTwo)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized = cv2.resize(ImgTwo, (500,500), interpolation = cv2.INTER_AREA)    

#resizes image to be more visible
cv2.imshow(window_name, resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

signalIntensityA = 128
posA1 = 50 * 5
posA2 = 100 * 5
lengthA1 = 50 * 5
lengthA2 = 50 * 5
signalIntensityB = 254
posB1 = 15 * 5
posB2 = 35 * 5
lengthB1 = .25 * 5
lengthB2 = .25 * 5
signalIntensityC = 2
posC1 = 75 * 5
posC2 = 75 * 5
lengthC1 = 12 * 5
lengthC2 = 18 * 5

startTime = 0
finishtime = 0
actualtime = 0
# runs through image and creates 
# objects based on the user defined 
# paramaters
startTime = time.time()
for i in range(0, oOne):
    for j in range(0, oTwo):
        
        # runs through image and creates rectangle object when running through position where rectangle is at 
        if((((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB2, 2)/((lengthB2/2 * lengthB2/2))) and ((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB1, 2)/(lengthB1/2 * lengthB1/2)):
            ImgThree[i,j] = signalIntensityB

        # runs through image and creates ellipse object when running through position where ellipse is at
        elif((((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC2, 2)/((lengthC2/2 * lengthC2/2))) and ((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC1, 2)/(lengthC1/2 * lengthC1/2)):
            ImgThree[i,j] = signalIntensityC

        # runs through image and when not in either the rectangle or ellipse, sets equal to the signal intensity of object A
        else:
            ImgThree[i,j] = signalIntensityA

finishtime = time.time()

print(finishtime - startTime)

# Displaying the actual image (100 x 100)
cv2.imshow(window_name, ImgThree)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized = cv2.resize(ImgThree, (500,500), interpolation = cv2.INTER_AREA)    

#resizes image to be more visible
cv2.imshow(window_name, resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

signalIntensityA = 128
posA1 = 50 * 10
posA2 = 100 * 10
lengthA1 = 50 * 10
lengthA2 = 50 * 10
signalIntensityB = 254
posB1 = 15 * 10
posB2 = 35 * 10
lengthB1 = .25 * 10
lengthB2 = .25 * 10
signalIntensityC = 2
posC1 = 75 * 10
posC2 = 75 * 10
lengthC1 = 12 * 10
lengthC2 = 18 * 10

startTime = 0
finishtime = 0
actualtime = 0
# runs through image and creates 
# objects based on the user defined 
# paramaters
startTime = time.time()
for i in range(0, pOne):
    for j in range(0, pTwo):
        
        # runs through image and creates rectangle object when running through position where rectangle is at 
        if((((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB2, 2)/((lengthB2/2 * lengthB2/2))) and ((np.power(i - (abs(lengthB2 - posB2)), 2))/(lengthB2/2 * lengthB2/2)) + ((np.power(j - (abs(lengthB1 - posB1)), 2))/(lengthB1/2 * lengthB1/2)) < np.power(lengthB1, 2)/(lengthB1/2 * lengthB1/2)):
            ImgFour[i,j] = signalIntensityB

        # runs through image and creates ellipse object when running through position where ellipse is at
        elif((((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC2, 2)/((lengthC2/2 * lengthC2/2))) and ((np.power(i - (abs(lengthC2 - posC2)), 2))/(lengthC2/2 * lengthC2/2)) + ((np.power(j - (abs(lengthC1 - posC1)), 2))/(lengthC1/2 * lengthC1/2)) < np.power(lengthC1, 2)/(lengthC1/2 * lengthC1/2)):
            ImgFour[i,j] = signalIntensityC

        # runs through image and when not in either the rectangle or ellipse, sets equal to the signal intensity of object A
        else:
            ImgFour[i,j] = signalIntensityA

finishtime = time.time()

print(finishtime - startTime)
# Displaying the actual image (100 x 100)
cv2.imshow(window_name, ImgFour)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized = cv2.resize(ImgFour, (500,500), interpolation = cv2.INTER_AREA)    

#resizes image to be more visible
cv2.imshow(window_name, resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

