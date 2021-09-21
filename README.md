# Real Time Computer Vision

Computer vision, one of the deep learning applications, was used in this work repository. Many studies have been carried out using OpenCV and mediapipe libraries and source codes have been added to the repository.

## Files


|    Files            |Description|                         |
|----------------|-------------------------------|-----------------------------|
|[Output_img](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/tree/main/Output_img "Output_img")|`Sample output images`                     
|[HandTracking.py](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/HandTracking.py "HandTracking.py")         |`real-time detection of hand points` 
|[Hand_Module.py](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/Hand_Module.py "Hand_Module.py")         |`Modulated script of HandTracking file` 
|[Volume_Hand_Control.py](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/Volume_Hand_Control.py "Volume_Hand_Control.py")         |`volume control with finger spacing` 
|[face_mesh.py](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/face_mesh.py "face_mesh.py")         |`detection of face points` 
|[pose_estimation.py](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/pose_estimation.py "pose_estimation.py")         |`real-time detection of human poses` 
|[requirements.txt](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/requirements.txt "requirements.txt") |`required libraries` 

## Results

### 1- Hand Tracking
With the help of the mediapipe library, the points on the hand are detected in real time. The output is a screenshot taken from the real-time image.

![Hands](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/Output_img/Hands1.png)

### 2- Hand volume control
With the help of the mediapipe library, the points on the hand are detected in real time. Then the sound level of the computer is adjusted with the distance between the fingers.

![Volume](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/Output_img/Volume.png)

### 3- Face Mesh
The points on the face are detected in real time using mediapipe and opencv, and these points are combined and masked. The output is a screenshot from the real-time image.

![Face](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/Output_img/face.png)

### 4- Pose Estimation
real-time pose detection is performed by detecting points on the human body.

![Pose](https://github.com/Onurryilmazz/Real-Time-Computer-Vision/blob/main/Output_img/pose.png)
