import math
from PIL import Image, ImageDraw, ImageOps, ImageFont
from Necromancer import SpinePlotter
from Artist import SkeletonArtist

# @TODO vary spacing and size

# Setup Base Canvas
canvas = (300, 300)
scene = Image.new('RGB', canvas, (0,0,0,0))

# Define spine geometry
pointA = (30, 30)
pointB = (260, 260)
curveRate = 1
vertSize = 10

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
