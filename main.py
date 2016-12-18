import math
from random import randint
from PIL import Image, ImageDraw, ImageOps, ImageFont

from Necromancer import SpinePlotter
from Artist import SkeletonArtist

# @TODO vary spacing and size

# Setup Base Canvas
canvas = (400, 400)
scene = Image.new('RGB', canvas, (0,0,0,0))

# Define spine geometry
pointA = (90, 90)
pointB = (290, 290)
curveRate = ((randint(1, 100)/100.0) * 1.7) + 0.3
vertSize = randint(3, 13)


# Create Spine
spine = SpinePlotter(
        startPoint = pointA,
        endPoint = pointB,
        curveRate = curveRate,
        vertSize = vertSize)

skeletonArtist = SkeletonArtist(
                 scene = scene,
                 spine = spine)
# Draw Skeleton
skeletonArtist.drawSkeleton(color = (255, 0, 0))


scene.save('art/generated/foo.png')
