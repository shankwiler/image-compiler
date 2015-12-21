from PIL import Image, ImageColor
import sys

#open all given files, ignoring python files
imgs = [Image.open(n) for n in sys.argv if n[-3:] != ".py"]
wid = max([i.width for i in imgs]) # max width
hi = sum([i.height for i in imgs]) # total height
canvas = Image.new("RGB", (wid, hi), ImageColor.getrgb("white")) # add imgs on
addHi = 0 #height to add

for im in imgs:
    canvas.paste(im, (0, addHi)) # paste the imgs on top of each other
    addHi += im.height

canvas.save("compilation.png", "PNG")
