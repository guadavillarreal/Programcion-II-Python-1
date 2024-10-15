#dado N enteros positivos determinar la suma de los valores que son numero primos

n=int(input("Ingrese la cantidad de número a evaluar: "))

while n<=0:
    print("Ingreso un valor invalido ingrese nuevamente")
    n=int(input("Ingrese la cantidad de número a evaluar: "))

c=0
primo=2
p=0
suma_primos=0
while c<n:
    num=int(input("Ingrese un número para evaluar "))
    while num<=0:
        print("Ingreso un valor invalido ingrese nuevamente")
        num=int(input("Ingrese un número para evaluar "))
    while primo<num:
        if num%primo==0:
            p=p+1

        primo=primo+1
    if p<1:
        print("El numero ingresado es primo")
        suma_primos=suma_primos+num
    c=c+1

print("La suma de los primos ingresados es: ", suma_primos)

