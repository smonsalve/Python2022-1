import random

def gen_placa(pais):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = [0,1,2,3,4,5,6,7,8,9]
    placa = ""
    if (pais == "Colombia"):
        cont = 1
        while(cont<=3):
            placa = placa+ letras[random.randint(0,25)]
            cont += 1 
        cont2 = 1
        while(cont2<=3):
            placa = placa + str(numeros[random.randint(0,9)])
            cont2 += 1 
        return(placa)

    elif(pais == "Francia"):
        cont = 1
        while(cont<=2):
            placa = placa+ letras[random.randint(0,25)]
            cont += 1 
        cont2 = 1
        while(cont2<=2):
            placa = placa + str(numeros[random.randint(0,9)])
            cont2 += 1 

        return(placa)


placas_francia = []
for i in range(20):
    placas_francia.append(gen_placa("Colombia"))

print(placas_francia)