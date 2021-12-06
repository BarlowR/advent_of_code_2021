import utils.utils as ut
depth_readings = []


with open("input/day1.txt") as file: 

    input_text = file.read()

    for depth in input_text.split("\n"):
        depth_value, success = ut.parse_int(depth)
        if success:
            depth_readings.append(depth_value)
            print(depth_value)

depth_increases = 0
for i in range(0, len(depth_readings)-1):
    if depth_readings[i+1] > depth_readings[i]:
        depth_increases +=1

print(f"The depth increases {depth_increases} times")
    