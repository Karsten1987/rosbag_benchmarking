#/usr/bin/env python3

import os

class BigDataGenerator(object):

    __slots__ = [
            'data_size_type',
    ]

    def __init__(self):
        self.data_size_type = 2

    def generate(self):
        return bytearray(os.urandom(3 * 1024 * 1024))

class BenchmarkInterface(object):
    """ Base class for every benchmark app """

    __slots__ = [
            'name',
    ]

    def __init__(self, name):
        self.name = name

    def write(self, binary_data, data_size_type):
        """ data is treated as a character array """

        raise NotImplementedError('write function not implemented in base class')

    def read(self):
        raise NotImplementedError('read function not implemented in base class')
