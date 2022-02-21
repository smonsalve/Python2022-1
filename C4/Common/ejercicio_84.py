def mediana(A,B,C):
    if A<B and B<C:
        return B
    if A>B and B>C:
        return B
    if B<A and A<C:  
        return A
    if B>A and A>C:
        return A
    if C<A and B<C:
        return C
    if C>A and B>C:
        return C

A = input("Valor de A: ")
B = input("Valor de B: ")
C = input("Valor de C: ")
print(mediana(A,B,C))