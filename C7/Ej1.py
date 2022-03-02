# https://docs.python.org/3/tutorial/inputoutput.html

# Lectura
f = open('Prueba1.txt', 'w')

cont = 1
for i  in range(20):
    f.writelines(str(cont)+"\n")
    cont += 1
    
f.close()

