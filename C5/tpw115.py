cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vocal = ["a","e","i","o","u"]

def isvocal(car):
    return(car in vocal)

p1 = input("ingrese una palabra: ")  #"papá"

for i in p1:
    print(i,isvocal(i))