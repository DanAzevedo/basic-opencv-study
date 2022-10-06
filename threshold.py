import cv2

img = cv2.imread('imagens/img022.jpg')
#Diminuindo a resolução
img = cv2.resize(img, (700, 800))
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Variável que vai receber a imagem binarizada. Para utilizar a função threshold do opencv, preciso criar duas imagens
#ou simplesmente colocar um _ representando a primeira e um nome para a segunda (th1)
#1º parâmetro a imagem alvo; 2º o valor de threshold que defini quando um pixel vai assumir a cor preta ou branca. Esse valor
# corresponde a intensidade. >127 = cor preta; <127 = cor branca;
# 3º valor máximo de intensidade de um pixel que é 255 (padrão)
#4º o tipo de threshhold
_,th1 = cv2.threshold(imgCinza, 127, 255, cv2.THRESH_BINARY)
#Caso a imagem tenha sombra, teremos um problema e para corrigir isso, precisamos utilizar um threshold adaptativo
#1º parâmetro é a imagem alvo; 2º valor de intensidade máxima do ; 3º parâmetro é o tipo de adaptação que a img vai receber
#4º parâmetro é o método de threshold; 5º blocksize que são config que terão efeitos sobre a imagem
th2 = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 16)

th3 = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 16)

#cv2.imshow('ORIGINAL', img)
cv2.imshow('TH1', th1)
cv2.imshow('TH2', th2)
cv2.imshow('TH3', th3)

cv2.waitKey(0)
