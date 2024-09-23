#1. Dado un numero entero positivo N, presentar por pantalla un mensaje que 
# indique si dicho número es o no un numero primo

n =int (input("Ingrese un número "))
x= 2
b=0
mult=0

while x<n:
    if n % x==0 :
        b= 1
    else: 
        b= 0
    x=x+1
    if b == 1:
        mult = mult+1

if mult>0:
    print("El número ingresado no es primo")
else:
    print("El número ingresado es primo")
print ("Fin")
