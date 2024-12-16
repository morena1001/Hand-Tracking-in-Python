import math

import cv2
import mediapipe as mp

def distance (point1, point2) :
    return math.sqrt (math.pow (point1[0] - point2[0], 2) + (point1[1] - point2[1], 2))

def is_fist (landmarks) :
    # for thumb
    # "draw" line from id 0 to id 9, 
    # if id 4 is closer to that "line" than id 2, count it toward a fist

    #for fingers

    lms = enumerate (landmarks)

    # for lm in lms :
    #     print (lm[0], lm[1].x, lm[1].y)
    
    point_0 = {lms[0][1].x, lms[0][1].y}
    print (lms[0])
    # print (point_0)
    # check distance between 0 and 4
    



    # for id, lm in enumerate (landmarks) :
        
        
        # print (lm.x, lm.y)
    
    return True

vid = cv2.VideoCapture (0) # 1 for external webcam
vid.set(3, 960)

mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils
Hands = mphands.Hands (max_num_hands = 1, min_detection_confidence = 0.7, min_tracking_confidence = 0.6)

while True :
    success, frame = vid.read ()

    # Convert bgr to rgb
    RGBframe = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)
    result = Hands.process (RGBframe)

    # cv2.circle (frame, (5, 5), 10, (0, 0, 255), cv2.FILLED)
    # cv2.circle (frame, (frame.shape[1] - 5, 5), 10, (0, 255, 255), cv2.FILLED)
    # cv2.circle (frame, (frame.shape[1] - 5, frame.shape[0] - 5), 10, (255, 0, 255), cv2.FILLED)
    # cv2.circle (frame, (5, frame.shape[0] - 5), 10, (255, 255, 0), cv2.FILLED)
    
    if result.multi_hand_landmarks :
        # print ("hand found")
        for handLm in result.multi_hand_landmarks :
            # print (handLm)
            mpdraw.draw_landmarks (frame, handLm, mphands.HAND_CONNECTIONS)
            is_fist (handLm.landmark)
            for id, lm in enumerate (handLm.landmark) :
                h, w, _ = frame.shape
                cx, cy = int (lm.x * w), int (lm.y * h)
                # print (id, cx, cy)
                # cv2.circle (frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

                # if id == 4 : 
                #     Tx, Ty = cx, cy
                #     cv2.circle (frame, (Tx, Ty), 6, (255, 0, 0), cv2.FILLED)

                # if id == 8 : 
                #     cv2.circle (frame, (cx, cy), 6, (255, 0, 0), cv2.FILLED)
                #     cv2.line (frame, (cx, cy), (Tx, Ty), (255, 0, 255), 5)

    # cv2.imshow ("rgbvideo", RGBframe)
    frame = cv2.flip (frame, 1)
    cv2.imshow ("video", frame)
    cv2.waitKey (1)
