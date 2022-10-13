import cv2
import time # Útil na hora de ajustar a velocidade de exibição do vídeo

cap = cv2.VideoCapture('teste.mp4')

if cap.isOpened() == False:
    print("Erro ao abrir vídeo!")

while cap.isOpened():
    ret, frame = cap.read()
    # Fechando o video apertando q ou quando o vídeo acabar
    if ret == True:
        time.sleep(1/20) # Deixar o vídeo mais próximo da velocidade normal
        cv2.imshow('Frame', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

