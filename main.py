import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
cap = cv2.VideoCapture(0)
cap.set(3,640)#the property of the width is 3 and we set its value to 640
cap.set(4,480)#the property of the height is 4 and we set its value to 480
detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0,0] #AI , Player
imgAI = None #the AI move image, None until the AI has played a move

while True:
    imgBG = cv2.imread("Resources/background.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.92)#for the output image we right none 420/480=0.875
    imgScaled = imgScaled[:,68:480]# 640*0.875 = 560-400 =160*2 = 80
    # find hand
    hands, img = detector.findHands(imgScaled)

    if startGame:

        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)
            if timer >3:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers ==[0,0,0,0,0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3
                    randomNumber = random.randint(1,3)
                    imgAI = cv2.imread(f'Resources/{randomNumber}.png',cv2.IMREAD_UNCHANGED)
                    imgAI = cv2.resize(imgAI, (0, 0), None, 0.7, 0.7)
                    imgBG = cvzone.overlayPNG(imgBG,imgAI,(149,220))

                    #player wins
                    if(playerMove == 1 and randomNumber ==3) or \
                      (playerMove == 2 and randomNumber == 1) or \
                      (playerMove == 3 and randomNumber == 2):
                        scores[1]+=1
                        # AI wins
                    if (playerMove == 3 and randomNumber == 1) or \
                       (playerMove == 1 and randomNumber == 2) or \
                       (playerMove == 2 and randomNumber == 3):
                         scores[0] += 1




    imgBG[220:662, 792:1204] = imgScaled # the first vale of [] will be the height and the second value will be the width

    if stateResult and imgAI is not None:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (130, 290))

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    #cv2.imshow('imgame', img)
    cv2.imshow('BG', imgBG)
    #cv2.imshow('scaled', imgScaled)

    key = cv2.waitKey(1)
    if key ==ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
        imgAI = None #a new round starts, so the old AI move is cleared