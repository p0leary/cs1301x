punctuation = [".",",","!","?"]

def word_count(my_string):
    try:
        if my_string[0] != ' ' and not my_string[0] in punctuation:
        	word_count = 1
        else:
        	word_count = 0        
        last_char = ''
        for char in my_string:
            if (char != ' ' and char not in punctuation) and last_char == (' '):
                word_count += 1
            last_char = char
        return(word_count)
    except TypeError:
        return("Not a string")    

def string_length(my_string):
	string_length = 0
	try:
		for char in my_string:
			if char != ' ' and char not in punctuation:
				string_length += 1
		return string_length
	except TypeError:
		return "Not a string"

def average_word_length(my_string):
	length = string_length(my_string)
	words = word_count(my_string)
	try:
		if length == "Not a string" or word_count == "Not a string":
			return "Not a string"
		else:
			return length / words
	except ZeroDivisionError:
		return "No words"


#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words

print("test_1 avg",average_word_length("Hi"))
print("test_1 string length:",string_length("Hi"))
print("test_1 word count",word_count("hi"))
print("test_2 average_word_length",average_word_length("Hi, Lucy"))
print("test_2 string length:",string_length("Hi, Lucy"))
print("test_2 word count",word_count("hi, lucy"))
print("test_3 average_word_length",average_word_length("   What   big spaces  you    have!"))
print("test_2 string length:",string_length("   What   big spaces  you    have!"))
print("test_2 word count",word_count("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))
# print("string length:",string_length("?!?!?! ... !"))
# print("word count",word_count("?!?!?! ... !"))