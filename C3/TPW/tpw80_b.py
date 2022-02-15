import random

promedio = 0 

for i in range(1,11,1):
    
    procesando = True
    contador = 0
    pasada = -1 # Cara, cara
    antepasada = -1 # -1, cara
    trasantepasada = 2 # -1, -1
    resultado = ""
 
    while(procesando):
        if(random.randint(0,1) == 0): resultado = "Cara"
        else: resultado = "Sello" 

        trasantepasada = antepasada
        antepasada = pasada
        pasada = resultado

        if((pasada == antepasada) and (antepasada == trasantepasada)):
            procesando = False    
        contador = contador + 1

    print(i, contador)

    promedio += contador  # promedio = promedio + contador
print("El promedio es: ", promedio/10)