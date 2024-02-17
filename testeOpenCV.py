import cv2

img = cv2.imread('opencvlogo.png')

cv2.namedWindow('Janela')
cv2.imshow('Janela', img)
cv2.waitKey()
