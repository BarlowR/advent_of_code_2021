from os import read
import utils.utils as ut
import numpy as np

diagnostic_readings = []


with open("input/day3.txt") as file: 

    input_text = file.read()

    for reading in input_text.split("\n"):
        reading, success = ut.parse_bits(reading)
        if success and len(reading) > 0 :
            diagnostic_readings.append(reading)

most_common_digit = np.round(np.sum(diagnostic_readings, axis=0)/np.size(diagnostic_readings, 0)).astype(bool)

least_common_digit = np.logical_not(most_common_digit)

gamma = ut.reduce(most_common_digit)
epsilon = ut.reduce(most_common_digit)

print(gamma)
