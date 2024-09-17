#dado un número entero positivo determinar si es o no primo

n1= int (input("Ingrese un número "))

while n1<0 :
    print("El número ingresado no es correcto ")
    n1= int (input("Ingrese un número "))
if (n1%2==0 or n1%3==0 or n1%4==0 or n1%5==0 or n1%6==0 or n1 % 7 == 0 or n1%8==0  or n1 % 9 == 0) and (n1!=2 and n1!=3 and n1!=5 and n1 != 7) :
#( (n1%2==0 or n1%3==0 or n1%4==0 or n1%5==0 or n1%6==0 or n1%7==0 or n1%8==0 or n1%9==0 ) and (n1!=2 or n1!=3 or n1!=5 or n1!=7)):
    print("El numero ",n1, " ingresado no es primo ")
else:
    print("El número ingresado es primo")