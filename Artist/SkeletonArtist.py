#!/usr/bin/python
import attr
import math
from random import randint
from PIL import Image, ImageDraw, ImageOps, ImageFont

"""
A segment of the spine
"""
@attr.s
class SkeletonArtist(object):
    _scene = attr.ib()
    _spine = attr.ib()

    def drawSkeleton(self, color):
        self.drawSpine(color)
        self.drawRibs(color)
        pass

    def drawRibs(self, color):
        draw = ImageDraw.Draw(self._scene)

        onVert = 0
        startVert = randint(1, len(self._spine.nodes))
        endVert = randint(startVert, len(self._spine.nodes))

        for vert in self._spine.nodes:
            onVert = onVert + 1
            incrementor = math.atan(vert.slope)
            circSize = vert.size/2

            if onVert > startVert and onVert < endVert:
                for i in range(50):
                    circSize = circSize - 0.1
                    draw.ellipse(
                        (vert.nub1X - circSize + (1-incrementor)*i,
                         vert.nub1Y - circSize - incrementor*i,
                         vert.nub1X + circSize + (1-incrementor)*i,
                         vert.nub1Y + circSize - incrementor*i),
                         fill = (255, 0, 255, 0))

                    draw.ellipse(
                        (vert.nub2X - circSize - (1-incrementor)*i,
                         vert.nub2Y - circSize + incrementor*i,
                         vert.nub2X + circSize - (1-incrementor)*i,
                         vert.nub2Y + circSize + incrementor*i),
                         fill = (255, 0, 255, 0))

    def drawSpine(self, color):
        draw = ImageDraw.Draw(self._scene)

        for vert in self._spine.nodes:
            draw.ellipse(
                (vert.x,
                 vert.y,
                 vert.x + vert.size,
                 vert.y + vert.size),
                 fill = color)


            draw.ellipse(
                (vert.nub1X,
                 vert.nub1Y,
                 vert.nub1X + vert.nubSize,
                 vert.nub1Y + vert.nubSize),
                 fill = color)


            draw.ellipse(
                (vert.nub2X,
                 vert.nub2Y,
                 vert.nub2X + vert.nubSize,
                 vert.nub2Y + vert.nubSize),
                 fill = color)
