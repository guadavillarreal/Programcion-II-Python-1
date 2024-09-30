#dado dos enteros 
# encuentre la suma de los números comprendidos entre ellos

n1 = int (input("Ingrese un número: "))
n2 = int (input("Ingrese otro número: "))
n3=0
suma=0

if n2<n1:
    n3=n1
    n1=n2
    n2=n3

for numero in range( n1+1 , n2):
    suma+=numero
print("La suma de los números comprendidos entre los números ingresados es: ", suma)
