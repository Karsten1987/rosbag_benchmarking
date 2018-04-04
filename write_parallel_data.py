#!/usr/bin/env python3

from benchmark_interface import *
from data_generator import DataGenerator
from dummy_benchmark import DummyBenchmark
from image_generator import ImageGenerator
from sqllite_benchmark import SQLliteBenchmark

import time
import threading

class Benchmark(threading.Thread):
    __slots__ = [
        'benchmark',
        'generator',
        'name',
    ]

    def __init__(self, benchmark, generator, name):
        threading.Thread.__init__(self)
        self.benchmark = benchmark
        self.generator = generator
        self.name = name

    def run(self):
        start = time.time()

        n = 1000
        for i in range(n):
          self.benchmark.write(self.generator.generate_large_size())

        end = time.time()
        print('[%s] writing %d messages took %f seconds' % (self.name, n, end-start))


class BenchmarkSuite(object):
  """ Benchmark suite class which takes various benchmarks to perform """

  __slots__ = [
      'benchmark_threads',
  ]

  def __init__(self, benchmarks, data_generators=[]):
      self.benchmark_threads = []
      for benchmark in benchmarks:
          for data_gen in data_generators:
              self.benchmark_threads.append(Benchmark(benchmark, data_gen, str(benchmark.name + data_gen.name)))

  def start_benchmark(self):
      for benchmark in self.benchmark_threads:
          benchmark.start()

      for benchmark in self.benchmark_threads:
          benchmark.join()

if __name__ == "__main__":
  sql_benchmark = SQLliteBenchmark()

  data_gen = DataGenerator()
  image_gen = ImageGenerator('/lhome/kaknese/Downloads/WiegelesHeliSki_DivXPlus_19Mbps.mkv')

  # suite = BenchmarkSuite([sql_benchmark], [data_gen, image_gen])
  # suite = BenchmarkSuite([sql_benchmark], [data_gen])
  # suite = BenchmarkSuite([sql_benchmark], [image_gen])
  # suite.start_benchmark()

  #sql_benchmark.read()
  #data = sql_benchmark.read_next()
  data = sql_benchmark.read_single(1)
  image_gen.show_image_from_bytearray(data)

