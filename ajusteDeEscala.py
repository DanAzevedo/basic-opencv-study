import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("imagens/einstein.jpg", 0)

imgModificada = cv2.resize(img,
                           None,
                           fx=0.8,
                           fy=0.8,
                           interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original", img)
cv2.imshow("Modificada", imgModificada)
cv2.waitKey(0)
cv2.destroyAllWindows()