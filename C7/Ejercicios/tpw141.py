# nombre del archivo 
# abrir el archivo (nombre y modo lectura)
# leer las lineas del archivo

f = open("Ejercicios/elements.txt", 'r')
for line in f.readlines()[-1:]:
    print(line, end="-")
f.close()