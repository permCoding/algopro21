# наложить один рисунок на другой
# должны поддерживать ARGB

from PIL import Image

img1 = Image.open("./images/color.png")
img2 = Image.open("./images/белка.png")

img3 = Image.blend(img1, img2, .5)

img3.show()
