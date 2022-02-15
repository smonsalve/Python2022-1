import random

caracteres = list(range(33,127))
longitud = random.randint(7,10)

psw = ""

for j in range(longitud):
    psw += chr(random.choice(caracteres))

print(psw)
