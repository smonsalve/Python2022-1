# Mayusculas, minusculas, titulos...

texto1 = "Me encanta este curso de Python!"
texto1.capitalize()


texto2 = "Me encanta este curso de Python!"
texto2.upper()


texto3 = "ME ENCANTA ESTE CURSO DE PYTHON!"
texto3.lower()

texto4 = "ME ENCANTA ESTE CURSO DE PYTHON!"
texto4.isupper()


texto5 = "ME ENCANTA ESTE CURSO DE PYTHON!"
texto5.islower()

#Isnumeric, Isalpha, Isalnum


texto6 = "Python"
print(texto6.isnumeric())
#False
print(texto6.isalpha())
#True
print(texto6.isalnum())
#True


texto7 = "2022"
print(texto7.isnumeric())
True
print(texto7.isalpha())
False
print(texto7.isalnum())
True


texto8 = "Python2022"
print(texto8.isnumeric())
False
print(texto8.isalpha())
False
print(texto8.isalnum())
True


texto9 = "Python-2022"
print(texto9.isnumeric())
False
print(texto9.isalpha())
False
print(texto9.isalnum())
False


texto10 = "Hoy es un día lluvioso"
texto10.count("e")


texto11 = "Data science"
texto11.find("a")
#1

texto12.find("a", 2)
#3
texto12.find("sci")
#

#Startswith
mylist = ["John", "Jane", "Emily", "Jack", "Ashley"]
j_list = [name for name in mylist if name.startswith("J")]
j_list
['John', 'Jane', 'Jack']

#Endswith
texto13 = "Python"
texto13.endswith("n")
#True
texto14 = "Python"
texto14.startswith("p")
#False
texto14.startswith("P")
#True


#Replace
texto15 = "Python is awesome!"
texto15 = texto15.replace("Python", "Data science")
print(texto15)
'Data science is awesome!'


#Split
texto16 = 'Data science is awesome!'
texto16.split()
#['Data', 'science', 'is', 'awesome!']


#Partition

texto17 = "Python is awesome!"
texto17.partition("is")
('Python ', 'is', ' awesome!')

texto18 = "Python is awesome and it is easy to learn."
texto18.partition("and")
('Python is awesome ', 'and', ' it is easy to learn.')


texto19 = "Python and data science and machine learning"
texto19.partition("and")
('Python ', 'and', ' data science and machine learning')


texto20 = "Python and data science and machine learning"
texto20.split("and", 1)
['Python ', ' data science and machine learning']



#join
mylist = ["Jane", "John", "Matt", "James"]
"-".join(mylist)
#'Jane-John-Matt-James'


mytuple = ("Caracteres, Strings", "Listas")
" y ".join(mytuple)




# Basado en el articulo:
#https://towardsdatascience.com/15-must-know-python-string-methods-64a4f554941b