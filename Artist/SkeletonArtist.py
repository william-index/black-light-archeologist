#!/usr/bin/python
import attr
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
        pass

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
