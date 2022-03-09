# повернуть рисунок

from PIL import Image

# img = Image.open("./images/color.jpg")
# img = img.rotate(45)
# img.show()

with Image.open("./images/color.jpg") as img:
    # img.rotate(180).show()

    new_img = img.rotate(222)

img.show()
new_img.show()
