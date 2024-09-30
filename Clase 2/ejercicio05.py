#Dado N cifras construye con ellos un numero compuesto

n=int(input("Ingrese la cantidad de cifras del número compuesto a evaluar "))
numeroCompuesto=""
p=0
for i in range(n):
    p=i+1
    cifra=int(input("Ingrese una cifra: "))
    numeroCompuesto+= str(cifra)

numeroCompuesto=int(numeroCompuesto)
print(numeroCompuesto)