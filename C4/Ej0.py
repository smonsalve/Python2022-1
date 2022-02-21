# Listas!!! :D

https://docs.python.org/3/tutorial/datastructures.html

# Objetivos de Clase

# * Crear una variable que contenga una lista de valores

milista = [1,2,3,4,5]
# print(milista)

# * Modificar una lista añadiendo, insertando, actualizando y eliminando elementos * Buscar un valor en una lista

# milista.append(6)
# print(milista)

# * Mostrar algunos o todos los valores de una lista

# for i in milista:
#     print(i)

# * Escribir una función que tome una lista como parámetro
# * Escribir una función que devuelva una lista como resultado

def suma1(unalista):
    otralista = []

    for i in range(len(unalista)):
        print(i)
        otralista[i] = unalista[i]
    return otralista

print(suma1(milista))


# Slices
# Ordenar Listas
# append

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.count('apple')
# # 2
# fruits.count('tangerine')
# # 0
# fruits.index('banana')
# # 3
# fruits.index('banana', 4)  # Find next banana starting a position 4
# # 6
# fruits.reverse()
# fruits
# # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# fruits.append('grape')
# fruits
# # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# fruits.sort()
# fruits
# # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# fruits.pop()
# # 'pear'