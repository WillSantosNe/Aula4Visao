import cv2
import numpy as np

placas = [
    "pare.jpeg", 
    "placa.jpeg",
    "placa2.jpeg", 
    "placa3.jpeg", 
    "placa4.jpeg"
]

for placa in placas:
    imagem = cv2.imread(placa)
    if imagem is None:
        print(f"Erro ao carregar {placa}. Verifique o caminho do arquivo.")
        continue

    imagem = cv2.resize(imagem, (640, 480))

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

    bordas = cv2.Canny(imagem_suavizada, 100, 200)
    imagem_combinada = np.hstack((imagem, cv2.cvtColor(bordas, cv2.COLOR_GRAY2BGR)))
    
    cv2.imwrite("saida_" + placa, imagem_combinada)
    
    cv2.imshow(f"Placa: {placa}", imagem_combinada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
