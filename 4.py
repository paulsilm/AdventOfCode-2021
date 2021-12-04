import helper
import numpy as np

def task1():
  inp = helper.get_input_for_file("4")
  ns = [int(n) for n in inp[0].split(",")]
  boards = np.array([boardFromStrings(i, inp[2:]) for i in range(0,len(inp[2:]),6)])
  mask = boards == -1
  for n in ns:
    mask = mask | (boards == n)
    maskk = np.any(np.all(mask, axis=1) | np.all(mask, axis=2), axis = 1)
    if boards[maskk].size != 0:
      print (boards[maskk][~mask[maskk]].sum() * n)
      break

def task2():
  inp = helper.get_input_for_file("4")
  ns = [int(n) for n in inp[0].split(",")]
  boards = np.array([boardFromStrings(i, inp[2:]) for i in range(0,len(inp[2:]),6)])
  mask = boards == -1
  maskk = np.any(np.all(mask, axis=1) | np.all(mask, axis=2), axis = 1)
  for n in ns:
    maskkk = maskk.copy()
    mask = mask | (boards == n)
    maskk = np.any(np.all(mask, axis=1) | np.all(mask, axis=2), axis = 1)
    if np.count_nonzero(~maskk) == 0:
      print(boards[~maskkk][~mask[~maskkk]].sum() * n)
      break


def boardFromStrings(startIndex:int, inp):
  return np.array([np.array([int(n) for n in line.split()]) 
                    for line in inp[startIndex:startIndex+5]]
                  )

if __name__ == '__main__':
  task1()
  task2()
