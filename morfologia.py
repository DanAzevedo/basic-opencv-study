import cv2

img = cv2.imread('imagens/piramide.jpg')
img = cv2.resize(img, (500,400))
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgCinza, (7,7),0)#Borrar a imagem
imgCanny = cv2.Canny(img, 50,100)#Destacar os contornos de uma imagem
imgDilate = cv2.dilate(imgCanny, (5,5), iterations=5)#Dilatamos a imagem. O processo expande todas as linhas e todos os pontos dessa imagem
imgErode = cv2.erode(imgCanny, (5,5), iterations=2)#Tende a criar uma erosão na imagem, ou sejam desfragmentar os objetos ao contrário do dilate
imgOpening = cv2.morphologyEx(imgCanny, cv2.MORPH_OPEN, (5, 5))#Há uma redução nos detalhes, na quantidade de ruídos tentando ao máximo limpar a imagem
imgClosing = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (5, 5))#O inverso do Open, tentamos ao máximo fechar a imagem

#cv2.imshow('Img original', img)
#cv2.imshow('Img Cinza', imgCinza)
#cv2.imshow('Img Blur', imgBlur)
cv2.imshow('Img Canny', imgCanny)
#cv2.imshow('Img Dilate', imgDilate)
#cv2.imshow('Img Erode', imgErode)
cv2.imshow('Img Open', imgOpening)
cv2.imshow('Img Close', imgClosing)


cv2.waitKey(0)

