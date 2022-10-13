import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("imagens/Superman.png", 0)

img2 = cv2.imread("imagens/batman.png", 0)

imgTotal = cv2.addWeighted(img1, 0.8, img2, 1, 0)
fig = plt.figure(figsize=(20, 5))
plt.imshow(imgTotal, cmap=plt.cm.gray)
plt.show()
