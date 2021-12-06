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

position = [0,0,0] #horizontal position, depth, aim

for command, val in course_readings:
    print(command, val)
    if (command == "forward"):
        position[0] += val
        position[1] += val*position[2]
    elif (command == "down"):
        position[2] += val
    elif (command == "up"):
        position[2] -= val
    print(position, end = "\n\n")

print(position[0] * position[1])



