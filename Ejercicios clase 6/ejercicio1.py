#presentar por pantala los siete primeros numeros enteros positivos
n= int (input ("Ingrese un número "))
 
cont = 0
while cont <7:
    if n>=1:
        print(n)
        cont= cont +1
    n=int (input ("Ingrese un número "))

print("FIN")