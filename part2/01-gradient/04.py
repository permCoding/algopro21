# фигуры

from PIL import Image, ImageDraw

with Image.open("./images/white.jpg") as img:

    draw = ImageDraw.Draw(img)
    draw.line((0, 0) + img.size, fill=128)
    draw.line((0, img.size[1], img.size[0], 0), fill=128)

    clr = (255, 0, 0)

    draw.line(
        (img.size[0]//4, img.size[1]//2, 
        3*img.size[0]//4, img.size[1]//2), 
        clr,
        width=3
    )

    draw.ellipse(
        ((img.size[0]//4,5),
        (img.size[0]*3//4,img.size[1]//3)),
        outline=clr,
        fill=None,
        width=2
    )

    img.show()
    