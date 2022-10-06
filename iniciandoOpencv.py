import cv2

#Cortar uma imagem utilizando o openCV para identificar as dimensões e salvar o arquivo
#img = cv2.imread('farol.jpg')
#dim = cv2.selectROI('Selecione a área de recorte', img, False)
#Fechar a janela após extrair as coordenadas
#cv2.destroyWindow('Selecione a área de recorte')
#v1 = int(dim[0])
#v2 = int(dim[1])
#v3 = int(dim[2])
#v4 = int(dim[3])
#
#recorte = img[v2:v2+v4, v1:v1+v3]
#
#Salvar a imagem recortada
#caminho = ''
#nome_arquivo = input('Digite o nome do arquivo: ')
#
#cv2.imwrite(f'{caminho}{nome_arquivo}.jpg', recorte)
#print('Imagem salva com sucesso!')
#
##cv2.imshow('Imagem', img)
##cv2.imshow('Recorte', recorte)
#
#cv2.waitKey(0)


#Cortar uma imagem utilizando o paint
#img = cv2.imread('farol.jpg')
#print(img.shape)
#Verificando as dimensões pelo paint
#y 310-520
#x 120-420
#recorte = img[310:520, 120:420]
#print(recorte.shape)
#cv2.imshow('Imagem', img)
#cv2.imshow('Recorte', recorte)
#
#cv2.waitKey(0)


#Para se trabalhar com WebCam, caso tenha a mesma integrada, usa-se o índice 0, fora isso fazer testes até achar a correta
#camera = cv2.VideoCapture(1)
#Setar configurações para melhorar a imagem
#camera.set(3, 640)#3 - seta a largura
#camera.set(4, 420)#4 - seta a altura
#camera.set(10, 200)#seta o brilho/luminosidade

#while True:
#     #Estabelcemso duas variáveis para abrir a câmera, porém só utilizamos a img
     #check, img = camera.read()
#
     #cv2.imshow('WebCam', img)
     #A função waitKey vai esperar uma chave que é a letra q para fechar
     #if cv2.waitKey(1) & 0xFF == ord('q'):
      #    break


#Abrindo um vídeo e reproduzindo
#video = cv2.VideoCapture('runners.mp4')
#Uma imagem é um conjunto de fotos, por isso precisamos rodar a mesma em loop infinito
#while True:
#     check, img = video.read()
#     #Redimensionar o vídeo
#     imgRedim = cv2.resize(img, (640, 420))
#     cv2.imshow('Video', imgRedim)
#     cv2.waitKey(10)


#Abrindo uma imagem colorida
#img = cv2.imread('farol.jpg')
#Abrindo uma imagem em escala de cinza
#imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#
#print(imgCinza)
#Mostrando imagens
#cv2.imshow('Imagem', img)
#cv2.imshow('Imagem Cinza', imgCinza)
#Para fixar a janela na tela
#cv2.waitKey(0)