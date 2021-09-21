import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
pTime = 0

draw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
face_mesh = mpFaceMesh.FaceMesh(max_num_faces = 3)

drawSpec = draw.DrawingSpec(thickness = 1, circle_radius = 1)

while True:

    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLm in results.multi_face_landmarks:
            draw.draw_landmarks(img,faceLm,mpFaceMesh.FACEMESH_TESSELATION,
            drawSpec,drawSpec)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow('Image',img)
    cv2.waitKey(1)