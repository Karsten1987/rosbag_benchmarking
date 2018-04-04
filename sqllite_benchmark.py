#/usr/bin/env python3

import sqlite3
import threading

from benchmark_interface import BenchmarkInterface

class SQLliteBenchmark(BenchmarkInterface):

  __slots__ = [
      'lock',
      'conn',
      'cursor',
      'read_index',
  ]

  def __init__(self, database_file='sqlbenchmark.db', name='sqlite_benchmark'):
    BenchmarkInterface.__init__(self, name)
    self.lock = threading.Lock()
    self.conn = sqlite3.connect(database_file, check_same_thread=False)
    self.cursor = self.conn.cursor()
    sql = '''create table if not exists t_benchmark_data(
    k_id INTEGER PRIMARY KEY AUTOINCREMENT, f_data BLOB);'''
    self.cursor.execute(sql) # shortcut for conn.cursor().execute(sql)

  def __del__(self):
    self.conn.commit()
    self.conn.close()

  def write(self, binary_array):
    sql = '''INSERT INTO t_benchmark_data (f_data) VALUES (?);'''
    self.lock.acquire(True)
    self.cursor.execute(sql, (sqlite3.Binary(binary_array),))
    self.lock.release()

  def read(self):
    sql = '''SELECT * from t_benchmark_data'''
    self.cursor.execute(sql)
    self.read_index = 0

  def read_next(self):
    data = self.cursor[self.read_index]
    self.read_index += 1
    return data

  def read_single(self, i):
    sql = '''SELECT f_data FROM t_benchmark_data WHERE rowid = ?;'''
    self.cursor.execute(sql, (i,))
    return self.cursor.fetchone()
