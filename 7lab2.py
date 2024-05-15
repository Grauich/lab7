from PIL import Image


def editimg(picture, editpicture):
    try:
        pict = Image.open(picture)
        # В 3 раза
        threeraza = pict.resize((pict.width // 3, pict.height // 3))
        threeraza.save(editpicture + "_3raza.jpg")
        # Горизонт
        horizont = pict.transpose(Image.FLIP_LEFT_RIGHT)
        horizont.save(editpicture + "_horizont.jpg")
        # Вертикаль
        vertical = pict.transpose(Image.FLIP_TOP_BOTTOM)
        vertical.save(editpicture + "_vertical.jpg")

    except FileNotFoundError:
        print("Ошибка")


picture = "kosh.jpg"
editpicture = "new"
editimg(picture, editpicture)
