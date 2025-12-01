import re

file_path = "input_3_1.in" 
total = 0

with open(file_path, "r") as file:

    line = ""
    
    for l in file:
        line += l

    sects = line.split("do")

    for g in sects:
        


        if g[:3] != "n't":
            print(g)
            valid_sets = re.findall("mul[(][0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?[)]", g)
    
            for s in valid_sets:
                print(s)
                vals = s[4:-1].split(",")
                total += int(vals[0]) * int(vals[1])


print(total)

