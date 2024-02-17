import matplotlib.pyplot as plt
import cv2

imagem = cv2.imread("versa1.jpeg")

plt.figure(figsize=(20,10))
plt.imshow(imagem)
plt.title("Placa Mercosul")
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(20,10))
plt.imshow(imagem_gray, cmap="gray")
plt.title("Placa Mercosul Escala de Cinza")

imagem_suavizada = cv2.blur(imagem_gray, (13,13))
plt.figure(figsize=(20,10))
plt.imshow(imagem_suavizada, cmap="gray")


_, imagem_limiarizada = cv2.threshold(imagem_suavizada, 120, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(20,10))
plt.imshow(imagem_limiarizada, cmap="gray")

imagem_contornos = imagem.copy()
lista_roi = []

contornos, _ = cv2.findContours( imagem_limiarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Contornos encontrados: " + str(len(contornos)))
razao_placa = 40/13

for contorno in contornos:
    (x, y, w, h) = cv2.boundingRect(contorno)
    
    area = int(w) * int(h)
    print("area=" + str(area))

    if area > 40000:
        razao_cont = w/h
        
        if razao_cont >= (razao_placa - 0.10*razao_placa) and razao_cont <= (razao_placa + 0.10*razao_placa):
            cv2.rectangle(imagem_contornos, (x,y), (x+w, y+h), (0,255,0), 2)
            lista_roi.append(contorno)

plt.figure(figsize=(20,10))
plt.imshow(imagem_contornos)

print("Placas identificadas: " + str(len(lista_roi)))

for item in lista_roi:
    (x, y, w, h) = cv2.boundingRect(item)
    roi = imagem[y:y+h, x:x+w]
    
    plt.figure(figsize=(10,5))
    plt.imshow(roi)
    
    cv2.imwrite("roi.png", roi)
