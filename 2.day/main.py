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

def get_your_move(opponent, expected_outcom):
    move = ""
    if(excepted_outcome == "X"):
        if(opponent == "A"):
            move = "Z"
        elif(opponent == "B"):
            move = "X"
        elif(opponent == "C"):
            move = "Y"

    elif(excepted_outcome == "Y"):
        if(opponent == "A"):
            move = "X"
        elif(opponent == "B"):
            move = "Y"
        elif(opponent == "C"):
            move = "Z"
    elif(excepted_outcome == "Z"):
        if(opponent == "A"):
            move = "Y"
        elif(opponent == "B"):
            move = "Z"
        elif(opponent == "C"):
            move = "X"
    return move

if '__main__' == __name__:
    f = open("./2.day/input.txt", "r")
    total_points = 0
    for l in f:
        [opponent, excepted_outcome] = l.split(" ") 
        if(excepted_outcome[-1] == "\n"):
            excepted_outcome = excepted_outcome[:-1]

        you = get_your_move(opponent, excepted_outcome)
        total_points += get_points(you, opponent)
        
    print(total_points)



"""
You:
Rock     -> X -> 1
Paper    -> Y -> 2
Scissors -> Z -> 3

Opponent
Rock     -> A 
Paper    -> B
Scissors -> C

"""