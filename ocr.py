import pytesseract
from PIL import Image
image = Image.open("./ocr_data/hello_world.jpg")
code = pytesseract.image_to_string(image)
print(code)

image = Image.open("./ocr_data/train_ch_tra.jpg")
code = pytesseract.image_to_string(image, lang='chi_tra')
print(code)