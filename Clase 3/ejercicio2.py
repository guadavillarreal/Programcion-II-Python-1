""" #2 Dado N enteros positivos, 
#determina cuantos son tales, que sus dos últimas 
#cifras son números primos.

n=int(input("Ingrese la cantidad de números a evaluar: "))
while n<0:
       print("El número ingresado no es valido")
       print("Ingrese un numero entero positivo")
       n=int(input("Ingrese la cantidad de números a evaluar: "))

contnum=0
aux=0
auxp=0
c=2
cv=0 #contador de cantidad de vueltas para evaluar un numero
num=int(input("Ingrese un número entero positivo: "))

while n>cv:
       while num<0: 
            print("El número ingresado es no es valido")
            num=int(input("Ingrese un número entero positivo: "))
       
       while num>0:
            aux=num
            num=num%100
            while c<num:
                    if num%c==0:
                        print("El número ingresado no es primo")
                    else:
                        print("El número ingresado es primo")
                        contnum=1
                    c=c+1

       cv=cv+1
       

 """

#2 Dado N enteros positivos, 
#determina cuantos son,tales que sus dos últimas 
#cifras son números primos.

n=int(input("Ingrese la cantidad de números a evaluar: "))
while n<0:
    print("Ingreso un número invalido")
    print("Ingrese un número entero positivo")
    n=int(input("Ingrese la cantidad de números a evaluar"))

cn=0 #contador de vueltas de numeros
contp=0
while cn<n:
    aux=0 #var para guardar las variables

    num=int(input("Ingrese un número a evaluar "))
    while num<0:
        print("Ingreso un valor invalido ")
        print("Ingrese un número entero positivo")
        num=int(input("Ingrese un número a evaluar "))

    num=num%100
    p=2 #comparador de primos
    primo=0
    while p<num:
        if num%p==0:
            primo=1

        p=p+1

    if primo <1:
       contp=contp+1
    cn=cn+1

print("La cantidad de números primos ingresados es: ",contp)


