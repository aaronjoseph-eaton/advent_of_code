import numpy as np
from sympy import *
import json

file_path = "input_13_1.in"  # Replace with the actual file path
#file_path = "test.in"  # Replace with the actual file path

total = 0

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def process_coordinates(line, button=None):
    if button:
        coords = line.replace(f"Button {button}: ", "")
    else:
        coords = line.replace(f"Prize: ", "")
    split_coord = coords.split(", ")
    if button:
        if button == "A":
            cost = 3
        else:
            cost = 1

        X = split_coord[0].replace("X+", "")
        Y = split_coord[1].replace("Y+", "")
    else:
        cost = 0
        X = split_coord[0].replace("X=", "")
        Y = split_coord[1].replace("Y=", "")
    return {"X": int(X), "Y": int(Y), "cost": cost}

machines = []
machine_id = 0

with open(file_path) as f:
    for idx, line in enumerate(f.readlines()):
        line = line.strip()
        # print(line)
        mod = idx % 4
        if mod == 0:
            machine = {}
            machine["A"] = process_coordinates(line, "A")
            pass
        elif mod == 1:
            machine["B"] = process_coordinates(line, "B")
            pass
        elif mod == 2:
            machine["PRIZE"] = process_coordinates(line)
            pass
        elif mod == 3:
            """             a = np.array([[machine["A"]["X"], machine["B"]["X"]], [machine["A"]["Y"], machine["B"]["Y"]]])
            b = np.array([machine["PRIZE"]["X"], machine["PRIZE"]["Y"]])

            ax = int(machine["A"]["X"])
            bx = int(machine["B"]["X"])

            ay = int(machine["A"]["Y"])
            by = int(machine["B"]["Y"])

            px = int(machine["PRIZE"]["X"])
            py = int(machine["PRIZE"]["Y"])
        
            t = linsolve(Matrix( ([ax, bx, px], [ay, by, py])), (x,y))
            #print(a)
            #print(b)

            # print(ax)
            # print(bx)  

            # print(ay)
            # print(by)            
            
            # print(px)
            # print(py)


            nt = np.linalg.solve(a,b)

            # print(t)
            # print(nt)

            # type_a = type(t.args[0][0])
            # type_b = type(t.args[0][1])

            # print(type_a)
            # print(type_b)

            #print(type(type_a))

            if t.args[0][0] and t.args[0][1]:
                print("YES")
                ta = t.args[0][0] * 3
                tb = t.args[0][1] * 1
                #     print("----")
                total += ((int(t[0]) * 3) + (int(t[1]) * 1))
            #     print("NO")
            #     print(x[0])
            #     print(x[1])
            #     print("----") """

            
            


            a, b = symbols(['a','b'])
            sol = solve([machine["A"]["X"]*a + machine["B"]["X"]*b - machine["PRIZE"]["X"], machine["A"]["Y"]*a + machine["B"]["Y"]*b - machine["PRIZE"]["Y"]], (a, b))

            if sol[a].is_integer and sol[b].is_integer:
                a_presses = int(sol[a])
                b_presses = int(sol[b])
                print(f"machine {machine_id} gets to {machine['PRIZE']['X']},{machine['PRIZE']['Y']} via {a_presses} presses of A and {b_presses} presses of B")
                print(f"{a_presses} * {machine['A']['X']} + {b_presses} * {machine['B']['X']} = {machine['PRIZE']['X']}")
                print(f"{a_presses} * {machine['A']['Y']} + {b_presses} * {machine['B']['Y']} = {machine['PRIZE']['Y']}")
                print(f"Cost: {int((3*a_presses + 1*b_presses))}")
                total += int((machine["A"]["cost"]*a_presses + machine["B"]["cost"]*b_presses))
            else:
                print(f"machine {machine_id} is not solvable")

            machine_id += 1
        print("-----------------")

    print(f"Total: {total}")
#print(total)




