from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import collections
import sys
import json
from pprint import pprint
from math import sqrt

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

f = open("CharacterBrightnessSequence", "w")

for letter in stdLetters:
	f.write(letter)
	f.write(chr(0x001F))

# print(resultDict)

adjustedMap = {}
for i in range(0, 256):
    closestKey = min(resultDict.keys(),
            key=lambda x: abs(((float(x) ** .3) * 255) - i))

    adjustedMap[i] = resultDict[closestKey]

json.dump(adjustedMap, open('./charBrightness.json', 'w'))
