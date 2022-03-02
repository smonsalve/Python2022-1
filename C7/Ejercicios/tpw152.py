
# Write a program that reads a file containing information about chemical elements
# and stores it in one or more appropriate data structures. 
 
# Then your program should read and process input from the user. 
 
# If the user enters an integer then your program should display 
# the symbol and name of the element with the number of protons entered. 

# If the user enters a string then your program should display the number of protons for the element with that name or symbol. 
# Your program should display an appropriate error message if no element exists for the name, symbol or num- ber of protons entered. 

# Continue to read input from the user until a blank line is entered.


elementos = {}

f = open('elements.txt', 'r')    # ruta y nombre del archivo,  modo de lectura

for line in f.readlines():
    linea = (line.split(","))

    numero  = int(linea[0])
    simbolo  = linea[1]
    elemento = linea[2].rstrip()

    elementos[numero] = { "Elemento": elemento, "simbolo": simbolo}

f.close() 

# print(elementos)

for k,v in elementos.items():        
    print(f"{k} -> {v}")

