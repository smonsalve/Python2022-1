import random

def gen_placa(pais):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = [0,1,2,3,4,5,6,7,8,9]
    placa = ""
    if (pais == "Colombia"):
        for i in range(3): placa += letras[random.randint(0,25)]
        for j in range(3):  placa += str(numeros[random.randint(0,9)])
        return(placa)
    elif(pais == "Francia"):
        for i in range(2): placa += letras[random.randint(0,25)]
        for j in range(2): placa += str(numeros[random.randint(0,9)])
        return(placa)

placas_francia = []
for i in range(20):   placas_francia.append(gen_placa("Francia"))
placas_col = []
for i in range(20):   placas_col.append(gen_placa("Colombia"))
print(placas_francia)
print(placas_col)