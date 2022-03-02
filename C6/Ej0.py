from titleprint import title_print
# Crear diccionario vacío
# Crear diccionario con elementos
# Agregar Elementos
# Leer Elemento
# Modificar Elementos

# lista = [0,0,0,0,0]
# lista[3] = -1
# print(lista)

# a,b,c,d = 1,2,3,4
# print(d,c,b,a)

# diccionario_vacio = {}
# diccionario_vacio[1111111111] = "Juan Pablo Aguilar"
# diccionario_vacio[2222222] = "Sergio Monsalve"

# print(diccionario_vacio)

#id_estudiantes = {"Antonia":1020304050, "Bernardo":1020304051, "Carlos": 1020304052, "Daniela":1020304053, "Esteban":1020304054  }
#print(id_estudiantes)
# Clave = "Antonia"
# print(id_estudiantes["Carlos"])

# ###############################################################################

# variable = "False"

# if(variable):
#     print("True")
# else:
#     print("False")



# ###############################################################################

# title_print("Diccionario Vacío")


# if not diccionario_vacio:
#     print(f"Sin elementos: longitud -> {len(diccionario_vacio)}")
# else:
#     print(f"Con elementos: longitud -> {len(diccionario_vacio)}")




# ###############################################################################

# title_print("Diccionario Vacío")
# diccionario_vacio["uno"] = "Sergio"
# if not diccionario_vacio:
#     print(f"Sin elementos: longitud -> {len(diccionario_vacio)}")
# else:
#     print(f"Con elementos: longitud -> {len(diccionario_vacio)}")

# # ###############################################################################
# title_print("Para cada llave imprima")

# lista_nombres = list(id_estudiantes.keys())
# print("Bernardos" not in lista_nombres)



# for j in id_estudiantes.keys():
#     print(j)





# # ###############################################################################
# title_print("Para cada valor imprima")

# for i in id_estudiantes.values():
#     print(i)





# # ###############################################################################
#title_print("Para cada llave y Valor imprima")

# print(id_estudiantes.items())

# for key, value in id_estudiantes.items():
#     print(f"{key} -> {value}")
#     #print("llave: " + key + " valor: " + str(value))

# for tupla in id_estudiantes.items():
#     print(f"{tupla[0]} -> {tupla[1]}")

id_estudiantes = {"Antonia":1020304050, "Bernardo":1020304051, "Carlos": 1020304052, "Daniela":1020304053, "Esteban":1020304054  }
# for a,b in id_estudiantes.items():
#     print(f"{a} -> {b}")


# # ###############################################################################
title_print("Agregar un nuevo elemento")

id_estudiantes["Zulaima"] = 1020304055

for key, value in id_estudiantes.items():
    print(f"{key} -> {value}")





# print("Hola", end =" ")
# print("", end =" ")
# print("Diego", end =" ")

# print("Hola")
# print()
# print("Diego")