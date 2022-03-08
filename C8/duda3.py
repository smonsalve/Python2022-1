a = ["h","o","l","a","aguacate",4,"l","o",7]

def pos_elem(lista,elemento):
    indice = None
    cont = 0
    list_pos = []
    for i in lista:
        if lista[cont] == elemento:
            indice = cont
            list_pos.append(cont)
        cont = cont + 1
    return list_pos




print(pos_elem(a,input("ingrese elemento: ")))


# print("aguacate"=="aguacate")