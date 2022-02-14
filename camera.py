#Kameradan görüntü almak için
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Kamera bağlantısı başarısız!")
    exit()
 
while True:
    ret, frame = cap.read()
    if not ret:
        print("Bağlantıdan görüntü alınamadı!")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

#Kameradan alınan görüntüleri video olarak kaydetme
cap = cv.VideoCapture(0)
filename='C:/Users/Pc/Desktop/video_deneme.mp4'
codec= cv.VideoWriter_fourcc(*'MP4V')
out = cv.VideoWriter(filename,codec, 40.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv.flip(frame,1)
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()

