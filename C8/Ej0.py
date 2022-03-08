archivo = open("in0.txt", "r")

lista_lineas = archivo.readlines()

lista_nums = []
cont = 0
while(cont < len(lista_lineas)):
    linea = lista_lineas[cont]
    sin_fin_de_linea = linea.strip("\n")
    numero = int(sin_fin_de_linea)
    lista_nums.append(numero)
    cont = cont + 1

print(lista_nums)