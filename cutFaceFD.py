import cv2

imagePath = 'people.jpg'

img = cv2.imread(imagePath)
print(img.shape)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)

face_classifier = cv2.CascadeClassifier( cv2.data.haarcascades + "haarcascade_frontalface_default.xml" )
face = face_classifier.detectMultiScale( gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40) )

# recortar as faces identificadas
i=0
for (x, y, w, h) in face:
    imgCut = img[y:y+h,x:x+w]
    fileName = 'cut' + str(i) + '.jpg'
    cv2.imwrite(fileName, imgCut)
    print('Write in file ' + fileName)
    i+=1

# desenha um retângulo nas imagens detectadas
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imwrite('people2.jpg', img_rgb)
