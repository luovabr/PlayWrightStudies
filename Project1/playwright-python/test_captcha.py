import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'  # your path may be different


img = cv2.imread(r'C:\Users\55119\Desktop\Estudos\UVT\playwright-python\captcha.png')

cv2.imshow('image', img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img_rgb))

cv2.waitKey(0) 

cv2.destroyAllWindows()