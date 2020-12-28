import cv2
import time

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

init_time = time.time()
counter_timeout = init_time+1
counter = 1
fileno=1

while(capture.isOpened()):
 ret, frame = capture.read()

 if ret==True:
  if (time.time() > counter_timeout):
   print(counter)#time clock
   counter+=1
   counter_timeout+=1

   if(counter%1==0):
    cv2.imwrite("Jaeyeong6-%d.png" % fileno, frame)     # save frame as JPEG file
    fileno+=1

  cv2.imshow('frame', frame)
  if cv2.waitKey(10) == 27:   #esc   
   break

 else:
  break
    # Release everything if job is finished
capture.release()
cv2.destroyAllWindows()