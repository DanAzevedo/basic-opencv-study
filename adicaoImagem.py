import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("imagens/Superman.png", 0)

img2 = cv2.imread("imagens/batman.png", 0)

imgsomada = cv2.add(img1, img2)

fig = plt.figure(figsize=(20, 5))
plt.imshow(imgsomada, cmap=plt.cm.gray)
plt.show()