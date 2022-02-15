def almacenar(**losargs):
    for (k,v) in losargs.items():
        print(f"{k}->{v}")


def main():
    almacenar(leche= "alpina", gasolina=["Corriente","Diesel"], edad = 35 )

if __name__ == "__main__":
    main()