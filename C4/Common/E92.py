


def primo(a):
    if a==2:
        return "es primo"
    
    for i in range(2,a):
        if a%i==0:

            return "no es primo"
        else:
            return "es primo"

print(primo(5))






