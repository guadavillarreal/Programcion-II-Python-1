#1. Dado un numero entero positivo N, presentar por pantalla un mensaje que 
# indique si dicho número es o no un numero primo

n =int (input("Ingrese un número "))
x= 2
b=True

while x<n:
    if n % x==0 :
        b= True
    else: 
        b= False
    x=x+1

if b == True:
    print("El número ingresado no es primo")
else:
    print("El número ingresado es primo")
print ("Fin")
