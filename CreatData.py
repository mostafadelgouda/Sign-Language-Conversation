# normal mediapipe

import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
#================================================
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
#================================================
cap1 = cv2.VideoCapture(0)

cap1.set(3,3000)
cap1.set(4,3000)
w=cap1.get(3)
h=cap1.get(4)

print(w)
print(h)
count=0
sign_image=np.ones((1500,1500))
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap1.isOpened():
        ret, frame = cap1.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)
        # Set flag
        image.flags.writeable = False
        # Detections
        results = hands.process(image)    
        # Set flag to true
        image.flags.writeable = True
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Detections
#         print(results)
        
        # Rendering results
        if results.multi_hand_landmarks:
            
            for hand in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
#                                         mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=4),
#                                         mp_drawing.DrawingSpec(color=(250, 255, 250), thickness=8, circle_radius=-1),
#                                          )
   
                count=count+1
                xl=[]
                yl=[]
                zl=[]

                for point in hand.landmark:
                    xl.append(point.x)
                    yl.append(point.y)
                    zl.append(point.z)
                    
                x1=int(min(xl)*w)-80
                y1=int(min(yl)*h)-50
                x2=int(max(xl)*w)+50
                y2=int(max(yl)*h)+50

            cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),1)  
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            sign_image=image[y1:y2,x1:x2]
#             sign_image=cv2.resize(sign_image,(555,555))    
            try:
                sign_image=cv2.resize(sign_image,(300,300))
                
                
#                 sign_image = cv2.cvtColor(sign_image, cv2.COLOR_RGB2GRAY)
#                 cv2.imshow("sign image",sign_image)
            except:
                sign_image=np.ones((300,300))
#                 cv2.imshow("sign image",sign_image)
#                 print('errrrrrrr')
       
        # print(sign_image) 
        cv2.imshow('Hand Tracking', image)
         #Save our image    
        cv2.imwrite('F:/VS Code/Grad k7yan/data/zal/{}.jpg'.format(uuid.uuid1()), sign_image)
        #print((os.path.join('data', '{}.jpg'.format(uuid.uuid1()))))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap1.release()
cv2.destroyAllWindows()