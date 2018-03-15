#/usr/bin/env python3

import sqlite3

from benchmark_interface import BenchmarkInterface

class SQLliteBenchmark(BenchmarkInterface):

  def __init__(self, database_file='sqlbenchmark.db'):
    BenchmarkInterface.__init__(self, 'sqlite_benchmark')
    self.conn = sqlite3.connect(database_file)
    self.cursor = self.conn.cursor()
    sql = '''create table if not exists t_benchmark_data(
    k_id INTEGER PRIMARY KEY AUTOINCREMENT, f_data BLOB);'''
    self.cursor.execute(sql) # shortcut for conn.cursor().execute(sql)

  def __del__(self):
    self.conn.commit()
    self.conn.close()

  def write(self, binary_array, data_size_type):
    sql = '''INSERT INTO t_benchmark_data (f_data) VALUES (?);'''
    self.cursor.execute(sql, (sqlite3.Binary(binary_array),))
