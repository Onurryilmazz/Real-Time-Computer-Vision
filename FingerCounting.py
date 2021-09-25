import cv2
import mediapipe as mp
import time
import os
import Hand_Module as htm

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
overlayList = []

for imgPath in myList:
    
    image = cv2.imread(f"{folderPath}/{imgPath}")
    image = cv2.resize(image,(200,200))
    overlayList.append(image)

print(len(overlayList))

pTime = 0


detector = htm.handDetector(detectionCon=0.75,)
tipsId = [4,8,12,16,20]    #finger location index

while True:

    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        fingers = []
        """
        Right Hands
        """

        #Baş parmak kontrolu
        if lmList[tipsId[0]][1] > lmList[tipsId[0]-1][1]:
            fingers.append(1)

        else:
            fingers.append(0)

        for id in range(1,5):

            if lmList[tipsId[id]][2] < lmList[tipsId[id]-2][2]:
                fingers.append(1)

            else:
                fingers.append(0)

        totalFingers = fingers.count(1)


        print(totalFingers)

        img[0:200,0:200] = overlayList[totalFingers-1]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (500, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow('Image',img)
    cv2.waitKey(1)