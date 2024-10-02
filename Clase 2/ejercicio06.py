#Dado N números enteros positivos de cualquier longitud 
# construya con ellos un número compuesto
#el profe creo que lo resolvio en clases verlo

n=0
while n<=0:
   n=int(input("Ingrese la cantidad de números para trabajar "))
   
cont=0
while cont<n:
    num=int(input("Ingrese un número entero positivo "))
    if cont==0:
        nc=num
    else:
         aux=num 
         cc=0
         while 0<aux:
            cc=cc+1 
            aux=aux//10
         nc=nc*(10**cc)+num
    cont=cont+1

print("El número compuesto creado es: ",nc)
