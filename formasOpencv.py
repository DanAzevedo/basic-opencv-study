import cv2

video = cv2.VideoCapture('imagens/runners.mp4')

while True:
    check, img = video.read()
    cv2.rectangle(img, (50, 50), (200, 200), (255, 0, 0), 5)
    cv2.circle(img, (300, 300), 50, (0, 0, 255), 5)
    cv2.line(img, (400, 400), (500, 300), (0, 255, 0), 2)
    texto = 'Piramides do Egito'
    cv2.putText(img, texto, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
    cv2.imshow('Imagem', img)
    cv2.waitKey(10)

img = cv2.imread('imagens/piramide.jpg')
#Cria um retângulo na imagem; O 1º parâmetro, é a imagem alvo, 2º início em pixels, 3º final em pixels, 4º cor, 5º expessura
cv2.rectangle(img, (50, 50), (200, 200), (255, 0, 0), 5)
#Cria um círculo na imagem; O 1º parâmetro, é a imagem alvo, 2º início em pixels, 3º raio, 4º cor, 5º expessura
cv2.circle(img, (300, 300), 50, (0, 0, 255), 5)
#Cria uma linha na imagem; O 1º parâmetro, é a imagem alvo, 2º início e o final em pixels, 3º cor, 4º expessura
cv2.line(img, (400, 400), (500, 300), (0, 255 ,0), 2)

texto = 'Piramides do Egito'
#Insere um  texto na imagem; 1º parâmetro é a imagem alvo; 2º parâmetro a variável que guardamos o texto;
# 3º parâmetro início e final em pixels, 4º parâmetro é a fonte; 4º parâmetro tamanho da fonte; 5º parâmetro cor e 6º expessura
cv2.putText(img, texto, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

cv2.imshow('Imagem', img)
cv2.waitKey(0)