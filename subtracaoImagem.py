import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("imagens/Superman.png", 0)

img2 = cv2.imread("imagens/batman.png", 0)

fig = plt.figure(figsize=(20, 5))
ax1 = fig.add_subplot(121)
plt.imshow(img1, cmap=plt.cm.gray)

ax2 = fig.add_subplot(122)
plt.imshow(img2, cmap=plt.cm.gray)

imgsub = cv2.subtract(img1, img2)
fig = plt.figure(figsize=(20, 5))
plt.imshow(imgsub, cmap=plt.cm.gray)
plt.show()

