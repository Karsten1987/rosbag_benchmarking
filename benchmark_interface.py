#!/usr/bin/env python3

class BenchmarkInterface(object):
    """ Base class for every benchmark app """

    __slots__ = [
            'name',
    ]

    def __init__(self, name):
        self.name = name

    def write(self, binary_data):
        """ data is treated as a character array """

        raise NotImplementedError('write function not implemented in base class')

    def read(self):
        raise NotImplementedError('read function not implemented in base class')
