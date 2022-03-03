f1 = open("tpw141.py")
a1 = f1.readlines()

f2 = open("tpw152.py")
a2 = f2.readlines()

todo = []
todo.extend(a1)
todo.extend(a2)

f3 = open("Mix.txt", 'w')
f3.writelines(todo)

f1.close()
f2.close()
f3.close()