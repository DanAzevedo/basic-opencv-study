import cv2
from matplotlib import pyplot as plt

img = cv2.imread('imagens\einstein1.png.')

# FUNÇÃO blur(img, máscara) onde máscara é a dimensão da máscara que será aplicada.
imgM = cv2.blur(img, (5, 5))

fig = plt.figure(figsize=(15, 37.5))
ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem com ruído")

ax2 = fig.add_subplot(122)
plt.imshow(imgM)
plt.title("Imagem filtrada")
plt.show()