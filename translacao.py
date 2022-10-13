import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("imagens/einstein.jpg", 0)

totalLinhas, totalColunas = img.shape
print(totalLinhas)
print(totalColunas)

# float32 recebe dois vetores de três valores [horizontal, vertical, quantidade de pixel referente ao deslocamento]
mat = np.float32([[1, 0, 100], [0, 1, 100]])
imgDeslocada = cv2.warpAffine(img, mat, (totalColunas, totalLinhas))

fig = plt.figure(figsize=(10 ,8))
plt.imshow(imgDeslocada, cmap=plt.cm.gray)
plt.show()