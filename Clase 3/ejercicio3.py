#3. Dado N enteros positivos comprendidos entre 10000 y 99999 para cada uno de 
#ellos invierta la primera con su última cifra y preséntelo en pantalla junto al valor 
#original

n=int(input("Ingrese la cantidad de números a evaluar: "))

while n<=0:
    print("Ingreso la un valor invalido")
    print("Ingrese un valor mayor a cero")
    n=int(input("Ingrese la cantidad de números a evaluar: "))

c=0
while c<n:
    num=int(input("Ingrese un número comprendido entre 1.000 y 99.999: "))
    while num<10000 or num>99999:
        print("Ingreso la un valor invalido")
        num=int(input("Ingrese un número comprendido entre 1.000 y 99.999: "))

    inv=0
    uaux=0
    paux=0
    aux=num
    uaux=num%10
    paux=num//10000
    num= (num%10000)-uaux
    print(num)
    inv=(uaux*10**4)+paux+num
    print("El número ingresado fue: ",aux)
    print("Su invertido es: ", inv)
    print("La primera cifra del número ingresado es: ",paux)
    print("La última cifra de del número ingresado es: ",uaux)
    c=c+1
