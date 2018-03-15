#/usr/bin/env python3

from benchmark_interface import BenchmarkInterface

class DummyBenchmark(BenchmarkInterface):
    """ dummy class benchmark instance """

    def __init__(self, name):
      BenchmarkInterface.__init__(self, name)

    def write(self, data):
      print('[%s]: writing data' % self.name)

    def read(self):
      print('[%s]: reading data' % self.name)
      return 0
