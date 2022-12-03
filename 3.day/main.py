def get_item_inBoth(rucksack):
    rucksack = list(rucksack)
    middle_index = len(rucksack)//2
    first_half = rucksack[:middle_index]
    second_half = rucksack[middle_index:]

    for i in first_half:
        for e in second_half:
            if(e == i):
                return i

    
def getPrio(listOfItems):
    listOfCharacter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    total_prio = 0

    for i in listOfItems:
        i = str(i)
        pointStarter = 1
        if(i.isupper()):
            pointStarter = 27
        
        i = i.lower()
        for l in listOfCharacter:
            if(l == i):
                total_prio += pointStarter
                break
            pointStarter+=1
            

    return total_prio

def find_group_attachement(first, second, third):
    for i in first:
        for e in second:
            for a in third:
                if(i == e and e == a):
                    return i





def part1():
    f = open("./3.day/input.txt", "r")
    list_ofDobleItems = []

    for l in f:
        list_ofDobleItems.append(get_item_inBoth(l))

    total_prio = getPrio(list_ofDobleItems)
    print(total_prio)

def part2():
    f = open("./3.day/input.txt", "r")
    
    index = 0
    first = []
    second = []
    third = []
    all_Attachemnts = []
    for l in f:
        # get 3 
        if(index == 0):
            first = list(l)
            index=1
        elif(index == 1):
            second = list(l)
            index=2
        elif(index == 2):
            third = list(l)
            all_Attachemnts.append(find_group_attachement(first, second, third))
            index = 0
    
    total_prio = getPrio(all_Attachemnts)
    print(total_prio)

if '__main__' == __name__:
    part2()