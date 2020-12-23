def moveElementToEnd(array, toMove):
	last_idx=len(array)-1
	idx=0
	while idx <= last_idx and last_idx >=0:
		if array[idx] == toMove:
			#swap
			#target to swap could be toMove
			while array[last_idx] == toMove and idx < last_idx:
				last_idx -= 1
			
			#you don't look back since No swap needed,
			if idx >= last_idx:
				break
				
			array[idx], array[last_idx] = array[last_idx], array[idx]
			last_idx -= 1
		idx += 1
			
	return array