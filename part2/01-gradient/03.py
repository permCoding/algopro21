# наложить один рисунок на другой
# должны поддерживать ARGB

from PIL import Image

img1 = Image.open("./mini/color.png")
img2 = Image.open("./mini/белка.png")

img3 = Image.blend(img1, img2, .9)

img3.show()
