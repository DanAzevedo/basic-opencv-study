import cv2
import numpy as np
import matplotlib.pyplot as plt

# Criação da imagem 1 - Retângulo
img1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img1, (100, 100), (250, 250), 255, -1)

# Criação da imagem 2 - Círculo
img2 = np.zeros((300, 300), dtype="uint8")
cv2.circle(img2, (150, 150), 90, 225, -1)

# Plot da imagem
plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 1)
plt.imshow(img1, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.show()

# Operação AND - Pixels em comum entre as duas imagens ficarão aparecendo
rect_and_circle = cv2.bitwise_and(img1, img2)

plt.figure(figsize=(10, 8))
plt.imshow(rect_and_circle, cmap='gray')
plt.show()

# Operação OR - Pegando pixels de uma ou outra img
rect_or_circle = cv2.bitwise_or(img1, img2)

plt.figure(figsize=(10, 8))
plt.imshow(rect_or_circle, cmap='gray')
plt.show()

# Operação XOR - Pega o que for de uma img e outra em conjunto,
# e mostra o que tiver excludente de uma imagem em relação a outra
rect_xor_circle = cv2.bitwise_xor(img1, img2)

plt.figure(figsize=(10, 8))
plt.imshow(rect_xor_circle, cmap='gray')
plt.show()

# Operação NOT - Inverte os pixels, era branco e ficou preto
bit_not = cv2.bitwise_not(img1)

plt.figure(figsize=(10, 8))
plt.imshow(bit_not, cmap='gray')
plt.show()