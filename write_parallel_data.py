#/usr/bin/env python3

from benchmark_interface import *
from dummy_benchmark import DummyBenchmark
from sqllite_benchmark import SQLliteBenchmark

import time

class BenchmarkSuite(object):
  """ Benchmark suite class which takes various benchmarks to perform """

  __slots__ = [
      'benchmark',
      'data_gen',
  ]

  def __init__(self, benchmark):
    self.benchmark = benchmark
    self.data_gen = BigDataGenerator()

  def benchmark_write(self):
    start = time.time()

    for i in range(1000):
      self.benchmark.write(self.data_gen.generate(), self.data_gen.data_size_type)

    end = time.time()
    print('writing 1000 messages took', end-start)


if __name__ == "__main__":
  sql_benchmark = SQLliteBenchmark()

  suite = BenchmarkSuite(sql_benchmark)
  suite.benchmark_write()

