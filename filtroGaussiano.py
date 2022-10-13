import cv2
from matplotlib import pyplot as plt

img = cv2.imread('imagens/formas.png')

# FUNÇÃO GaussianBlur(img, máscara, suavização) onde máscara é a
# dimensão da máscara que será aplicada e depois o Grau de suavização.
imgGauss = cv2.GaussianBlur(img, (5 ,5), 0)

fig = plt.figure(figsize=(15, 37.5))
ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(imgGauss)
plt.show()
