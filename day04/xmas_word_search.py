


file_path = "input_4_1.in"  # Replace with the actual file path

total = 0
matrix = []
word = "XMAS"

with open(file_path, "r") as file:
    for line in file:
       matrix.append(line)


rows = len(matrix)
cols = len(matrix[0]) - 1

# print("Rows: ", rows)
# print("Cols: ", cols)

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "X":
            for k in range(-1 , 2):
                for l in range(-1, 2):
                    for m in range(0, 4):
                        if (i + k*m) >= 0 and (i + k*m) < rows and (j + l*m) >= 0 and (j + l*m) < cols:
                            
                            if matrix[i + k*m][j + l*m] == word[m]:
                                if m == 3:
                                    # print("i: ", i, " j: ", j, " k: ", k, " l: ", l, " m: ", m, " word: ", word, " matrix: ", matrix[i + k*m][j + l*m])
                                    total += 1
                            else:
                                break

print(total)                    
