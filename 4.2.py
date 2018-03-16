# 4.2.2
# def third_character(s):
# 	try:
# 		return s[2]
# 	except Exception as e:
# 		return "Too short"
	
# print(third_character("CS1301"))
# print(third_character("Georgia Tech"))
# print(third_character("GT"))

# 4.2.3
# def last_n(search_string, n):
# 	if len(search_string)>=n:
# 		return search_string[-n:]
# 	else:
# 		return search_string

# print(last_n("123456789", 3))
# print(last_n("Bulbasaur", 4))
# print(last_n("1", 5))

# # 4.2.4
# def in_parentheses(x):
# 	open_index = x.find('(')
# 	close_index = x.find(')', open_index)
# 	if open_index > 0 and close_index > 0:
# 		return x[open_index+1:close_index]
# 	else:
# 		return ''

# print(in_parentheses("This is a sentence (words!)."))
# print(in_parentheses("No parentheses here!"))
# print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
# print(in_parentheses("Open ( only"))
# print(in_parentheses("Closed ) only"))
# print(in_parentheses("Closed ) before ( open"))
# print(in_parentheses("That's a lot of test cases(!)"))

# mystring = '1234567890'
# # print(mystring[6:])
# # print(mystring[5:10])
# # print(mystring[:-4])
# # print(mystring[-4:])
# # print(mystring[len(mystring)-4:])
# print(mystring[5]+mystring[7]+mystring[9])
# print(mystring[4::2])
# print(mystring[5:9:2])
# print(mystring[-6:10:2])
# print(mystring[::2])

# mystring_odd = 'abcdefg'
# mystring_even = 'abcdefgh'
# print(mystring_odd[4::2])
# print(mystring_odd[4:-1:2])

# 4.2.5
# def string_type(aString):
# 	if aString == '':
# 		return "empty"
# 	else:
# 		length = len(aString)
# 		if length == 1:
# 			return "character"
# 		elif length > 1:
# 			num_spaces = aString.count(' ')
# 			num_periods = aString.count('.')
# 			num_paras = aString.count('\n')
# 			if num_paras > 0:
# 				return "page"
# 			elif num_spaces == 0:
# 				return "word"
# 			elif num_periods <= 1:
# 				return "sentence"
# 			else:
# 				return "paragraph"

# 4.2.6
# def input_type(some_input):
# 	if some_input.isdigit():
# 		return "integer"
# 	elif (some_input.replace('.','',1)).isdigit():
# 		return "float"
# 	elif some_input in ["True", "False"]:
# 		return "boolean"
# 	else:
# 		return "string"

# print(input_type(""))
# print(input_type("False"))
# print(input_type("7.432621"))
# print(input_type("2788"))

#4.2.7
def find_color(rgb_string):
	split1 = rgb_string.split("(")
	split2 = split1[1].split(")")
	rgb = split2[0].split(",")
	r = int(rgb[0].strip())
	g = int(rgb[1].strip())
	b = int(rgb[2].strip())
	if r > g and r > b:
		return "red"
	elif g > r and g > b:
		return "green"
	elif b > r and b > g:
		return "blue"
	elif r == g and r > b:
		return "yellow"
	elif r == b and r > g:
		return "purple"
	elif b == g and b > r:
		return "teal"
	elif r == b and r == g:
		return "gray"

print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(125, 17, 125)"))
print(find_color("rgb(217, 217, 217)"))
