# claves =  ["B","I","N","G","O"]
# numeros = list(range(1,16))

# cont = 1
# for c in range(5):
#     for i in numeros:
#         print(f"{claves[c]}{cont}", end = " ") 
#         cont +=1
#     print()




def crear_bingo(cantidad):

    claves =  ["B","I","N","G","O"]
    numeros = list(range(1,cantidad+1))
    posibilidades = []
    
    cont = 1
    for c in range(5):
        letras = []
        for i in numeros:
            letras.append(f"{claves[c]}{cont}") 
            cont +=1
        posibilidades.append(letras)
    return(posibilidades)





print(crear_bingo(5))
#matriz = crear_bingo(20)
#print(matriz[3][12])
# def random_card():
#     card = {"B", "I", "N", "G", "O"}





# numeros = [0, 1, 2, 3, 4]
# letras = []
# posibilidades = []
# claves =  ["B","I","N","G","O"]


# cont = 0
# for i in numeros:
#     letras.append(f"{claves[i]}{cont}") 
#     cont +=1
# posibilidades.append(letras)

# print(letras[0])
# print(posibilidades[0])