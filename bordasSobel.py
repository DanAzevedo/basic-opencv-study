import cv2
from matplotlib import pyplot as plt

img = cv2.imread('imagens/predio.jpg')

# FUNÇÃO Sobel(img, var_arm, h, v, máscara) var_arm - valor que representa o pixel;
# h e v - realce na horizontal e vertical
# máscara - dimensão da máscara que será aplicada
sobelx = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=7)
sobely = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=7)

fig = plt.figure(figsize=(15, 37.5))
ax1 = fig.add_subplot(131)
plt.imshow(img)

ax2 = fig.add_subplot(132)
plt.imshow(sobelx)

ax3 = fig.add_subplot(133)
plt.imshow(sobely)

plt.show()