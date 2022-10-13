import cv2

cap = cv2.VideoCapture(0)

# Altura e Largura
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Salvar um vídeo (Nome do vídeo, tipo de codec, taxa de frame entre 20-30 e H e W da img
writer = cv2.VideoWriter('teste.mp4', cv2.VideoWriter_fourcc(*'DVIX'), 20, (width, height))

# Laço de repetição
while True:
    ret, frame = cap.read()
    cv2.imshow('Frame', frame)
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Acabar com a captação de imagens
writer.release()
cv2.destroyAllWindows()
