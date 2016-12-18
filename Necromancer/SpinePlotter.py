#!/usr/bin/python
import attr
import math
from Vertebra import Vertebra

"""
Plots vertebra in a spine
"""
@attr.s
class SpinePlotter(object):
    _startPoint = attr.ib()
    _endPoint = attr.ib()
    _curveRate = attr.ib()
    _vertSize = attr.ib()

    vertebrae = attr.ib(default = [])
    _spinalScale = attr.ib(default = 1)

    @property
    def nubSize(self):
        halfSize = self._vertSize/2 * self.spinalScale
        # forces even number rounding down
        halfSize = halfSize - (halfSize % 2)
        return halfSize

    @property
    def nodes(self):
        if self.vertebrae == []:
            self.generateNodes()

        return self.vertebrae

    @property
    def spinalScale(self):
        return self._spinalScale

    @property
    def localVertSize(self):
        scaledSize = self._vertSize * self.spinalScale
        # forces even number rounding down
        scaledSize = scaledSize - (scaledSize % 2)
        return scaledSize

    @spinalScale.setter
    def spinalScale(self, scale):
        self._spinalScale = scale

    def generateNodes(self):
        linePosition = self._startPoint
        lineEnd = self._endPoint

        while linePosition[0] < lineEnd[0]:
            position = float(linePosition[0] - self._startPoint[0])
            runway = float(lineEnd[0] - self._startPoint[0])
            distance = position/runway
            self.spinalScale = 1 - abs(distance - 0.5)

            curvedDistance = math.radians(distance*360*self._curveRate)
            sinOff = math.sin(curvedDistance) * 25
            cosOff = math.cos(curvedDistance) * 25

            linePosition = (linePosition[0]+1, linePosition[1]+1)

            if linePosition[0] % self._vertSize == 0:
                self.addVertebra(curvedDistance, sinOff, cosOff, linePosition)

        pass

    def addVertebra(self, curvedDistance, sinOff, cosOff, linePosition):
        x = linePosition[0] + sinOff
        y = linePosition[1] + (sinOff * -1)
        rawCurceAngle = math.cos(curvedDistance)
        nubXOffset = abs(rawCurceAngle - 1) * self.localVertSize/2


        vert = Vertebra(
            coordinates = (x, y),
            angle = rawCurceAngle,
            nubOffset = self.localVertSize/2 - self.nubSize/2,
            nubXOff = nubXOffset,
            nubYOff = nubXOffset - self.localVertSize/2 - self.nubSize,
            size = self.localVertSize,
            nubSize = self.nubSize,
            scale = self.spinalScale
        )

        self.vertebrae.append(vert)
