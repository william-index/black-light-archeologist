import math
from PIL import Image, ImageDraw, ImageOps, ImageFont
from Necromancer import SpinePlotter

# @TODO vary spacing and size

# Setup Base Canvas
canvas = (300, 300)
interfacedScene = Image.new('RGB', canvas, (255,200,120))

# Define spine geometro
pointA = (30, 30)
pointB = (260, 260)
curveRate = 3.5

# Create Spine
spine = SpinePlotter(
        startPoint = pointA,
        endPoint = pointB,
        curveRate = curveRate)

# Draw Skeleton
draw = ImageDraw.Draw(interfacedScene)

for vert in spine.nodes:
    draw.ellipse(
        (vert.x,
         vert.y,
         vert.x + 10,
         vert.y + 10),
         fill=(255,255,255,255))

interfacedScene.save('art/generated/foo.png')
