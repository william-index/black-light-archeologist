#!/usr/bin/python
import attr
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
        self.drawRibs(color)
        self.drawSpine(color)
        pass

    def drawRibs(self, color):
        print len(self._spine.nodes)
        draw = ImageDraw.Draw(self._scene)
        fullSize = randint(50, 150)

        startRib = randint(4, len(self._spine.nodes))
        endRib = randint(startRib, len(self._spine.nodes))

        onVert = 0
        onRib = 0
        arcLength = 50 + randint(0, 40)

        for vert in self._spine.nodes:
            if onVert > startRib and onVert < endRib:
                onRib = onRib + 1

                ribSizeMod =  1.0 - abs(((float(onRib) / float(endRib - startRib)) - 0.5) * 2)
                size = fullSize * ribSizeMod

                netVertOffset = (vert.angle + 1)/2
                xShift = (1 - netVertOffset) * size/2
                yShift =  netVertOffset * size/2

                lineStart = (vert.nub1X - xShift + vert.nubSize*2 * (1 - netVertOffset), vert.nub1Y - yShift)
                lineEnd = (lineStart[0] + size, lineStart[1] + size)

                lineStart = (lineStart[0] + vert.size/2, lineStart[1])

                altRibLineStart = (vert.nub2X - xShift - vert.nubSize*2 * netVertOffset, vert.nub2Y - yShift)
                altRibLineEnd = (altRibLineStart[0] + size - vert.nubSize*2, altRibLineStart[1] + size + vert.nubSize*2)

                altRibLineStart = (altRibLineStart[0] + vert.size/2, altRibLineStart[1])

                startArc = 270 - (arcLength * netVertOffset)
                endArc = startArc + arcLength

                for i in range(3):
                    # lineStart = (lineStart[0]+i, lineStart[1]+1)
                    draw.arc(
                        [lineStart, lineEnd],
                        startArc,
                        endArc,
                        (0, 255, 0))

                    # altRibLineStart = (altRibLineStart[0] + 1*(netVertOffset), altRibLineStart[1] + 1*netVertOffset)
                    draw.arc(
                        [altRibLineStart, altRibLineEnd],
                        startArc - arcLength,
                        startArc,
                        (0, 255, 0))

            onVert = onVert + 1

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
