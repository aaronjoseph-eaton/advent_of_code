import re

file_path = "input_1.in" 


total = 0

with open(file_path, "r") as file:

    db = file.readline()


    ranges = [r.strip() for r in db.strip().split(",")]
    result = []

    for range_str in ranges:
        left, right = map(int, range_str.split("-"))
        result.append([left, right])

    for rng in result:
#        print(str(rng[0]) + "   " + str(rng[1]))
        for i in range(rng[0], rng[1] + 1):
            s = str(i)
            
#            if re.fullmatch(r'(\d+)\1', s):    #### for part 1 [num sequence only repeated twice}`` ###
            if re.fullmatch(r'(\d+)\1+', s):
                total += int(s)


print(total)
