import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# # START HERE
img = cv2.imread('OCRtest2.jpg')
# # print(pytesseract.image_to_string(img))
# # # grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # # print(pytesseract.image_to_string(grayImg))

# Detecting Characters
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
adaptive = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 65, 43)

# text = pytesseract.image_to_string(img) changing original image to string
text = pytesseract.image_to_string(adaptive)

print(text)
cv2.imshow('adaptive', adaptive)
cv2.waitKey(0)
# import required modules:
