import numpy as np

def next_step(row_idx, col_idx, direction):
	
	if direction == 'r':
		col_idx += 1
	elif direction == 'd':
		row_idx += 1
	elif direction == 'l':
		col_idx -= 1
	elif direction == 'u':
		row_idx -= 1

	return (row_idx, col_idx)

def reverse_step(row_idx, col_idx, direction):
	if direction == 'r':
		row_idx += 1
	elif direction == 'd':
		col_idx -= 1
	elif direction == 'l':
		row_idx -= 1
	elif direction == 'u':
		col_idx += 1

	return (row_idx, col_idx)

def snail(snail_map):
	snail_map = np.array(snail_map)
	traversed = np.full_like(snail_map, False, dtype=bool)   # marks if element traversed
	direction_list = ['r', 'd', 'l', 'u']
	direction_idx = 0
	direction = direction_list[direction_idx]
	row_idx, col_idx = 0,0
	max_row, max_col = np.shape(snail_map)
	sort_list = []
	while not np.all(traversed):	# go until all elements are traversed
		if ((row_idx < max_row) and (col_idx < max_col)) and (not(traversed[row_idx, col_idx])):	 # keep going in same direction, append to list
			sort_list.append(snail_map[row_idx, col_idx])
			traversed[row_idx, col_idx] = True
		else:   # a violation has occurred, needs direction change
			direction_idx = (direction_idx+1)%(len(direction_list))
			direction = direction_list[direction_idx]
			row_idx, col_idx = reverse_step(row_idx, col_idx, direction) 	# reverse the step taken in wrong direction out of bounds
		row_idx, col_idx = next_step(row_idx, col_idx, direction)   # next step in same direction
	return sort_list

array = [[1,2,3],
		 [8,9,4],
		 [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))	# expected