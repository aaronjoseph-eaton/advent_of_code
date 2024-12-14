file_path = "input_1.in"  # Replace with the actual file path

total = 0

with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split()
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

        if safe == True:
            total += 1

    print(total)


        


