def taximetro(distancia):
    """
    Esta funcion calcula cuanto vale el taxi, recibe una distancia en kilometros retorna el valor del taxi
    """

    BASE = 4 #Este es el banderazo
    recorrido = 140 # cada cuantos metros cobro la tarifa
    tarifa = 0.25 # El valor por unidad de metros recorrido
    distancia_en_metros = distancia * 1000 # Cambiando parametro distancia en km a metros
    resultado = BASE + (distancia_en_metros//recorrido)*tarifa # Calculando el resultado

    return resultado
    
distancia_total = float(input("Cual es la distancia que viajar? "))

print("su tarifa sería: ", taximetro(distancia_total))



