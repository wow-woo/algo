def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()

	abs_val=float('inf')
	abs_arr=[]
	for a_item in arrayOne:
		for b_item in arrayTwo:
			# which array an item is bigger from?
			# if a bigger, we need to go all the way to the end
			# if a smaller, we look into only first element of araryTwo
			if a_item > b_item:
				diff = abs(a_item - b_item)
				if diff < abs_val:
					abs_val=diff
					abs_arr = [a_item, b_item]
			else:
				diff = abs(b_item - a_item)
				if diff < abs_val:
					abs_val=diff
					abs_arr = [a_item, b_item]
				break
	return abs_arr
