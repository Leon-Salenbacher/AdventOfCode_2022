f = open("./1.day/input.txt", "r")

cur_elv = 0
max_elv_1 = 0
max_elv_2 = 0
max_elv_3 = 0
    

for l in f:
    if(len(l) == 1):
        if(max_elv_1 < cur_elv):
            max_elv_3 = max_elv_2
            max_elv_2 = max_elv_1
            max_elv_1 = cur_elv
        elif(max_elv_2 < cur_elv):
            max_elv_3 = max_elv_2
            max_elv_2 = cur_elv
        elif(max_elv_3 < cur_elv):
            max_elv_3 = cur_elv
        cur_elv = 0
    else:
        cur_elv += int(l)

if(max_elv_1 < cur_elv):
    max_elv_3 = max_elv_2
    max_elv_2 = max_elv_1
    max_elv_1 = cur_elv
elif(max_elv_2 < cur_elv):
    max_elv_3 = max_elv_2
    max_elv_2 = cur_elv
elif(max_elv_3 < cur_elv):
    max_elv_3 = cur_elv

total = max_elv_1 + max_elv_2 + max_elv_3

print("total: " + str(total))


