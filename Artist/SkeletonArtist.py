#!/usr/bin/python
import attr
import math
from random import randint
from PIL import Image, ImageDraw, ImageOps, ImageFont
from LimbArtist import LimbArtist

"""
A segment of the spine
# @TODO adbstract to methods for spine, limbs, ribs and skull
# @TODO: limbs
#        limbs can be drawn as their own artist class and then added
#        to nodes in the spine, the counter limb can be a double flip of the original
# @TODO: ribs
#        a single rib can be drawn and rotated with a counter rib
# @TODO: skull generation
"""
@attr.s
class SkeletonArtist(object):
    _scene = attr.ib()
    _spine = attr.ib()

    def drawSkeleton(self, color):
        self.plotSpine(color)
        pass


    def plotSpine(self, color):
        firstVert = True
        for vert in self._spine.nodes:
            self.drawVertebra(vert, color)

            if firstVert:
                print "skull"
                firstVert = False

            if vert.hasLimbs and not firstVert:
                self.addLimbs(vert)



    def addLimbs(self, vert):
        limbArtist = LimbArtist(self._scene.size)
        limb = limbArtist.generateLimb(vert)

        limbRight = limb.rotate(90, expand=True)
        rightJoint = (int(vert.x + vert.size/2), int(vert.y - limbRight.size[1] - vert.size/2))
        self._scene.paste(limbRight, rightJoint, limbRight)

        limbLeft = limb.transpose(Image.FLIP_LEFT_RIGHT)
        leftJoint = (int(vert.x - limbLeft.size[0] - vert.size/2), int(vert.y + vert.size/2))
        self._scene.paste(limbLeft, leftJoint, limbLeft)

    # @TODO abstract to a segment ploting artist
    def drawVertebra(self, vert, color):
        draw = ImageDraw.Draw(self._scene)
        stroke = 2

        for strokeMod in [stroke, 0]:
            fillColor = color if strokeMod == 0 else (0,0,0,255)
            draw.ellipse(
                (vert.x - strokeMod,
                 vert.y - strokeMod,
                 vert.x + vert.size + strokeMod,
                 vert.y + vert.size + strokeMod),
                 fill = fillColor)

            draw.ellipse(
                (vert.nub1X - strokeMod,
                 vert.nub1Y - strokeMod,
                 vert.nub1X + vert.nubSize + strokeMod,
                 vert.nub1Y + vert.nubSize + strokeMod),
                 fill = fillColor)

            draw.ellipse(
                (vert.nub2X - strokeMod,
                 vert.nub2Y - strokeMod,
                 vert.nub2X + vert.nubSize + strokeMod,
                 vert.nub2Y + vert.nubSize + strokeMod),
                 fill = fillColor)
