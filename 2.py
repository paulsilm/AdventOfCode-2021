import helper

def task1():
  ls = helper.get_input_for_file("2")
  cmds = [(l[0],int(l[1])) for l in [l.split() for l in ls]]
  d = 0
  h = 0
  for cmd,i in cmds:
    if cmd == "forward":
      h += i
    elif cmd == "up":
      d -= i
    elif cmd == "down":
      d += i
  print (h*d)

def task2():
  ls = helper.get_input_for_file("2")
  cmds = [(l[0],int(l[1])) for l in [l.split() for l in ls]]
  d = 0
  h = 0
  aim = 0
  for cmd,i in cmds:
    if cmd == "forward":
      h += i
      d += aim*i
    elif cmd == "up":
      aim -= i
    elif cmd == "down":
      aim += i
  print (h*d)


if __name__ == '__main__':
  task1()
  task2()
