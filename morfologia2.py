import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("imagens/placa.png")

element_struct = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)) # Nosso elemento estruturante
# passando o tipo retangular do no elemento no tamanho 7x7 (Existem o de cruz e elíptico tb)
print(element_struct)

# FUNÇÃO erode(img, element_struct, interc)
img_process = cv2.erode(img, element_struct, iterations = 2) # interc = número de iterações

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(211)
plt.imshow(img)

ax2 = fig.add_subplot(212)
plt.imshow(img_process)
plt.show()

element_struct2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)) # Nosso elemento estruturante
print(element_struct2)

# FUNÇÂO dilate(img, elem_struct, interc)
img_dil = cv2.dilate(img, element_struct2, iterations = 2)

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(211)
plt.imshow(img)

ax2 = fig.add_subplot(212)
plt.imshow(img_dil)
plt.show()

# FUNÇÃO morphologyEx(img, oper, elem_struct) oper = operação a ser realizada
img1 = cv2.imread('imagens/moeda.png')
img2 = cv2.imread('imagens/esqueleto.tif')

fig = plt.figure(figsize=(15,15))

ax1 = fig.add_subplot(221)
plt.imshow(img1)
plt.title("Imagem original")

ax2 = fig.add_subplot(212)
plt.imshow(img2)
plt.title("Imagem original")

plt.show()

elem_struct1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
elem_struct2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21))

print(elem_struct1)
print(elem_struct2)

imgProc1 = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, elem_struct1)
imgProc2 = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, elem_struct2)
imgProc3 = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, elem_struct2)

fig = plt.figure(figsize=(15,15))

ax1 = fig.add_subplot(131)
plt.imshow(imgProc1)
plt.title("Gradiente Morfológico")

ax2 = fig.add_subplot(132)
plt.imshow(imgProc2)
plt.title("TOPHAT")

ax3 = fig.add_subplot(133)
plt.imshow(imgProc3)
plt.title("BLACKHAT")

plt.show()