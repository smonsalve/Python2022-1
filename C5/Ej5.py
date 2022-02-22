
archivo = open('entrada.csv','r')

for line in archivo.readlines():
    for palabra in line.split(","):
        print(palabra.rstrip("\n"))
