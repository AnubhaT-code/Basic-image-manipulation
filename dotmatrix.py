
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

c = { 0 : [ [1,1,1] , [1,0,1] , [1,0,1] , [1,0,1] , [1,1,1] ] , 1 : [ [0,0,1] , [0,0,1] , [0,0,1] , [0,0,1] , [0,0,1] ] , 2 : [ [1,1,1] , [0,0,1] , [1,1,1] , [1,0,0] , [1,1,1] ] , 3 : [ [1,1,1] , [0,0,1] , [1,1,1] , [0,0,1] , [1,1,1] ] , 4 : [ [1,0,1] , [1,0,1] , [1,1,1] , [0,0,1] , [0,0,1] ] , 5 : [ [1,1,1] , [1,0,0] , [1,1,1] , [0,0,1] , [1,1,1] ], 6 : [ [1,1,1] , [1,0,0] , [1,1,1] , [1,0,1] , [1,1,1] ], 7 : [ [1,1,1] , [0,0,1] , [0,0,1] , [0,0,1] , [0,0,1] ], 8 : [ [1,1,1] , [1,0,1] , [1,1,1] , [1,0,1] , [1,1,1] ] , 9 : [ [1,1,1] , [1,0,1] , [1,1,1] , [0,0,1] , [1,1,1] ]}

x = 50
n_input = sys.argv[1]
n = int(n_input)
radius = 25
w = 60
t = (n%10)*10 + (n//10)


image = np.zeros((300, 500, 3), dtype=np.uint8)
for i in range(0,2):
    d = c[t%10]
    for i in range(5):
        for j in range(3):
            if d[i][j] == 1:
                x_c = x+5+10*j+radius+2*radius*j
                y_c = 5+10*i+radius+2*radius*i
                centre = (x_c,y_c)
                color = (255,255,255)
                image = cv2.circle(image, centre , radius, color,-1)
    t = t//10
    x = x + 150 + w

#plt.imshow(image)


#print(image.size)


numpy_image = Image.fromarray(image)
numpy_image.save(".\dotmatrix.jpg")

# print(numpy_image.size) #(width, height)
# print(numpy_image.format)
# print(numpy_image.mode)




