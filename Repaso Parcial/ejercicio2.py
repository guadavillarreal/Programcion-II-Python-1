#dado n num enteros positivos diferentes,
# encuentra el mayor num par,
# en caso de no haber ingresado ninguno numero par al sistema debe decir "no se ingreso ningun num par"
#si se ingreso uno solo el sistema debe decir "Se ingreso un solo numero par no es posible det el mayor"

n=int(input("Ingrese la cantidad de números a evaluar "))
lista_pares=[]

while n<=0:
    print("Ingreso un número incorrect")
    n=int(input("Ingrese la cantidad de números a evaluar "))
c=0
while c<n:
    num=int(input("Ingrese un número entero positivo "))
    while num<=0:
        print("Ingreso un número incorrect")
        num=int(input("Ingrese un número entero positivo "))
    if num %2==0:
        while num in lista_pares:#pregunta si ya esta en la lista
            print("El número ya se encuentra en la lista debe ingresar uno distinto")
            num=int(input("Ingrese un número entero positivo "))
        lista_pares.append(num)#agrega al ultimo
    c=c+1

lista_pares.sort() #ordena de menor a mayor
if len(lista_pares)>0:#pregunta si el largo de la lista es menor a 0
    if len(lista_pares)>1:#pregunta si el largo de la lista es 
        print("El mayor número par ingresado es: ", lista_pares[-1])#muestra el ultimo elemento de la lista
    else:
        print("Se ingreso un solo numero par " , lista_pares," no es posible determinar el mayor")#muestra la lista
else:
    print("no se ingreso ningun num par")