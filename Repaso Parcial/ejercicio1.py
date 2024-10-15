#ingrese numeros enteros positivos distintos de 0 
#y luego ingrese 0 para sumar los ingresados

num= int (input("Ingrese un número entero positivo: "))
suma=0

while num!=0 :
    while num<0:
        print("Ingreso un número invalido")
        num= int (input("Ingrese un número entero positivo: "))
    suma=suma+num
    num= int (input("Ingrese un número entero positivo: "))
print("La suma de los números ingresados es: ",suma)
        