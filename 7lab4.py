from PIL import Image
import os

current_directory = os.getcwd()
save_directory = os.path.join(current_directory, "7lab4watermark")
save_path = os.path.join(save_directory, "imagwatermark.png")

def addwatermark(image: Image.Image):
    try:
        with Image.open("watermark.png") as watermark:
            resized_watermark = watermark.resize(
                size=(int(image.width / 5), int(image.height / 5))
            )
            resized_watermark = resized_watermark.convert("RGBA")
            image.paste(resized_watermark, (0, 0), resized_watermark)
        
    except FileNotFoundError:
        print("Ошибка знака:")

def watermarkimg(picture):
    try:
        with Image.open(picture) as image:
            addwatermark(image)
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            image.save(save_path)

    except FileNotFoundError:
        print("Ошибка изображения:")

picture = "kosh.jpg"
watermarkimg(picture)
