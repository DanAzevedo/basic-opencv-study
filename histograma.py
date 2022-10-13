'''
O histograma de uma imagem é a distribuição de frequÊncia dos níveis de cinza
em relação ao número de amostras. Essa distribuição nos fornece informações
sobre a qualidade da imagem, principalmente no que diz respeito à intensidade
luminosa e contraste.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('imagens/Cinza.jpg')

# plt.imshow(img)
# plt.show()
'''
A função histograma precisa de 3 parâmetros:
    - Entrada:
        1. Img = Imagem com a qual queremos trabalhar.
        2. Num1 = Número de elementos distintos que podem ser representados.
        3. Intervalo = Intervalo entre os elementos.
    - Saída: Gráfico representadno o histograma da imagem.   
    
A função ravel:
    - Entrada:
        1. Img = Matriz de entrada, no caso a imagem. Os elementos em um são lidos na ordem
        especificada por ordem e empacotados como uma matriz.
    - Saída: Retorna uma matriz plana contígua (matriz 1D com todos os elementos da matriz
    de entrada e com o mesmo tipo que ela).        
'''
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
'''
- Histogramas de imagens coloridas
    Uma imagem colorida possui um histograma para cada canal de cor. Uma vez que cada canal é
    representado por pixels em tons de cinza, o mesmo método estudado no tópico anterior pode ser implementado
    para mostrar os histograma de imagens coloridas.
'''
img = cv2.imread('imagens/colorida.jpg')
# Fazer o split da imagem para cada canal de cor que a imagem colorida possui RGB
b, g, r = cv2.split(img)

fig = plt.figure(figsize=(20, 5))

ax1 = fig.add_subplot(131)
ax1.hist(b.ravel(), 256, [0, 256])
plt.title('Histograma do canal azul')

ax2 = fig.add_subplot(132)
ax2.hist(g.ravel(), 256, [0, 256])
plt.title('Histograma do canal verde')

ax3 = fig.add_subplot(133)
ax3.hist(r.ravel(), 256, [0, 256])
plt.title('Histograma do canal vermelho')

plt.show()

'''
Histograma de imagens em tons de cinza e coloridas.
'''




