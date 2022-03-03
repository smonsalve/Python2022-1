f = open("entrada.txt")

longest = []
len_lon = 0
lineas = f.readlines()
palabras = []

for line in lineas:
    for word in line.split(" "):
        palabra = word.rstrip()
        palabras.append(palabra)
        long_palabra = len(palabra)
        if  long_palabra > len_lon:
            len_lon = long_palabra

print(len_lon)

for p in palabras:
    if len(p) == len_lon:
        longest.append(p)

print(longest)
print(set(palabras))

f.close()