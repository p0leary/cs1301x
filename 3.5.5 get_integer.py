def get_integer(my_var):
    try:
        result = int(my_var)
    except Exception as error:
        return error
    else:
        return result
print(get_integer("Boggle."))