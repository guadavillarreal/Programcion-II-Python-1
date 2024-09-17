#Dado N cifras construye con ellos un numero compuesto
#no concatena como tiene que ser lo hace con comas el profe lo resolvio en 
# pizarra ver su resolucion porq creeria que le falta un = en el primer while
n =int (input("Ingrese la cantidad de cifras a ingresar: "))
c=0
n99=0

while c<n :
    n1 = int (input("Ingrese la primera cifra "))
    n99 = n99, n1
    c = c +1

print(n99)
print (n1)