def multiply_strings(string_list):
    # for item in string_list[::2]:
    #     item *= 2
    #     print(item)
    # for item in string_list[::3]:
    #     item *= 3
    #     print(item)
    # return string_list

    for i in range(0,len(string_list)):
    	if i % 2 == 0:
    		string_list[i] *= 2
    	if i % 3 == 0:
    		string_list[i] *= 3
    return string_list


test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))