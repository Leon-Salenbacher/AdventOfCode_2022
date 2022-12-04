

def get_section_pair(line):
    [first, second] = str(line).split(",")
    if(second[-1] == "\n"):
        second = second[:-1]
    return [first, second]

def split_section(section):
    return str(section).split("-")

def get_range_of_section(section):
    [first, second] = split_section(section)

    range = []
    i = int(first)
    while i <= int(second):
        range.append(i)
        i+=1
    return range

def proof_full_containing_ranges(first, second):
    if(first[0] <= second[0] and first[len(first)-1] >= second[len(second)-1]):
        return True
    elif(second[0] <= first[0] and second[len(second)-1] >= first[len(first)-1]):
        return True
    return False

def proof_any_overlapping(first, second):
    for i in first:
        for e in second:
            if(i == e):
                return True
    return False


def part1():
    f = open("./4.day/input.txt", "r")
    counter = 0
    for l in f:
        [first_section, second_section] = get_section_pair(l)
        
        first_range = get_range_of_section(first_section)
        second_range = get_range_of_section(second_section)
        containing = proof_full_containing_ranges(
            first_range,
            second_range
        )
        if(containing):
            counter += 1
    print(counter)

def part2():
    f = open("./4.day/input.txt", "r")
    counter = 0
    for l in f:
        [first_section, second_section] = get_section_pair(l)
        
        first_range = get_range_of_section(first_section)
        second_range = get_range_of_section(second_section)
        containing = proof_any_overlapping(
            first_range,
            second_range
        )
        if(containing):
            counter += 1
    print(counter)

if '__main__' == __name__:
    part2()