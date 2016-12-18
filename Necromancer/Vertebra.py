#!/usr/bin/python
import attr

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

    @property
    def x(self):
        return self._coordinates[0]

    @property
    def y(self):
        return self._coordinates[1]

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
    def nub1X(self):
        return self.x + self._nubOffset + self._nubXOff

    @property
    def nub1Y(self):
        return self.y + self._nubOffset + self._nubYOff

    @property
    def nub2X(self):
        return self.x + self._nubOffset - self._nubXOff

    @property
    def nub2Y(self):
        return self.y + self._nubOffset - self._nubYOff

    @property
    def slope(self):
        rise = (self.nub1Y - self.nub2Y)
        run = (self.nub1X - self.nub2X)
        return rise/run * -1
