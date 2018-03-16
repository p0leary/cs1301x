def sort_artists(tuple_list): #each tuple = ('artist_name', int(album_sales))
	artist_list = []
	sales_list = []
	for artist in tuple_list:
		artist_list.append(artist[0])
		sales_list.append(artist[1])
	artist_list.sort()
	sales_list.sort()
	sales_list.reverse()
	return (artist_list, sales_list)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])  
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))