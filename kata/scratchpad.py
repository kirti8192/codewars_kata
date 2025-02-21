import numpy as np

def comp(array1, array2):
	if isinstance(array1, list) & isinstance(array2, list):
		if (array1 == array2) & (len(array1)==0):
			return True
	if not array1 or not array2:
		return False
	
	# both arrays are valid now
	if sorted(array1) == sorted(array2):
		return False

    # process array 2 first
	if not isinstance(array2, list):
		array2 = [array2]
	array2 = np.sqrt(np.array(array2))
	if any(array2%1):
		return False
	array2.sort()
	array2 = array2.astype(int)
	
    # process array 1
	if not isinstance(array1, list):
		array1 = [array1]
	array1 = np.array(array1)
	array1 = np.abs(array1)
	array1.sort()

	return np.all(array1 == array2)