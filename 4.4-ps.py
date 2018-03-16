
#Coding Problem 4.4.1
# def angry_file_finder(filename):
# 	newFile = open(filename)
# 	lines = newFile.readlines()
# 	for line in lines:
# 		if "!" not in line:
# 			return False
# 	else:
# 		return True
# 	newFile.close()
# print(angry_file_finder("AngryFileFinderInput.txt"))

#Coding Problem 4.4.2

# def format_checker(filename):
# 	file_reader = open(filename, "r")
# 	weight_total = 0.0
# 	for line in file_reader:
# 		line_as_list = line.split(" ")
# 		print(line_as_list)
# 		#check whether there are 5 elements separated by spaces
# 		if (len(line_as_list)) != 5:
# 			file_reader.close()
# 			return False
# 		#check whether elements 0, 2, and 3 are integers
# 		try:
# 			int(line_as_list[0])
# 			int(line_as_list[2])
# 			int(line_as_list[3])
# 		except:
# 			file_reader.close()
# 			return False
# 		#check whether element 4 is a decimal number
# 		try:
# 			float(line_as_list[4])
# 		except:
# 			file_reader.close()
# 			return False
# 		#check whether all element 4s sum to 1
# 		weight_total += float(line_as_list[4])
# 	if weight_total != 1.0:
# 		file_reader.close()
# 		return False
# 	else:
# 		return True
# 	file_reader.close()

# Test your function below. With the original values of these
# files, these should print True, then False:
# print(format_checker("sample_1.cs1301"))
# print(format_checker("sample_2.cs1301"))
# print(format_checker("sample_3.cs1301"))

#Coding Problem 4.4.3

# def reader(filename):
# 	file_reader = open(filename, "r")
# 	output = []
# 	for line in file_reader:
# 		elements = line.split(" ")
# 		output.append((int(elements[0]), elements[1], int(elements[2]), int(elements[3]), float(elements[4])))
# 	file_reader.close()
# 	return output

# print(reader("sample_1.cs1301"))

#Coding Problem 4.4.4

# def write_1301(filename, tuple_list):
# 	file_writer = open(filename, "w")
# 	for line in tuple_list:
# 		print(line[0], line[1], line[2], line[3], line[4], file = file_writer)
# 	file_writer.close()

# #The code below will test your function. It's not used
# #for grading, so feel free to modify it! You may check
# #output.cs1301 to see how it worked.
# tuple1 = (1, "exam_1", 90, 100, 0.6)
# tuple2 = (2, "exam_2", 95, 100, 0.4)
# tupleList = [tuple1, tuple2]
# write_1301("output.cs1301", tupleList)

#Coding Problem 4.4.5

# def reader(filename):
# 	file_reader = open(filename, "r")
# 	output = []
# 	for line in file_reader:
# 		elements = line.split(" ")
# 		output.append((int(elements[0]), elements[1], int(elements[2]), int(elements[3]), float(elements[4])))
# 	file_reader.close()
# 	return output

# def get_grade(filename):
# 	tuple_list = reader(filename)
# 	sum_of_grades = 0
# 	for assignment in tuple_list:
# 		sum_of_grades += (assignment[2]/assignment[3])*assignment[4]
# 	# 	print(sum_of_grades)
# 	# print("Final Grade is: " + str(sum_of_grades*100))
# 	return sum_of_grades * 100

# #Below are some lines of code that will test your function.
# #You can change the value of the variable(s) to test your
# #function with different inputs.
# #If your function works correctly, this will originally
# #print: 91.55 
# print(get_grade("sample.cs1301"))

#Coding Problem 4.4.6

def sort_films(filename_in, filename_out):
	file_read = open(filename_in, "r")
	file_write = open (filename_out, "w")
	movie_list = []
	for line in file_read:
		line_list = line.split("\t")
		movie_list.append((line_list[0], int(line_list[1])))
	movie_list.sort(key=lambda tup: tup[1], reverse = True)
	for line in movie_list:
		print(str(line[0])+"\t"+str(line[1]), file = file_write)
	file_read.close()
	file_write.close()

#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")
