#!/usr/bin/python
import attr
from random import randint

"""
A segment of the spine
"""
@attr.s
class Vertebra(object):
    _coordinates = attr.ib()
    _angle = attr.ib()
    _nubOffset = attr.ib()
    _nubXOff = attr.ib()
    _nubYOff = attr.ib()
    _size = attr.ib()
    _nubSize = attr.ib()
    _scale = attr.ib()
    _hasLimbs = attr.ib(default=False)

    _limbSegments = 0
    _limbBrances = []
    _segLengths = []

    @property
    def x(self):
        return self._coordinates[0]

    @property
    def y(self):
        return self._coordinates[1]

    @property
    def segLengths(self):
        if self._segLengths == []:
            for i in range(1, self.limbSegments):
                self._segLengths.append(randint(10, 80))

        return self._segLengths

    @property
    def angle(self):
        return self._angle

    @property
    def size(self):
        return self._size

    @property
    def nubSize(self):
        return self._nubSize

    @property
    def scale(self):
        return self._scale

    @property
    def hasLimbs(self):
        return self._hasLimbs

    @property
    def limbSegments(self):
        if self._limbSegments == 0:
            self._limbSegments = randint(1, 5)

        return self._limbSegments
    # _limbBrances = []


    @property
    def nub1X(self):
        return self.x + self._nubOffset + self._nubXOff*.9

    @property
    def nub1Y(self):
        return self.y + self._nubOffset + self._nubYOff*.9

    @property
    def nub2X(self):
        return self.x + self._nubOffset - self._nubXOff*.9

    @property
    def nub2Y(self):
        return self.y + self._nubOffset - self._nubYOff*.9

    @property
    def slope(self):
        rise = (self.nub1Y - self.nub2Y) or 1
        run = (self.nub1X - self.nub2X) or 1
        return rise/run * -1
