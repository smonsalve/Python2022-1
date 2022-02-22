# contador = 0
# text = "Muchas gracias por su participación"
# palabra = ""

# for c in text:
#     if(contador%2==0):
#         palabra += (c.upper())
#     else:
#         palabra += (c.lower())
#     contador = contador + 1

# print(palabra)
# print(contador)
# print(len(text))

contador = 0
text = "Muchas gracias por su participación"
palabra = ""

while(contador < len(text)):
    c = text[contador]
    if(contador%2==0):
        palabra += (c.upper())
    else:
        palabra += (c.lower())
    contador = contador + 1

print(palabra)
#print(contador)
#print(len(text))
