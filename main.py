import math
from PIL import Image, ImageDraw, ImageOps, ImageFont
from Necromancer import SpinePlotter

# @TODO vary spacing and size

# Setup Base Canvas
canvas = (300, 300)
interfacedScene = Image.new('RGB', canvas, (255,200,120))

# Define spine geometry
pointA = (30, 30)
pointB = (260, 260)
curveRate = 1.5
vertSize = 10
nubSize = 4

# Create Spine
spine = SpinePlotter(
        startPoint = pointA,
        endPoint = pointB,
        curveRate = curveRate,
        vertSize = vertSize,
        nubSize = nubSize)

# Draw Skeleton
draw = ImageDraw.Draw(interfacedScene)

for vert in spine.nodes:
    draw.ellipse(
        (vert.x,
         vert.y,
         vert.x + vert.size,
         vert.y + vert.size),
         fill=(255,255,255,255))


    draw.ellipse(
        (vert.nub1X,
         vert.nub1Y,
         vert.nub1X + vert.nubSize,
         vert.nub1Y + vert.nubSize),
         fill=(255,0,0,255))


    draw.ellipse(
        (vert.nub2X,
         vert.nub2Y,
         vert.nub2X + vert.nubSize,
         vert.nub2Y + vert.nubSize),
         fill=(0,0,255,255))



interfacedScene.save('art/generated/foo.png')
