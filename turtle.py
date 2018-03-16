from random import randint

dogs=0
watches=0
concert_tickets=0
candies=0
yachts=0

for i in range(0,100000):
	years = randint(0,5)
	months = randint(0,11)
	days = randint(0,30)

	relationship_length = [years, months, days]

	if relationship_length[0] >= 4:
		dogs += 1
	elif relationship_length[0]>=1:
		watches += 1
	elif relationship_length[1] >= 6:
		concert_tickets += 1
	elif relationship_length[2] >= 1:
		candies += 1
	else:
		yachts += 1
	
	i += 1

print("dogs:",dogs,"\n","watches:",watches,"\n","concert_tickets:",concert_tickets,"\n","candies:",candies,"\n","yachts:",yachts)
