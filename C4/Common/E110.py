lista=[]

def perfecto(a): 
    suma=0  
    for i in range(1,a):
        if a%i==0:
            lista.append(i)
            suma=suma+i
        
    if suma==a:
        return True
    else:
        return False

lista_perfectos=[]
for i in range(10000):
    if perfecto(i):
        lista_perfectos.append(i)

print(lista_perfectos)


