a = [1,2,3,None,4,5]

cont = 0 
while(cont < len(a)):
    if a[cont]==None:
        break
    cont = cont + 1
    print(cont)