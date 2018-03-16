# def lucky_sevens(int_list):
# 	consecutive_sevens = 0
# 	last_letter_7 = False
# 	for n in int_list:
# 		if consecutive_sevens == 3:
# 			return True
# 		else:
# 			if n == 7:
# 				consecutive_sevens += 1
# 				last_letter_7 = True
# 			else:
# 				consecutive_sevens = 0
# 				last_letter_7 = False
# 	if consecutive_sevens < 3:
# 		consecutive_sevens = 0
# 		last_letter_7 = False
# 		return False


# #If your function works correctly, this will originally
# #print: True, then False
# print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
# print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))

# 4.3.2
# def attendance_check(roster, present): #both are lists of strings
# 	all_students = roster
# 	present_students = present
# 	for attendee in present_students:
# 		all_students.remove(attendee)
# 	all_students.sort()
# 	return all_students

# #Below are some lines of code that will test your function.
# #You can change the value of the variable(s) to test your
# #function with different inputs.
# #
# #If your function works correctly, this will originally
# #print: 
# #['Ferguson', 'Winston']
# test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
# test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
# print(attendance_check(test_roster, test_present))

# 4.3.3
# def grade_scantron(answers, key):
# 	grade = 0
# 	if len(answers) != len(key):
# 		return -1
# 	else:
# 		for i in range(0,len(answers)):
# 			if answers[i] == key[i]:
# 				grade += 1
# 	return grade

# #Below are some lines of code that will test your function.
# #You can change the value of the variable(s) to test your
# #function with different inputs.
# #
# #If your function works correctly, this will originally
# #print: 7
# test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
# test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
# print(grade_scantron(test_answers, test_key))

# import math
# def solve_right_triangle(opposite, adjacent, use_degrees=False):
# 	hypotenuse = (opposite**2 + adjacent**2)**(1/2)
# 	angle = math.atan(opposite/adjacent) # in radians
# 	if use_degrees == True:
# 		angle = math.degrees(angle) # in degrees if use_degrees is true
# 	return (hypotenuse, angle)


# #If your function works correctly, this will originally
# #print:
# #(5.0, 0.6435011087932844)
# #(5.0, 36.86989764584402)
# print(solve_right_triangle(3.0, 4.0))
# print(solve_right_triangle(3.0, 4.0, use_degrees = True))

# def find_max_sales(movie_list):
# 	highest_sales = 0
# 	for movie in movie_list:
# 		if movie[1] > highest_sales:
# 			highest_sales = movie[1]
# 			top_movie = movie[0]
# 	return top_movie

# #If your function works correctly, this will originally
# #print: Rogue One
# movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]
# print(find_max_sales(movie_list))

# Coding Problem 4.3.6
def string_splitter(a_string):
	list_of_words = []
	current_word = ''
	for char in a_string:
		if char == ' ':
			list_of_words.append(current_word)
			current_word = ''
		else: 
			current_word += char
	list_of_words.append(current_word)
	return list_of_words
		
			

#If your function works correctly, this will originally
#print: ['Hello', 'world']
print(string_splitter("Hello world"))









