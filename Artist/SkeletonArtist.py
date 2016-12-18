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
                    inc = (incrementor)*i
                    inc2 = (1 - incrementor)*i
                    inc = max(inc, inc2)

                    draw.ellipse(
                        (vert.nub1X - circSize/2 + inc,
                         vert.nub1Y - circSize/2 - incrementor*i,
                         vert.nub1X + circSize + inc,
                         vert.nub1Y + circSize - incrementor*i),
                         fill = (255, 0, 255, 0))

                    draw.ellipse(
                        (vert.nub2X - circSize/2 - (1-incrementor)*i,
                         vert.nub2Y - circSize/2 + incrementor*i,
                         vert.nub2X + circSize - (1-incrementor)*i,
                         vert.nub2Y + circSize + incrementor*i),
                         fill = (255, 0, 255, 0))
            else:
                print onVert
                self.limbRoll(self._spine.nodes[onVert-1])


    def limbRoll(self, vert):
        if randint(0,10) == 5:
            print "limb"
            self.pasteLimbs(vert)

    def pasteLimbs(self, vert):
        thickness = (int(vert.size) - int(vert.size) % 2) / 2

        print vert.segLengths

        basePastePos = (
            int(vert.nub1X),
            int(vert.nub1Y)
        )
        previousBoneWidth = 0
        for seg in vert.segLengths:
            print "width", seg
            boneWidth = seg

            rotation = randint(0, 90)
            boneScene = self.drawBone(boneWidth, thickness)
            boneScene = boneScene.rotate(rotation, expand=True)

            pastePosition = (
                basePastePos[0] + previousBoneWidth,
                int(basePastePos[1] - boneScene.size[1] - thickness)
            )

            self._scene.paste(boneScene, pastePosition , boneScene)

            basePastePos = (
                basePastePos[0] + boneScene.size[0],
                basePastePos[1] - boneScene.size[1] - thickness
            )

    def drawBone(self, boneWidth, thickness):
        canvas = (boneWidth+thickness, int(thickness*1.75))
        boneScene = Image.new('RGBA', canvas, (255,100,100,0))
        draw = ImageDraw.Draw(boneScene)

        for capsX in [0, boneWidth]:
            draw.ellipse((0+capsX, 0, thickness+capsX, thickness), fill = (255,255,0,255))
            draw.ellipse((0+capsX, thickness*.75, thickness+capsX, thickness*.75 + thickness), fill = (255,255,0,255))
        draw.line(
            (thickness/2, thickness*.75, thickness/2+boneWidth, thickness*.75),
            fill = (255,255,0,255),
            width = thickness
        )

        return boneScene

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
