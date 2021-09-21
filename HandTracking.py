import cv2
import mediapipe as mp
import time 

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False,max_num_hands=2)

draw = mp.solutions.drawing_utils

pTime,cTime = 0,0

while True:

    succes, img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handL in results.multi_hand_landmarks:
            for id, lm in enumerate(handL.landmark):  #dönüm noktası (bilek,parmak vb) tespiti
                h, w, c =  img.shape
                cx, cy = int(lm.x*w) , int(lm.y*h)
                if id in [0,4,8,12,16,20]:
                    cv2.circle(img,(cx,cy),10,(200,20,20),cv2.FILLED)

            draw.draw_landmarks(img,handL,mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow('Image',img)
    cv2.waitKey(1)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break