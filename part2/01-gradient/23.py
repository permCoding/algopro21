from PIL import Image, ImageFont, ImageDraw

img = Image.open("./images/color.jpg")

draw = ImageDraw.Draw(img)

# use a bitmap font
# font = ImageFont.load("arial.pil")

# draw.text((10, 10), "hello", font=font)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 15)

draw.text((10, 25), "world", font=font)

img.show()
