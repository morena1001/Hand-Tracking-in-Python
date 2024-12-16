import math

import cv2
import mediapipe as mp

def distance (point1, point2) :
    return math.sqrt (math.pow (point1[0] - point2[0], 2) + (point1[1] - point2[1], 2))

def is_fist (landmarks) :
    lms = enumerate (landmarks)
    lm = next (lms)

    point_0 = {lm[1].x, lm[1].y}
    lm = next (lms)
    lm = next (lms)

    point_2 = {lm[1].x, lm[1].y}
    lm = next (lms)
    lm = next (lms)

    point_4 = {lm[1].x, lm[1].y}
    lm = next (lms)

    point_5 = {lm[1].x, lm[1].y}
    lm = next (lms)
    lm = next (lms)
    lm = next (lms)

    point_8 = {lm[1].x, lm[1].y}
    lm = next (lms)

    point_9 = {lm[1].x, lm[1].y}
    lm = next (lms)
    lm = next (lms)
    lm = next (lms)

    point_12 = {lm[1].x, lm[1].y}
    lm = next (lms)

    point_13 = {lm[1].x, lm[1].y}
    lm = next (lms)
    lm = next (lms)
    lm = next (lms)

    point_16 = {lm[1].x, lm[1].y}
    lm = next (lms)

    point_17 = {lm[1].x, lm[1].y}
    lm = next (lms)
    lm = next (lms)
    lm = next (lms)

    point_20 = {lm[1].x, lm[1].y}
    

    # Check 4 is closer to 17 than 2
    print ("WHY")
    dist4_17 = distance (point_4, point_17)
    dist2_17 = distance (point_2, point_17)

    print (dist2_17, dist4_17)

    if (dist2_17 < dist4_17) :
        return False

    # Check that 8 is closer to 0 than 5
    dist8_0 = distance (point_8, point_0)
    dist5_0 = distance (point_5, point_0)

    if (dist5_0 < dist8_0) :
        return False

    # Check that 12 is closer to 0 than 9
    dist12_0 = distance (point_12, point_0)
    dist9_0 = distance (point_9, point_0)

    if (dist9_0 < dist12_0) :
        return False

    # Check that 16 is closer to 0 than 13
    dist16_0 = distance (point_16, point_0)
    dist13_0 = distance (point_13, point_0)

    if (dist13_0 < dist16_0) :
        return False

    # Check that 20 is closer to 0 than 17
    dist20_0 = distance (point_20, point_0)
    dist17_0 = distance (point_17, point_0)
    
    if (dist17_0 < dist20_0) :
        return False
    
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
            print (is_fist (handLm.landmark))
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
