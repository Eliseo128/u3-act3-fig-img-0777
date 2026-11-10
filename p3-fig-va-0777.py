import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Eliseo Nava NC 0777
print("Eliseo Nava Nc 0777")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
mi_iagen = cv2.imread('JohnLennon.jpg')
plt.imshow(mi_iagen)
plt.title('John Lennon y Eliseo Nava 0777')
plt.show()
print("+-+-+-  Puntos en la imagen +-+-+-+")
plt.imshow(mi_iagen)
x = [100,100,300,340]
y = [100,400,500,300]
plt.scatter(x, y, s=20,c='red')
plt.show()
