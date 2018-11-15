#Write a function called string_search() that takes two
#parameters, a list of strings, and a string. This function
#should return  a list of all the indices at which the
#string is found within the list.
# #
# #You may assume that you do not need to search inside the
# #items in the list; for examples:
# #
# #  string_search(["bob", "burgers", "tina", "bob"], "bob")
# #      -> [0,3]
# #  string_search(["bob", "burgers", "tina", "bob"], "bae")
# #      -> []
# #  string_search(["bob", "bobby", "bob"])
# #      -> [0, 2]
# #
# #Use a linear search algorithm to achieve this. Do not
# #use the list method index.
# #
# #Recall also that one benefit of Python's general leniency
# #with types is that algorithms written for integers easily
# #work for strings. In writing string_search(), make sure
# #it will work on integers as well -- we'll test it on
# #both.


# #Write your code here!

# def string_search(strList, str):
# 	locations = []
# 	for i in range(len(strList)):
# 		if strList[i] == str:
# 			locations.append(i)
# 	return locations



# #Feel free to add code below to test your function. You
# #can, for example, copy and print the test cases from
# #the instructions.

# print(string_search(['nope', 'nope', 'yeah', 'nope', 'yeah'], 'yeah'))









#Recall in Worked Example 5.2.5 that we showed you the code
#for two versions of binary_search: one using recursion, one
#using loops.
#
#In this problem, we want to implement a new version of
#binary_search, called binary_year_search. binary_year_search
#will take in two parameters: a list of instances of Date,
#and a year as an integer. It will return True if any date
#in the list occurred within that year, False if not.
#
#For example, imagine if listOfDates had three instances of
#date: one for January 1st 2016, one for January 1st 2017,
#and one for January 1st 2018. Then:
#
#  binary_year_search(listOfDates, 2016) -> True
#  binary_year_search(listOfDates, 2015) -> False
#
#You should not assume that the list is pre-sorted, but you
#should know that the sort() method works on lists of dates.
#
#Instances of the Date class have three attributes: year,
#month, and day. You can access them directly, you don't
#have to use getters (e.g. myDate.month will access the
#month of myDate).
#
#You may copy the code from Worked Example 5.2.5 and modify
#it instead of starting from scratch.
#
#Don't move this line:
from datetime import date


#Write your code here!

# V1 - Moving the index around a steady dateList.  DONE and validated.
# def binary_year_search(dateList, searchYear):
# 	dateList.sort()
# 	maximum = len(dateList) - 1
# 	minimum = 0

# 	while maximum >= minimum:
# 		middle = minimum + ((maximum - minimum) // 2)
# 		# print('search year', searchYear)
# 		# print('min',minimum, dateList[minimum].year)
# 		# print('middle',middle, dateList[middle].year)
# 		# print('max',maximum, dateList[maximum].year, '\n')

# 		if dateList[middle].year == searchYear:
# 			return True

# 		elif dateList[middle].year > searchYear:
# 			maximum = middle - 1
# 			# repeat step 1

# 		elif dateList[middle].year < searchYear:
# 			# find new middle
# 			minimum = middle + 1
# 			# repeat step 1

# 	return False

#V2 - Modifying the dateList itself
def binary_year_search(dateList, searchYear):
	dateList.sort()

	while len(dateList) > 0:
		middle = (len(dateList) - 1) // 2

		# print('search year', searchYear)
		# print(dateList)

		if dateList[middle].year == searchYear:
			return True

		elif searchYear < dateList[middle].year:
			dateList = dateList[:(middle - 1)]
			
		elif searchYear > dateList[middle].year:
			dateList = dateList[(middle + 1):]

	return False


#The lines below will test your code. If it's working
#correctly, they will print True, then False, then True.
listOfDates = [date(2016, 11, 26), date(2014, 11, 29), 
               date(2008, 11, 29), date(2000, 11, 25), 
               date(1999, 11, 27), date(1998, 11, 28), 
               date(1990, 12, 1), date(1989, 12, 2), 
               date(1985, 11, 30)]

print(binary_year_search(listOfDates, 2016))
print(binary_year_search(listOfDates, 2007))
print(binary_year_search(listOfDates, 2008))

