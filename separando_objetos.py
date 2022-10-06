import cv2

img = cv2.imread('objetos.jpg')
img = cv2.resize(img, (600, 500))

imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#Como quero mapear objetos, vamos extrair os contornos da imagem
#1º parâmetro passamos a imagem alvo; 2º parâmetro passamos os valores de threshold para definirmos o que é e o que não é um contorno
#baseado em um limite de confiança min, max
imgCanny = cv2.Canny(imgCinza, 30, 200)
#Para melhorar a precisão  do algorítmo, vou aplicar a morfologia de Closing para termos um fechamento melhor em cada objeto
imgClose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (7, 7))
#Separar os contornos de cada objeto; Essa função irá retornar os dois valores que são os contornos e a hierarquia, porém, vamos
#trabalhar apenas com os contornos. Essa função captura os contornos da imagem; o parâmetro mode define qual a forma que o algoritmo irá
#procurar esses contornos Ex.: de dentro pra fora, por fora da imagem
#Nesse caso o melhor mode é o RETR_EXTERNAL e em seguida o método que faz a aproximação de contornos
contours, hierarchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#variável que vai servir para quando salvarmos o objeto, nós colocarmos o número no objeto
numOb = 1

for cnt in contours:
    #Desenha os contornos
    #cv2.drawContours(img, cnt, -1, (0, 0, 255), 2)
    #Coloca um retângulo ao redor do contorno onde retorna 4 valores: x, y, largura e altura que são coordenadas do
    #retângulo que vai ser formar em cada objeto
    x, y, w, h = cv2.boundingRect(cnt)
    #Vou recortar a imagem onde está o retângulo em cada objeto
    objeto = img[y:y+h, x:x+w]
    #Salvando cada imagem individual do objeto, nomeando e passando a variável objeto como parâmetro para salvar a img
    cv2.imwrite(f'objetos/objeto{numOb}.jpg', objeto)
    #Com os valores em mão, desenho o retângulo na imagem original onde a posição 1 será a inicial x e y
    #E ele vai até x+w e y+h, cor e expessura
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    numOb += 1

cv2.imshow('Imagem', img)
cv2.imshow('Imagem Cinza', imgCinza)
cv2.imshow('Imagem Canny', imgCanny)
cv2.waitKey(0)