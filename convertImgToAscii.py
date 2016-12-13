import sys
from PIL import Image

f = open(sys.argv[1], "r")
chrs = f.read().split(chr(0x001F))
f.close()

print(type(sys.argv[3]))
scale = float(sys.argv[3])

img = Image.open(sys.argv[2])
img = img.resize((int(img.size[0]*scale), int(img.size[1]*scale*(24.0/49.0))))

ascImg = []

def brightnessToAscii(brtns):
	frac = float(brtns)/255.0
	fracPerChar = 1.0/float(len(chrs))
	val = (frac/fracPerChar)
	
	
	chrIndex = int(round(val, 0))
	return chrs[len(chrs)-chrIndex-1]

pixels = list(img.getdata())
for y in range(img.size[1]):
	for x in range(img.size[0]):
		index = y*img.size[0]+x
		
		char = brightnessToAscii(pixels[index])
		ascImg.append(char)
	ascImg.append("\n")

ascStr = ""
for char in ascImg:
	ascStr += char

f = open("outputText", "w")
f.write(ascStr)
f.close()