# Ej 80: Simulacion de Moneda
# Cuantas veces hay que lanzar una moneda antes de que salga 
# el mismo lado durante 3 veces seguidas. 
# Cuantos lanzamientos se requieren en promedio.
# Su programa debe lanzar una moneda 
# hasta lanzar tres lanzamientos seguidos que den o cara o sello
#  Display an H each time the outcome is heads, and a T each time the outcome is tails, with all of the outcomes shown on the same line. 
# Then display the number of flips needed to reach 3 consecutive flips with the same outcome. When your program is run it should perform the simulation 10 times and report the average number of flips needed.
#  Sample output is shown below:


#Numeros Aleatorios

import random

procesando = True
contador = 0

pasada = -1 # Cara, cara
antepasada = -1 # -1, cara
trasantepasada = 2 # -1, -1

resultado = ""

while(procesando):
    if((pasada == antepasada) and (antepasada == trasantepasada)):
        procesando = False    
    contador = contador + 1

    if(random.randint(0,1) == 0): 
        resultado = "Cara"
    else: 
        resultado = "Sello"

    print(resultado)
    trasantepasada = antepasada
    antepasada = pasada
    pasada = resultado

print(contador)