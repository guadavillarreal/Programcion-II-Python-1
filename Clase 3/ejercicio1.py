#Dado un número entero positivo no múltiplo de 10 presente
#  en pantalla el valor dado y su invertido

n1 = int(input("Ingrese un número entero positivo no multiplo de 10:"))

while n1<= 0 and n1 %10 ==0:
    print ("Ingrese un número valido")
    n1 = int(input("Ingrese un número entero positivo no multiplo de 10:"))


