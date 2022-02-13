from PIL import Image, ImageFilter

with Image.open("./images/белка.jpg") as img:
    img_blurred = img.filter(filter=ImageFilter.BLUR).show()
    