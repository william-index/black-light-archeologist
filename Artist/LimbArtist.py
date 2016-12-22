#!/usr/bin/python
import attr
import operator
from random import randint
from PIL import Image, ImageDraw, ImageOps, ImageFont
# @TODO  creates and returns a canvas
# @TODO  Limbs are drawn positive for both axis
# @TODO  All limbs start exactly in top left
# @TODO  limbs have N segments
# @TODO  (p3) different segment bone types
# @TODO  each segment may branch to M other segments,
#           but only the "top" segments continue


# Taken from old method fo drawing bone


@attr.s
class LimbArtist(object):
    _canvas = attr.ib()


    def generateLimb(self, vert):
        limbScene = Image.new('RGBA', self._canvas, (0,0,0,0))
        print 'generating limb ...'

        segments = randint(1, 4)
        fingers = randint (1, 10)
        limbLength = randint(20, 60)

        previousBoneBBox = (10, 0)
        previousRotation = 0
        for seg in range(segments):
            # rotation start for bone
            rotation = randint(0, 90)

            # Draw Bones and rotate
            bone = self.drawBone(limbLength + randint(-15, 15), int(vert.size / 2))
            bone = bone.rotate(rotation * -1, expand=True)

            # Angled offset for joint formation
            rotationDiff = abs(previousRotation - rotation)
            jointOffset = (int(vert.size) * -1 * (1 - rotationDiff/90), int(vert.size) * (rotationDiff/90))
            previousBoneBBox = tuple(map(operator.add, previousBoneBBox, jointOffset))

            # Draw bone to scene
            limbScene.paste(bone, previousBoneBBox, bone)

            # updateRate of previous
            previousBoneBBox = tuple(map(operator.add, previousBoneBBox, bone.size))
            previousRotation = rotation

        return limbScene


    def drawBone(self, boneWidth, thickness):
        stroke = 2

        canvas = (boneWidth+thickness + stroke*2, int(thickness*2) + stroke*2)
        boneScene = Image.new('RGBA', canvas, (0,0,0,0))
        draw = ImageDraw.Draw(boneScene)

        # outline (yes I know copy paste twice is just sloppy here...)
        draw.line(
            (thickness/2, thickness*.75 + stroke, thickness/2+boneWidth, thickness*.75 + stroke),
            fill = (0,0,0,255),
            width = thickness + stroke*2)

        for capsX in [0, boneWidth]:
            draw.ellipse((0+capsX - stroke, 0 - stroke, thickness+capsX + stroke, thickness + stroke), fill = (0,0,0,255))
            draw.ellipse((0+capsX - stroke, thickness*.75 - stroke, thickness+capsX + stroke, thickness*.75 + thickness + stroke), fill = (0,0,0,255))

        # actual bone
        for capsX in [0, boneWidth]:
            draw.ellipse((0+capsX + stroke, stroke, thickness+capsX, thickness), fill = (255,255,0,255))
            draw.ellipse((0+capsX + stroke, thickness*.75 + stroke, thickness+capsX, thickness*.75 + thickness), fill = (255,255,0,255))

        draw.line(
            (thickness/2, thickness*.75 + stroke, thickness/2+boneWidth, thickness*.75 + stroke),
            fill = (255,255,0,255),
            width = thickness)

        return boneScene
