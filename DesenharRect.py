import cv2

cap = cv2.VideoCapture(0)

# Callback Retângulo
def draw_rect(event, x, y, flags, params):
    global pt1, pt2, topLeftClicked, bottonRightClicked
    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeftClicked == True and bottonRightClicked == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeftClicked = False
            bottonRightClicked = False

        if topLeftClicked == False:
            pt1 = (x, y)
            topLeftClicked = True
        elif bottonRightClicked == False:
            pt2 = (x, y)
            bottonRightClicked = True

# Variáveis Globais
pt1 = (0, 0)
pt2 = (0, 0)
topLeftClicked = False
bottonRightClicked = False

cv2.namedWindow("Teste")
cv2.setMouseCallback('Teste', draw_rect)

while True:
    ret, frame = cap.read()
    # Desenhar o retângulo de acordo com as variáveis globais
    if topLeftClicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255))
    if topLeftClicked and bottonRightClicked:
        cv2.rectangle(frame, pt1, pt2, color=(0, 0, 255), thickness = 1)

    cv2.imshow('Teste', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

