#Dado N números determinar el mayor y menor de ellos

n = int(input("Ingrese la cantidad de números a evaluar: "))
c =0
n0=1
n9 =0
while c <n:
    n1 = int (input("Ingrese un número para evaluar: "))
    if n1 < n0 : 
        n0=n1
    else:
        if n1 > n9:
            n9=n1
    c=c+1

print("La comparación de los números fue de: ",n)
print( "El menor número ingresado es: ", n0)
print("El mayor número ingresado es: ", n9)