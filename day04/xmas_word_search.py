


file_path = "input_4_1.in"  # Replace with the actual file path

total = 0
matrix = []

with open(file_path, "r") as file:
    for line in file:
       matrix.append(line)


rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "X":
            for k in range(j - 1, j + 2):
                for l in range(i - 1, i + 2):
                    
