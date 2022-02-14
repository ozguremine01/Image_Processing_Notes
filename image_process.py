import cv2 as cv
print(cv.__version__)
import numpy as np

a= cv.imread('C:/Users/Pc/Desktop/dene1.jpg',0)
image=cv.resize(a, (300,300))
print("Derinlik",image.shape)
cv.imshow('Resim', a)
edge= cv.Canny(image,100,200)
cv.imshow('Resim', edge)
cv.waitKey(0)
cv.destroyAllWindows()
laplace= cv.Laplacian(image, cv.CV_64F)
cv.imshow('Resim', laplace)
cv.waitKey(0)
cv.destroyAllWindows()
#Blurring
kernel_3x3= np.ones((3,3), np.float32) /9
output= cv.filter2D(image, -1, kernel_3x3)
output2=cv.blur(image, (5,5))
cv.imshow('Resim', output2)
cv.waitKey(0)
cv.destroyAllWindows()
#Erosion
erosion = cv.erode(image,kernel_3x3,iterations = 1)
cv.imshow('Resim', erosion)
cv.waitKey(0)
cv.destroyAllWindows()
#Dilation
dilation = cv.dilate(image,kernel_3x3,iterations = 1)
cv.imshow('Resim', dilation)
cv.waitKey(0)
cv.destroyAllWindows()
#Median Filter
median_filter= cv.medianBlur(image, ksize=7)
cv.imshow('Resim', median_filter)
cv.waitKey(0)
cv.destroyAllWindows()

scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dsize = (width, height)
dene = cv.resize(image, dsize)
cv.imwrite('C:/Users/Pc/Desktop/cicek1.jpg',dene)

laplace= cv.Laplacian(image, cv.CV_64F)
cv.imshow('Resim', laplace)
cv.waitKey(0)
cv.destroyAllWindows()

canny= cv.Canny(image, 100,200)
cv.imshow('Resim', canny)
cv.waitKey(0)
cv.destroyAllWindows()

sobel_horizontal = cv.Sobel(a, cv.CV_64F, 1, 0, ksize=3)
sobel_vertical = cv.Sobel(a, cv.CV_64F, 0, 1, ksize=3)
cv.imshow('sobel', sobel_horizontal)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow('sobel', sobel_vertical)
cv.waitKey(0)
cv.destroyAllWindows()

sobel= cv.hconcat([sobel_horizontal,sobel_vertical])
cv.imshow('Sobel',sobel)
cv.waitKey(0)
cv.destroyAllWindows()

from matplotlib import pyplot as plt

plt.subplot(1, 2, 1), plt.imshow(sobel_horizontal,cmap='gray')
plt.subplot(1, 2, 2), plt.imshow(sobel_vertical,cmap= 'gray')
plt.show()
sobel_vertical_1=cv.copyMakeBorder(a,10,10,10,10, cv.BORDER_CONSTANT,value=[255,255,255])
sobel_horizontal_1=cv.copyMakeBorder(a,10,10,10,10, cv.BORDER_CONSTANT,value=[255,255,255])
sobel= cv.hconcat([sobel_horizontal_1,sobel_vertical_1])
cv.imshow('Sobel',sobel)
cv.waitKey(0)
cv.destroyAllWindows()
import numpy as np
final = np.concatenate((sobel_horizontal_1, sobel_vertical_1), axis = 1)
cv.imshow('final', final)
cv.waitKey(0)
cv.destroyAllWindows()
ret,thresh1 = cv.threshold(a,127,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh1)
cv.waitKey(0)
cv.destroyAllWindows()
plt.hist(image.ravel(),256,[0,256])
plt.show()

histogram= cv.equalizeHist(a)
plt.hist(histogram.ravel(),256,[0,256])
plt.show()

#https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html
image1= cv.imread('C:/Users/Pc/Desktop/cicek.jpg')

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([image1],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

image1= cv.cvtColor(image1, cv.COLOR_RGB2GRAY)
cv.imshow('gri',image1)
cv.waitKey(0)
cv.destroyAllWindows()

ret,thresh1 = cv.threshold(image,127,255,cv.THRESH_BINARY)
dilation = cv.dilate(thresh1,kernel_3x3,iterations = 1)

cv.imshow('dilation', dilation)
cv.waitKey(0)
cv.destroyAllWindows()


matrix = np.ones(image.shape, dtype = "uint8") * 75

added = cv.add(image, matrix)
cv.imshow("Added", added)
cv.waitKey(0)
cv.destroyAllWindows()

from skimage.measure import compare_ssim
#keskinleştirme

sharpen=np.array(np.ones((3,3),np.float32)*(-1))
output_1 = cv.filter2D(image1, -1, sharpen)
cv.imshow("Added", output_1)
cv.waitKey(0)
cv.destroyAllWindows()


