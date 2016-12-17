#!/usr/bin/python
import attr

"""
A segment of the spine
"""
@attr.s
class Vertebra(object):
    _coordinates = attr.ib()
    _angle = attr.ib()

    @property
    def x(self):
        return self._coordinates[0]

    @property
    def y(self):
        return self._coordinates[1]
