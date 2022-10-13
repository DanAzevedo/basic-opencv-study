import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagens/einstein.jpg', 0)

totalLinhas, totalColunas = img.shape
print(totalLinhas)
print(totalColunas)

mat = cv2.getRotationMatrix2D((totalLinhas / 2, totalColunas / 2), 45, 1)

imgRotacionada = cv2.warpAffine(img, mat, (totalColunas, totalLinhas))

fig = plt.figure(figsize=(10, 8))
plt.imshow(imgRotacionada, cmap=plt.cm.gray)
plt.show()
