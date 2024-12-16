import cv2
import mediapipe as mp

vid = cv2.VideoCapture (0) # 1 for external webcam
vid.set(3, 960)

mphands = mp.solutions.hands
Hands = mphands.Hands (max_num_hands = 1, min_detection_confidence = 0.7, min_tracking_confidence = 0.6)

while True :
    success, frame = vid.read ()

    # Convert bgr to rgb
    RGBframe = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)
    result = Hands.process (RGBframe)
    print (result)

    # cv2.imshow ("rgbvideo", RGBframe)
    cv2.imshow ("video", frame)
    cv2.waitKey (1)
