#Dado un número entero positivo no múltiplo de 10 presente
# en pantalla el valor dado y su invertido

n1 = int(input("Ingrese un número entero positivo no multiplo de 10: "))

while n1<=0 or n1%10==0:
    print("ingreso al bucle")
    print ("Ingrese un número valido")
    n1 = int(input("Ingrese un número entero positivo no multiplo de 10: "))
inv = 0
aux=n1
c=0
while n1>0:
    inv= inv*10+(n1%10)#0+(37%10)=0+7  · 7x10+(3%10)=70+3=73
    n1=n1//10          #37:10=3        · 3:10=0


print("El número ingresado es: ",aux)
print("Su invertido es: ", inv)


