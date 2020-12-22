def isValidSubsequence(array, sequence):
	# 2arrays are the same
    if array == sequence:
	    return True

	idx=0
	for item in sequence:
		match = False
		for idx_array in range(idx, len(array)):
			match = False
			if item == array[idx_array]:
				idx = idx_array+1
				match = True
				break
		if not match:
			return False
	return True
