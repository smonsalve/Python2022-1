f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # Go to the 6th byte in the file
5
f.read(1)
b'5'
f.seek(-3, 2)  # Go to the 3rd byte before the end
13
f.read(1)
b'd'


with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')



# f.readline()
# for line in f:
#     print(line, end='')


# # lectura
# f.readlines()

# # Escritura
# f.write('Esto es una prueba\n')