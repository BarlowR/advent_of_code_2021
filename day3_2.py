from functools import reduce
from os import read
import utils.utils as ut
import numpy as np

diagnostic_readings = np.zeros(1)


with open("input/day3.txt") as file: 

    temp_list = []
    input_text = file.read()

    for reading in input_text.split("\n"):
        reading, success = ut.parse_bits(reading)
        if success and len(reading) > 0 :
            temp_list.append(reading)
    
    diagnostic_readings = np.asarray(temp_list)

oxygen_reading = diagnostic_readings.copy()
index = 0

while len(oxygen_reading)>1:
    bit_to_keep = 0.5 <= np.sum(oxygen_reading[:, index])/len(oxygen_reading)
    print(bit_to_keep, index)
    oxygen_reading = oxygen_reading[oxygen_reading[:, index] == bit_to_keep]
    print(oxygen_reading)
    index += 1


scrubber_reading = diagnostic_readings.copy()
index = 0
while len(scrubber_reading)>1:
    bit_to_keep = 0.5 > np.sum(scrubber_reading[:, index])/len(scrubber_reading)
    print(bit_to_keep, index)
    scrubber_reading = scrubber_reading[scrubber_reading[:, index] == bit_to_keep]
    print(scrubber_reading)
    index += 1

oxy_digit = ut.reduce(oxygen_reading[0].astype(bool))
scrubber_digit = ut.reduce(scrubber_reading[0].astype(bool))

print(oxy_digit, scrubber_digit, oxy_digit*scrubber_digit)