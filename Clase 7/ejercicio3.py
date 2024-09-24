#3. Dado N número enteros, presentar por pantalla el menor número impar 
#ingresado, en caso de que no se hubiera ingresado por lo menos dos números
#impares distintos, presentar el mensaje correspondiente

n= int(input("Ingrese la cantidad de números a evaluar "))
c=0 #contador de vueltas a evaluar
cp=0 #contador de primos
num=0 
cimp=0
mnpri=1
while c<n:
    num= int(input("Ingrese un número "))
    while cimp<num:
        if num % cimpr == 0:
            print("El número ingreso es par ")
            cimp=num
        else:
            if num<mnpri:
                mnpri=num
                cp=cp+1
        cimp = cimp+1
    c=c+1

if cp>1:
    print("Se ingreso por lo menos dos números primos ")
else:
    print ("Se ingreso menos de dos números primos")

print("El menor número primo ingresado es ",mnpri)