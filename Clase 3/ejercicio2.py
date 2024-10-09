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


