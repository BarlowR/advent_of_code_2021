import utils.utils as ut
course_readings = []

with open("input/day2.txt") as file: 

    input_text = file.read()

    for cmd in input_text.split("\n"):
        command_tup, success = ut.parse_command(cmd)
        if success:
            course_readings.append(command_tup)
        else:
            print("parse issue")

position = [0,0] #horizontal position, depth

for command, val in course_readings:
    if (command == "forward"):
        position[0] += val
    elif (command == "down"):
        position[1] += val
    elif (command == "up"):
        position[1] -= val

print(position[0] * position[1])



