import cv2
from matplotlib import pyplot as plt

img = cv2.imread("imagens/head.png")

# FUNÇÃO medianBlur(img, intensidade) Melhor filtragem!
imgMed = cv2.medianBlur(img, 5)

fig = plt.figure(figsize=(15, 37.5))
ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(imgMed)
plt.show()
