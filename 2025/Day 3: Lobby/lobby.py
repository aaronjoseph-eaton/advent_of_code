file_path = "input_1.in" 


total = 0

with open(file_path, "r") as file:

    for bank in file:
        bank = bank.strip()

        digits = 12
        idx = 0
        sz = len(bank)

        s = ""


        for i in range(12, 0, -1):

            d = int(bank[idx])

            for j in range(idx, (sz - i + 1)):
                if int(bank[j]) > d:
                    d = int(bank[j])
                    idx = j

            s += str(d)
            idx += 1


        total += int(s)



    print("Total:", total)

