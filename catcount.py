# mystery_string = "my cat your cat"
mystery_string = "catcatcatcatcat!!"


cat_count = 0
letter_before = ''
letter_2_back = ''
for l in mystery_string:
	if (letter_2_back + letter_before + l) == 'cat':
		cat_count += 1
	letter_2_back = letter_before
	letter_before = l
print(cat_count)