from PIL import Image, ImageFilter
import os


def fitlimg(picture):
    img = Image.open(picture)
    filtimg = img.filter(ImageFilter.EMBOSS)
    return filtimg


def main():
    papka = "7lab3picture"
    papkanew = "7lab3pictureNEW"
    os.makedirs(papkanew, exist_ok=True)

    for filename in os.listdir(papka):
        if filename.endswith(".jpg"):
            inputimg = os.path.join(papka, filename)
            outputimg = os.path.join(papkanew, f"{filename[:-4]}_new.jpg")
            filtimgsave = fitlimg(inputimg)
            filtimgsave.save(outputimg)


main()
