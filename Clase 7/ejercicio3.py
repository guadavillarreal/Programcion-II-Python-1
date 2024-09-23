#3. Dado N número enteros, presentar por pantalla el menor número impar 
#ingresado, en caso de que no se hubiera ingresado por lo menos dos números
#impares distintos, presentar el mensaje correspondiente

n= int(input("Inrese la cantidad de número a evaluar"))
num=0 #numero ingresado
men = 100 #menor numero impar ingresado
c= 0 #contador de vueltas
cimp=2 #ver si es impar
imp=0 #impar
conti=0 #cantidad de impares ingresados

while c<n:
    num=int(input("Ingrese el número a evaluar "))
    while cimp<num:
        if num % cimp ==0:
            print("el numero no es impar")
        else:
            if num<men:
                men=num;
                conti=conti+1
        cimp=cimp+1
    c=c+1

if conti<1:
    print("La cantidad de números impares ingresados es menor a 2")

print("El menor número impar ingresado es: ", men)


