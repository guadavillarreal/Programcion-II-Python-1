#3. Presentar por pantalla los N primeros números de la seria de Fibonacci

n=int(input("Ingrese la cantidad de posiciones de figonacci que desea conocer: "))
c=0
ca=1
num=0

print(num)
print(ca)
print(ca)

while c<n:      # 0<3   1<3     2
    if c<1:
        ca=1
    else:
        ca=c
    c=c+1       #=0+1   1+1     3
    num=ca+c
    print(num)

