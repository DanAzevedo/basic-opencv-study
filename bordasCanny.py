import cv2
from matplotlib import pyplot as plt

img = cv2.imread("imagens/predio.jpg")

# FUNÇÃO Canny(img, int_detc1, int_detc2) Intensidade de detecção 1 e 2 preto e branco
canny = cv2.Canny(img, 75, 50)

fig = plt.figure(figsize=(15, 37.5))
ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)
plt.title("Imagem original")

ax2 = fig.add_subplot(122)
plt.imshow(canny, cmap=plt.cm.gray)
plt.title("Operador Canny")

plt.show()