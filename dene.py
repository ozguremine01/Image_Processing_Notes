import cv2 
import numpy as np
import imageio
import matplotlib.pyplot as plt
import matplotlib.colors
import pymssql
from os import getenv
import colorsys
img_file='C:\\Users\\Pc\\Desktop\\implant_resimler\\Anew.jpg'
img=cv2.imread(img_file)
print(img.shape)
y=format(img.shape[0])
x=format(img.shape[1])
img1=cv2.imread(img_file)
ret, bw_img = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary Image",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img2=imageio.imread('C:\\Users\\Pc\\Desktop\\resim\\cv_resmi1.jpg')
print(format(img2.shape))
print('red:{}'.format(img2[460,353,0]))
img2r=format(img2[460,353,0])
img2g=format(img2[460,353,1])
img2b=format(img2[460,353,2])
print('green:{}' .format(img2[460,353,1]))
print('blue:{}'.format(img2[460,353,2]))
img4=imageio.imread(img_file)
img4r=img4[199,89,0]
img4g=img4[199,89,1]
img4b=img4[199,89,2]
print('red:{}'.format(img4r))
print('green:{}'.format(img4g))
print('blue:{}'.format(img4b))
img3=imageio.imread('C:\\Users\\Pc\\Desktop\\resim\\cv_resmi1.jpg')
print(format(img3.shape))
img3r=format(img3[199,89,0])
img3g=format(img3[199,89,1])
img3b=format(img3[199,89,2])
print('red:{}'.format(img3[199,89,0]))
print('green:{}' .format(img3[199,89,1]))
print('blue:{}'.format(img3[199,89,2]))
a=199
img3r1=img3[a,89,0]
img3g1=img3[199,89,1]
img3b1=img3[199,89,2]
img2r1=img2[199,89,0]
img2g1=img2[199,89,1]
img2b1=img2[199,89,2]
diff=0
for x in range(0,img2.shape[0]):
    x=x+1
    if(img2.shape[0]<=x):
        continue
    for y in range(0,img3.shape[1]):
            diff=(diff+(img2r1-img3r1))/255
            diff=(diff+(img2g1-img3g1))/255
            diff=(diff+(img2b1-img3b1))/255
            y=y+1
sonuc=100* diff /(img2.shape[1] * img3.shape[0] * 3)
print(sonuc)   
print(colorsys.rgb_to_hsv(img4r,img4g,img4b))
img_file1='C:\\Users\\Pc\\Desktop\\implant_resimler\\Ankylos.jpg'
img5=imageio.imread(img_file1)
print('red:{}'.format(img5[199,89,0]))
print('green:{}' .format(img5[199,89,1]))
print('blue:{}'.format(img5[199,89,2]))
print(format(img5.shape[0]))
print(format(img5.shape[1]))
img_file2='C:\\Users\\Pc\\Desktop\\implant_resimler\\Ankylos-7-x-11.jpg'
img6=imageio.imread(img_file2)
print('red:{}'.format(img6[199,89,0]))
print('green:{}' .format(img6[199,89,1]))
print('blue:{}'.format(img6[199,89,2]))
print(format(img6.shape[0]))
print(format(img6.shape[1]))
img_file3='C:\\Users\\Pc\\Desktop\\implant_resimler\\Ankylos-5.5-x-9.5.jpg'
img7=imageio.imread(img_file3)
print('red:{}'.format(img7[199,89,0]))
print('green:{}' .format(img7[199,89,1]))
print('blue:{}'.format(img7[199,89,2]))
print(format(img7.shape[0]))
print(format(img7.shape[1]))
img_file4='C:\\Users\\Pc\\Desktop\\implant_resimler\\Ankylos-5.5-x-9.5.jpg'
img8=imageio.imread(img_file4)
print('red:{}'.format(img8[199,89,0]))
print('green:{}' .format(img8[199,89,1]))
print('blue:{}'.format(img8[199,89,2]))
print(format(img8.shape[0]))
print(format(img8.shape[1]))
img_file5='C:\\Users\\Pc\\Desktop\\implant_resimler\\Ankylos-7-x-11.jpg'
img9=imageio.imread(img_file5)
print('red:{}'.format(img9[199,89,0]))
print('green:{}' .format(img9[199,89,1]))
print('blue:{}'.format(img9[199,89,2]))
print(format(img9.shape[0]))
print(format(img9.shape[1]))
import os
yol=os.listdir("C:\\Users\\Pc\\Desktop\\implant_resimler")
resim_yol=[]
for i,k in enumerate(yol):
    resim_yol.append(k)
    print(i+1,k)
print(resim_yol)
print(resim_yol[0])
for a in range(0,108):   
    print(resim_yol[a])
def mesaj():
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
from tkinter import *
import tkinter
window=Tk()
window.title("Benzerlik Oranı Karşılaştırma")
listekutu=Listbox(window,width=50)
for a in range(0,108):   
    listekutu.insert(END ,resim_yol[a])
listekutu.pack()
btn= Button(window, text='emineee',command=mesaj)
btn.pack()

mainloop()










