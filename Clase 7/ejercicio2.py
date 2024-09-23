# 2. Ingresar N números enteros,
#  presentar por pantalla el valor del mayor numero ingresado y
#  la posición en que se ingresó (tener en cuenta la posibilidad de que 
# todos los números ingresados pueden ser igual)

n = int (input("Ingrese la cantidad de núeros enteros a evaluar: "))
p=0
may = 0
men = 1
c=0

while c<n:
    num = int (input("Ingrese un número "))
    if num > may:
        may = num
        p = c+1
    else:
        if num < men :
            men = num
    c=c+1

print("El menor número ingresado es: ", men)
print("El mayor número ingresado es: ", may)
print("La posición en la que se lo ingreso es: ", p)
