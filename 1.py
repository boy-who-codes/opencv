import numpy as np
import cv2

img = cv2.imread('213.png' )
font = cv2.FONT_HERSHEY_SIMPLEX
size =0.5
#thres_1 = 50
#thres_2 = 100
#can = cv2.Canny(img , thres_1 , thres_2)
cv2.putText(img  ,'Shirley Setia' , (20,300) , font , size , (123 ,200 , 98) , 1 , cv2.LINE_8)
cv2.rectangle(img , (20,30) , (280,280) , (123 , 200 , 98 ) , 3 , lineType=8 , shift=0)
cv2.imshow('Detection' , img )
cv2.waitKey(0)
cv2.destroyAllWindows()