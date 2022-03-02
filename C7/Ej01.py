# Escritura
f = open("elements.txt", 'a')

lineas = []
for i in range(1,101):
    lineas.append(f"{i} \n")

f.writelines(lineas)
f.close()
