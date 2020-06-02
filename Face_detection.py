import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#python Face_detection.py
pic = cv2.imread('215.png')

scale_factor = 1.2

while 1:
    face = face_cascade.detectMultiScale(pic,scale_factor , 5)

    for (r,y,w,h) in face:
        cv2.rectangle(pic , (x,y) , (x+w , y+h) , (255 , 255, 255) , 2 )
        font = cv2.FONT_HERSHEY_SIMPLEX
        size =0.5
        cv2.putText(img  ,'Shirley Setia' , (x,y) , font , size , (123 ,200 , 98) , 1 , cv2.LINE_AA)
    #print("no of faces found {} " .format(len(face)))
    cv2.imshow ('detect' , pic)
    k = cv2.waitKey(30) & 0xff 
    if k == 2 :
        break
cv2.destroyAllWindows()