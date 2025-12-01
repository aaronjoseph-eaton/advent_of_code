

file_path = "input_2.in" 

pos = 50
count = 0

with open(file_path, "r") as file:

    for line in file:
        direction = line[0]
        clicks = int(line[1:])

#        print("\n\ncount: " + str(count) + " pos: "  +  str(pos) + "     " + direction  + "   " + str(clicks))

        if clicks >= 100 : 
            count += int(clicks/100)


        clicks %= 100

        if direction == "L":

            if (clicks > pos) and (pos != 0):
                count += 1

            clicks = (100 - clicks)



        else:
            if (clicks > (100 - pos))  and (pos != 0):
                count += 1

        pos = int((pos + clicks)) % 100

        if pos % 100 == 0:
            count += 1

        

#print(str(pos)+ "  ")
print(count)
 
