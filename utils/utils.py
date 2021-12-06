import numpy as np
def parse_int(int_val_string):
    try:
        return ((int(int_val_string), True))
    except ValueError:
        return ((int_val_string, False))

def parse_command(command_string):
    try:
        command, value = command_string.split(" ")
        int_val = int(value)
        return ((command, int_val), True)
    except ValueError:
        return (((), False))

def parse_bits(bits_string):
    bit_list = np.asarray([0]*len(bits_string))
    for idx, bit in enumerate(bits_string):
        if bit == "1":
            bit_list[idx] = 1
        elif bit != "0":
            return ((bit_list, False))
    return ((bit_list, True))


def reduce(binary_array):
    result = 0
    for ele in binary_array:
        result = (result << 1) | ele
    return result

def parse_line(line_string):
    try: 
        line = [[0,0],[0,0]]
        [start_str, end_str] = line_string.split(" -> ")
        start_split = start_str.split(",")

        val, suc = parse_int(start_split[0])
        if suc:
            line[0][0] = val
        else: 
            return (([], False)) 
        val, suc = parse_int(start_split[1])
        if suc:
            line[0][1] = val
        else: 
            return (([], False)) 
        
        end_split = end_str.split(",")
        val, suc = parse_int(end_split[0])
        if suc:
            line[1][0] = val
        else: 
            return (([], False)) 
        val, suc = parse_int(end_split[1])
        if suc:
            line[1][1] = val
        else: 
            return (([], False)) 

        return ((line, True))
    except ValueError:
        return (([], False)) 

def range_neg_inc(start, end):
    if start < end:
        return(range(start, end+1))
    else:
        return(range(start, end-1, -1))
    
def range_neg_inc(len):
    if len > 0:
        return(range(0, len+1))
    elif len<0:
        return(range(0, len-1, -1))
    else:
        return [0]

def sign(val):
    return (int)(val/abs(val))


