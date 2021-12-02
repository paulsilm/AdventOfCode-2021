import helper

ns = helper.get_int_input_for_file("1")
sums = [x+y+z for x,y,z in zip(ns,ns[1:],ns[2:])]
cnt = [a < b for a,b in zip(sums, sums[1:])].count(True)
print(cnt)
