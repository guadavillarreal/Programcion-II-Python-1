#dado dos enteros 
# encuentre la suma de los números comprendidos entre ellos
#FUNCIONA PERO NO GUARDA EL VALOR DEL PRIMER NUMERO INGRESADO

n1 = int (input("Ingrese un número: "))
n2 = int (input("Ingrese otro número: "))
n3 = 0
n4 = n2

while n1 & n2 <0:
    if n1>0:
        print("El segundo numero ingresado no es valido")
        print("Ingrese un dato valido")
        n2 = int (input("Ingrese otro número: "))
    else:
        print("El primer número ingresado no es valido")
        print("Ingrese un número valido")
        n1 = int (input("Ingrese un número: "))

if n1<n2:
    while n1<(n2-1) : 
        n1 = n1+1
        n3 = n3 +n1
##si n1 > n2
else:
    n4=n1
    n1=n2
    n2=n4
    while n1<(n2-1) : 
        n1 = n1+1
        n3 = n3 +n1
print("El primer numero ingresado es: ", n1)
print ("La suma de los numeros comprendidos entre ellos es: ",n3)
print (n3)
print ("El segundo numero ingresado es:{n2}")

