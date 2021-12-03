import helper
import numpy as np

def task1():
  ns = helper.get_int_input_for_file("3")
  l = len(ns)
  binlist = np.array([toDigits(n) for n in ns])
  sums = binlist.transpose().sum(1).tolist()
  g = toInt([1 if a > (l // 2) else 0 for a in sums])
  h = toInt([1 if a < (l // 2) else 0 for a in sums])
  print(g*h)

def toDigits(d:int):
  return np.array([(d // 10**(11-i)) % 10 for i in range(12)])

def toInt(d):
  b:int = 0
  for i in range(12):
    b += (d[i])*2**(11-i)
  return b

if __name__ == '__main__':
  task1()