file_path = "input_2.in"  # Replace with the actual file path

list1 = []
list2 = []
i = 0
j = 0
total = 0

with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split()

        list1.append(int(values[0]))
        list2.append(int(values[1]))
  
list1.sort()
list2.sort()

length = len(list1)

while i < length and j < length:
    while i < length and list1[i] < list2[j]:
        i += 1

    while j < length and list1[i] > list2[j]:
        j += 1

    if (i < length) and (j < length) and (list1[i] == list2[j]):
        cnt_1 = 0
        cnt_2 = 0
        val = list1[i]

        while i < length and list1[i] == val:
            cnt_1 += 1
            i += 1

        while j < length and list2[j] == val:
            cnt_2 += 1
            j += 1

        total += (cnt_1 * cnt_2 * val)
    

print(total)
