#!/usr/bin/env python3

import os

class DataGenerator(object):

    __slots__ = [
        'name',
        'large_size',
        'mid_size',
        'small_size',
    ]

    def __init__(self, name='generic_data_gen', large_size=1 * 1024 * 1024, mid_size=1*1024, small_size=1):
      self.name = name
      self.large_size = large_size
      self.mid_size = mid_size
      self.small_size = small_size

    def generate_large_size(self):
        return bytearray(os.urandom(self.large_size))

    def generate_mid_size(self):
        return bytearray(os.urandom(self.mid_size))

    def generate_small_size(self):
        return bytearray(os.urandom(self.mid_size))
