file_path = "input.txt"  # Replace with the actual file path

total = 0

def isSafe(values):
    length = len(values)

    if(int(values[0]) < int(values[1])):
        low = 1
        high = 3
    else:
        low = -3
        high = -1

    safe = True

    for i in range(length - 1):
            if(int(values[i+1]) < (int(values[i]) + low)) or (int(values[i+1]) > (int(values[i]) + high)):
                safe = False
                break

    return safe



with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split()
        length = len(values)

        safe = isSafe(values)

        if safe == True:
            total += 1

        else:
            for i in range(length):
                vals2 = values.copy()
                vals2.pop(i)
                safe = isSafe(vals2)
                if safe == True:
                    total += 1
                    break

    print(total)


        


