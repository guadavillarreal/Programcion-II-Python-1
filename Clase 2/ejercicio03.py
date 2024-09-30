#dado un número entero positivo determinar si es o no primo

n1= int (input("Ingrese un número "))
p=2
b=0
while p<n1:
    if n1%p ==0:
        b+=1
    p+=1
    
if b>=1:
    print("El número ingresado no es primo")
else:
    print("El número ingresado es primo")
