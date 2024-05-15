from PIL import Image


def imageinfo(picture):
    try:
        pict = Image.open(picture)
        w, h = pict.size
        print("Размер {}x{}".format(w, h))
        format = pict.format
        print("Формат {}".format(format))
        color = pict.mode
        print("Цвет {}".format(color))
        pict.show()

    except FileNotFoundError:
        print("Ошибка")


picture = "kosh.jpg"
imageinfo(picture)
