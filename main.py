import math
from PIL import Image, ImageDraw, ImageOps, ImageFont

canvas = (300, 300)
interfacedScene = Image.new('RGB', canvas, (255,200,120))

pointA = (30, 30)
pointC = (260, 260)

pointB = (145,145)

draw = ImageDraw.Draw(interfacedScene)

lineStart = pointA
lineMid = pointB

# @TODO combine into one function
# @TODO allow curve to have 0 1 or 3 segments
# @TODO vary spacing and size
# @TODO represent as spinal nodes
move = 0
while lineStart[0] < lineMid[0]:
    move = move + 1
    position = float(lineStart[0] - pointA[0])
    runway = float(pointB[0] - pointA[0])
    distance = position/runway
    sinOff = math.sin(math.radians(distance*360/2)) * 25
    cosOff = math.cos(math.radians(distance*360/2)) * 25
    print(sinOff)
    lineStart = (lineStart[0]+1, lineStart[1]+1)
    if lineStart[0] % 10 == 0:
        draw.ellipse((lineStart[0] + sinOff,lineStart[1]+(sinOff*-1),lineStart[0]+10+sinOff,lineStart[1]+10+(sinOff*-1)), fill=(255,255,255,255))
        pass
    pass

lineStart = pointB
lineMid = pointC

move = 0
while lineStart[0] < lineMid[0]:
    move = move + 1
    position = float(lineStart[0] - pointA[0])
    runway = float(pointB[0] - pointA[0])
    distance = position/runway
    sinOff = math.sin(math.radians(distance*360/2)) * 25
    cosOff = math.cos(math.radians(distance*360/2)) * 25
    print(sinOff)
    lineStart = (lineStart[0]+1, lineStart[1]+1)
    if lineStart[0] % 10 == 0:
        draw.ellipse((lineStart[0] + sinOff,lineStart[1]+(sinOff*-1),lineStart[0]+10+sinOff,lineStart[1]+10+(sinOff*-1)), fill=(255,255,255,255))
        pass
    pass

interfacedScene.save('art/generated/foo.png')
