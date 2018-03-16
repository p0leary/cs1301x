myString = "This string is not a number!"
try:
	print("Converting myString to int...")
	print(1/0)
	print("String #"+1+":"+ myString)
	myInt = Int(myString)
	print(myInt)
except ValueError as error:
	print(error)
except TypeError as error:
	print(error)
finally:
	print("An unknown error has occured!")
print("Done!")