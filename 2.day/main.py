def get_points(you, opponent):
    points = 0
    if(you == "Y"):
        points += 2
        if(opponent == "B"):
            points += 3
        elif(opponent == "A"):
            points += 6
    elif(you == "X"):
        points += 1
        if(opponent == "A"):
            points += 3
        elif(opponent == "C"):
            points += 6
    elif(you == "Z"):
        points += 3
        if(opponent == "C"):
            points += 3
        elif(opponent == "B"):
            points += 6
    return points

if '__main__' == __name__:
    f = open("./2.day/input.txt", "r")
    total_points = 0
    for l in f:
        [opponent, you] = l.split(" ") 
        if(you[-1] == "\n"):
            you = you[:-1]

        total_points += get_points(you, opponent)
        
    print(total_points)
