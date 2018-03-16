#4.5.4 Exercise 2
# groups = {1: ["Bob", "Susan"], 2: ["Sam", "Steve"]}
# groupNumber = 1
# memberName = "Patrick"

# def addMemberToGroups(groups, groupNumber, memberName):
# 	thisGroup = groups[groupNumber]
# 	thisGroup.append(memberName)
# 	print('memory location of thisGroup is: ' + str(id(thisGroup)))
# 	print('memory location of groups[groupNumber is: ' + str(id(groups[groupNumber])))
# 	print('thisGroup is now: ' + str(thisGroup))
# 	print('groups[groupNumber] is now: ' + str(groups[groupNumber]))

# addMemberToGroups(groups, groupNumber, memberName)

# print(str(groups[groupNumber]))

# lists_of_numbers = [[1, 2], [3, 4]]
# first_list = lists_of_numbers[0]
# # still only one value for list_of_numbers[0]
# # which means if we do this:
# first_list.append('smile')
# # then list_of_numbers[0] gets changed too!
# print(first_list)
# print(lists_of_numbers)


lists_of_numbers = [[1, 2], [3, 4]]
new_list = []
for l in lists_of_numbers:
	numbers = []
	for number in l:
		numbers.append(number)
	new_list.append(numbers)
first_list = new_list[0]
first_list.append(8)

print(first_list)
print(lists_of_numbers[0])

