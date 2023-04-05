import cv2
import numpy as np
import time

# Programmer : Mohammad Shirvani
# Date 1402/01/16


row=320
coulmn=500

cap=cv2.VideoCapture(0)
while True:
	ret, frame= cap.read()

	if ret:

		frame=cv2.flip(frame,1)
		frame=cv2.resize(frame,(coulmn,row))
		
		img1=frame.copy()
		img2=frame.copy()
		img2[:,:,2]=255

		img3=np.concatenate([img1,img2],1)

		img4=255-frame
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		gray1=gray.reshape(row,coulmn,1)
		img5=np.concatenate([gray1,gray1,gray1],2)

		img6=np.concatenate([img4,img5],1)

		img7=np.concatenate([img3,img6],0)

		cv2.putText(img7,"Mohammad Shirvani",(200,50),
			cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),5)
	
		cv2.imshow("webcamasdfasdf",img7)
		q=cv2.waitKey(1)
		if q==ord('q'):
			break
cv2.destroyAllWindows()
cap.release()

		