#1. Dado un numero entero positivo N, presentar por pantalla un mensaje que 
# indique si dicho número es o no un numero primo

n =int (input("Ingrese un número"))

if n % 2==0 or n % 3==0 or n % 4==0 or n % 5==0 or n % 6==0 or n %7==0 or n % 2==0 or n % 2==0 or (n != 2 and  n != 3 and  n != 5 and  n != 7 and  n != 9):
    print ("El número ingresado no es primo")
else: 
    print ("El número ingresado es primo")

print ("Fin")
