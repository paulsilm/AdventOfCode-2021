import helper

ns = helper.get_int_input_for_file("1")
cnt = [y > x for x,y in zip(ns,ns[1:])].count(True)
print(cnt)
