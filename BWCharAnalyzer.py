from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import collections
import sys

resultDict = {}
scale = 10
f = ImageFont.truetype(font=sys.argv[1], size=40*scale)


def makeImg(char):
	img = Image.new('1', (24*scale, 49*scale), color=1)
	d = ImageDraw.Draw(img)
	d.text((0, 0), char, font=f)
	return img

for chrC in range(32, 127):
	char = chr(chrC)
	
	img = makeImg(char)
	
	sum = 0.0
	for p in img.getdata():
		if p==0:
			sum += 1.0
		
	val = sum/(24*scale*49*scale)
	if val in resultDict.keys():
		val += 1.0/(24*scale*49*scale)

	resultDict[val] = char

sortedVals = sorted(resultDict.keys())

stdLetters = []
for key in sortedVals:
	stdLetters.append(resultDict[key])

sys.stdout = open("CharacterBrightnessSequence", "w")

for letter in stdLetters:
	sys.stdout.write(letter)
	sys.stdout.write(chr(0x001F))
#print(strOutput)