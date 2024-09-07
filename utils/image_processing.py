from PIL import Image
import pytesseract

def process_image(uploaded_image):
    img = Image.open(uploaded_image)
    text = pytesseract.image_to_string(img)
    return text
