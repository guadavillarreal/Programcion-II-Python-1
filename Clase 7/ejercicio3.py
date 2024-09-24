#3. Dado N número enteros, presentar por pantalla el menor número impar 
#ingresado, en caso de que no se hubiera ingresado por lo menos dos números
#impares distintos, presentar el mensaje correspondiente
"""falta la comparativa de los numeros anteriores
"""
n= int(input("Ingrese la cantidad de números a evaluar "))
c=0#contador de vueltas de num
ci=0
while c<n:
    num=int(input("Ingrese un número "))
    p=0 #posicion
    if num % 2 ==0:
        print("El número ingresado es par")
    else:
        print("EL número ingresado es impar")
        ci=ci+1            
    c=c+1

if ci>=2:
    print("Se ingresaron ",ci," números impares")
else:
    print("Se ingresaron menos de 2 números impares")