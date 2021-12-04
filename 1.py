import helper

def task1():
  ns = helper.get_int_input_for_file("1")
  cnt = [y > x for x,y in zip(ns,ns[1:])].count(True)
  print(cnt)

def task2():
  ns = helper.get_int_input_for_file("1")
  cnt = [y > x for x,y in zip(ns,ns[3:])].count(True)
  print(cnt)

if __name__ == '__main__':
  task1()
  task2()
