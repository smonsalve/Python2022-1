
import random
letters = list(range(65,90))
number = list(range(48,57))
plate_letter_length = 3
plate_number_length = 3
new_plate_number_length = 4
old_letter_plate = ""
old_number_plate = ""
new_letter_plate = ""
new_number_plate = ""


## old plate
# generate the random letters 
for i in range(plate_letter_length):
    old_letter_plate += chr(random.choice(letters))

# generate the random numbers
for j in range(plate_number_length):
    old_number_plate += chr(random.choice(number))


## new plate
# generate the random letters 
for k in range(plate_letter_length):
    new_letter_plate += chr(random.choice(letters))

# generate the random numbers
for l in range(new_plate_number_length):
    new_number_plate += chr(random.choice(number))


## randomly choose if old or new plate format
list = ('old plate', 'new plate')
x = random.choice(list)
print(x)

if x == 'old plate': 
    print(old_letter_plate,old_number_plate)
else:
    print(new_number_plate,new_letter_plate)