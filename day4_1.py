from numpy.lib.nanfunctions import nancumsum
import utils.utils as ut
import numpy as np

bingo_nums = []
boards = []

with open("input/day4.txt") as file: 

    input_text = file.read()

    temp = input_text.split("\n")
    
    for num in temp[0].split(","):
        int_num, success = ut.parse_int(num)
        if success:
            bingo_nums.append(int_num)

    print()
    boards = np.zeros(((int)((len(temp)-2)/6), 5, 5))
    for i in range(2, len(temp), 6):
        board = np.zeros((5,5))
        for row, line in enumerate(temp[i:i+6]):
            for col, num in enumerate(range(0, 15, 3)):
                int_num, success = ut.parse_int(line[num:num+3])
                if success and row < 5 and col < 5:
                    board[row, col] = int_num
        boards[(int)((i-2)/6), :, :] = board

checked = np.empty(boards.shape)
completed_board_index = 0         
bingo_draw_index = 0

diag_left = np.diag([True]*5)
diag_right = np.flip(diag_left, axis=0)

for val in bingo_nums:
    bingo_draw_index += 1
    checked = np.logical_or(checked, boards == val)

    if (5 in np.sum(checked, axis=1)):
        completed_board_index = (np.where(np.sum(checked, axis=1)==5), 1)
        break
    if (5 in np.sum(checked, axis=2)):
        completed_board_index = (np.where(np.sum(checked, axis=2)==5), 2)
        break


done_board = boards[completed_board_index[0][0]][0]
print(bingo_nums[0:bingo_draw_index])
print(checked[completed_board_index[0][0]])
print(done_board)

board_sum = np.sum(done_board, where = np.logical_not(checked[completed_board_index[0][0]]))
last_bingo_call = bingo_nums[bingo_draw_index-1]

print(board_sum * last_bingo_call)


