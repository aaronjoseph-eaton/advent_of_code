file_path = "input_1.in"  # Replace with the actual file path

list1 = []
list2 = []
idx = 0
total = 0

with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split()

        list1.append(int(values[0]))
        list2.append(int(values[1]))
  
list1.sort()
list2.sort()

for i in range(len(list1)):
    total += abs(list1[i]-list2[i])



print(total)
