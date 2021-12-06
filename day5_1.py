import utils.utils as ut
import numpy as np
import matplotlib.pyplot as plt
vent_lines = []

ocean_floor = np.zeros((1000, 1000))

with open("input/day5.txt") as file: 

    input_text = file.read()
    for line in input_text.split("\n"):
        line, succ = ut.parse_line(line)
        if succ:
            vent_lines.append(line)
        
    vent_lines = np.asarray(vent_lines)

overlaps = 0
for [start, end] in vent_lines:
    dir = 0
    line_len = 0
    if (start[1]==end[1]):
        line_len = end[0] - start[0]
    elif (start[0]==end[0]):
        line_len = end[1] - start[1]
        dir = 1

    for i in ut.range_neg_inc(line_len):
        x = 0
        y = 0
        if dir == 0:
            x = start[0]+i
            y = start[1]
        if dir == 1:
            x = start[0]
            y = start[1]+i
       
        ocean_floor[x,y] += 1
        if ocean_floor[x,y] == 2:
            overlaps += 1

plt.imshow(ocean_floor)
plt.show()
print(overlaps)