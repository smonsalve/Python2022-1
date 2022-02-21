text=str(input("Ingrese su texto: "))
I=str("i ")
espacio=""
aparicion= text.count(I)
puntos=str(["!","?",":","."])
aparicion1=text.count(espacio)

if aparicion>=1:
    print("Texto corregido: ",text.replace(I,"I "))
elif aparicion1>=1:
        print("Texto corregido: ",text.capitalize())
    
#else aparicion, aparicion1<=0:
    #print("Tu texto no necesita correciones")