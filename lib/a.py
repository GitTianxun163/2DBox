from PIL import Image

img = Image.open("icon.png").convert("RGBA")

for x in range(img.width):
	for y in range(img.height):
		pixel = img.getpixel((x,y))
		if (pixel == (0,0,0,255)):
			img.putpixel((x,y),(0,0,0,0))

img.save("r.png")