#4. Dados N números, presentar por pantalla la cantidad de series crecientes de 
#números cargados.

n=int(input("Ingrese la cantidad de números a evaluar "))
c=0
while c<n:
    num=int(input("Ingrese un número "))
    p=0
    while p<n:
        num=num+1
        print(num)
        p=p+1
    c=c+1
