# https://docs.python.org/3/tutorial/inputoutput.html

# Lectura
f = open("elements.txt", 'r')

#print(f.readlines())
# print(len(f.readlines()))

for line in f.readlines():
    print(line.rstrip("\n"), end=", ")

f.close()

