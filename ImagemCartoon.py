import cv2
from matplotlib import pyplot as plt

img = cv2.imread("imagens/por_sol.png")

plt.figure(figsize=(10, 8))
plt.imshow(img)
plt.show()

# Desfoque da imagem usando a função edgePreservingFilter
edgePreservingImage = cv2.edgePreservingFilter(img, flags=2, sigma_s=50, sigma_r=0.4)

plt.figure(figsize=(10, 8))
plt.imshow(edgePreservingImage)
plt.show()

# O filtro de estilização produz uma saída que parece que a imagem foi pintada com aquarela
# Interessante tratar com outros filtros antes (Threshold, Gaussian, etc.)
cartoon_image = cv2.stylization(img, sigma_s=150, sigma_r=0.25)

plt.figure(figsize=(10, 8))
plt.imshow(cartoon_image)
plt.show()