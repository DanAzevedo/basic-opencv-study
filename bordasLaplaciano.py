import cv2
from matplotlib import pyplot as plt

img = cv2.imread("imagens/predio.jpg")

# FUNÇÃO Laplacian(img, var_arm) Bem melhor que o Sobel
lap = cv2.Laplacian(img, cv2.CV_8U)

fig = plt.figure(figsize=(15, 37.5))
ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem original")

ax2 = fig.add_subplot(122)
plt.imshow(lap)
plt.title("Operador Laplaciano")

plt.show()
