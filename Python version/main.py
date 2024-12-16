import cv2
import mediapipe as mp

vid = cv2.VideoCapture (0) # 1 for external webcam
vid.set(3, 960)

while True :
    success, frame = vid.read ()

    cv2.imshow ("video", frame)
    cv2.waitKey
