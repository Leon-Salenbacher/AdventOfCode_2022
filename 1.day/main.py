f = open("./1.day/input.txt", "r")

cur_elv = 0
max_elv_1 = 0
max_elv_2 = 0
max_elv_3 = 0
    
def proof(m1, m2, m3, cur):
    if(m1 < cur):
        m3 = m2
        m2 = m1
        m1 = cur
    elif(m2 < cur):
        m3 = m2
        m2 = cur
    elif(m3 < cur):
        m3 = cur
    return [m1, m2, m3]

for l in f:
    if(len(l) == 1):
        [max_elv_1, max_elv_2, max_elv_3] = proof(max_elv_1, max_elv_2, max_elv_3, cur_elv)
        cur_elv = 0
    else:
        cur_elv += int(l)

[max_elv_1, max_elv_2, max_elv_3] = proof(max_elv_1, max_elv_2, max_elv_3, cur_elv)
total = max_elv_1 + max_elv_2 + max_elv_3

print("total: " + str(total))


