file_path = "input.txt"  # Replace with the actual file path
# file_path = "test.in"  # Replace with the actual file path

total = 0

width = 101
height = 103
mid_width = width // 2
mid_height = height // 2

t = 100

q1_tot = 0
q2_tot = 0
q3_tot = 0
q4_tot = 0


with open(file_path) as file:
    for line in file:
        coords = line.split(" ")

        pos = coords[0].replace("p=", "")
        vel = coords[1].replace("v=", "")

        pos = pos.split(",")
        vel = vel.split(",")

        vel[0] = int(vel[0])
        vel[1] = int(vel[1])

        pos[0] = int(pos[0])
        pos[1] = int(pos[1])

        if(vel[0] < 0):
            v0_dir = -1
            vel[0] *= -1
        else:
            v0_dir = 1

        if(vel[1] < 0):
            v1_dir = -1
            vel[1] *= -1
        else:
            v1_dir = 1

        vel[0] = int((int(vel[0]) * t) % width) * v0_dir
        vel[1] = int((int(vel[1]) * t) % height) * v1_dir

        pos[0] = (pos[0] + vel[0]) % width
        pos[1] = (pos[1] + vel[1]) % height

        if(pos[0] < mid_width):
            if(pos[1] < mid_height):
                q1_tot += 1
            else:
                if (pos[1] > mid_height):
                    q3_tot += 1

        else:
            if (pos[0] > mid_width):
                if(pos[1] < mid_height):
                    q2_tot += 1
                else:
                    if(pos[1] > mid_height):
                        q4_tot += 1

total = q1_tot * q2_tot * q3_tot * q4_tot

print(total)
