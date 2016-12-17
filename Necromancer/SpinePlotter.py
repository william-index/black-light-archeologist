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

    vertebrae = attr.ib(default = [])

    @property
    def nodes(self):
        if self.vertebrae == []:
            self.generateNodes()

        return self.vertebrae

    def generateNodes(self):
        linePosition = self._startPoint
        lineEnd = self._endPoint
        move = 0

        while linePosition[0] < lineEnd[0]:
            move = move + 1

            position = float(linePosition[0] - self._startPoint[0])
            runway = float(lineEnd[0] - self._startPoint[0])
            distance = position/runway

            curvedDistance = math.radians(distance*360*self._curveRate)
            sinOff = math.sin(curvedDistance) * 25
            cosOff = math.cos(curvedDistance) * 25

            linePosition = (linePosition[0]+1, linePosition[1]+1)

            if linePosition[0] % 10 == 0:
                x = linePosition[0] + sinOff
                y = linePosition[1] + (sinOff * -1)

                vert = Vertebra(
                    coordinates = (x, y),
                    angle = 0)

                self.vertebrae.append(vert)

        pass
