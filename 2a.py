import helper

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
