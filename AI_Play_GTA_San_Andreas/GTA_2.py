  
import numpy as np
from PIL import ImageGrab
import cv2
import time
from time import sleep
from key import *


def key_press():
	for i in list(range(5))[::-1]:
		print(i+1)
		time.sleep(2)
		
# f = 'CVWKXAM'
# for i in range(len(f)):
# 	PressKey(f[i])
# 	sleep(1)
# 	ReleaseKey(f[i])

	PressKey(L)
	sleep(1)
	ReleaseKey(L)
	PressKey(X)
	sleep(1)
	ReleaseKey(X)
	PressKey(G)
	sleep(1)
	ReleaseKey(G)
	PressKey(I)
	sleep(1)
	ReleaseKey(I)
	PressKey(W)
	sleep(1)
	ReleaseKey(W)
	PressKey(Y)
	sleep(1)
	ReleaseKey(Y)
	PressKey(L)
	sleep(1)
	ReleaseKey(L)

def screen_record(): 
    last_time = time.time()
    while(True):
       
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,640,480)))
        Edge = proc_img(printscreen)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

key_press()
