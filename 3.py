import helper
import numpy as np
from statistics import multimode

def task1():
  ns = helper.get_int_input_for_file("3")
  l = len(ns)
  binlist = np.array([toDigits(n) for n in ns])
  sums = binlist.transpose().sum(1).tolist()
  g = toInt([1 if a > (l // 2) else 0 for a in sums])
  h = toInt([1 if a < (l // 2) else 0 for a in sums])
  print(g*h)

def task2():
  ns = helper.get_int_input_for_file("3")
  binmatrix = np.array([toDigits(n) for n in ns])
  o2Rating = calculateRating(binmatrix.copy())
  co2Rating = calculateRating(binmatrix.copy(), 1)
  print(o2Rating*co2Rating)

# overengineered function
def calculateRating(matrix, thing=0):
  for i in range(12):
    temp = matrix[:,i]
    # if cnt(1) == cnt(0): m = 1
    m = sorted(multimode(temp), reverse=True)[0]
    if thing: # reverse value for co2Rating
      m = 1 - m
    matrix = matrix[temp == m] # filter stuff
    if len(matrix) == 1:
      return toInt(matrix[0])

def toDigits(d:int):
  return np.array([(d // 10**(11-i)) % 10 for i in range(12)])

def toInt(d):
  b:int = 0
  for i in range(12):
    b += (d[i])*2**(11-i)
  return b

if __name__ == '__main__':
  task1()
  task2()