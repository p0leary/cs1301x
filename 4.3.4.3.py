def two_dimensional_booleans(superlist, use_and):
	results = []
	for sublist in superlist:
		if use_and:
			results.append(not False in sublist)
		else:
			results.append(True in sublist)
	return results

#If your function works correctly, this will originally
#print:
#[True, False, False]
#[True, True, False]
bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))

