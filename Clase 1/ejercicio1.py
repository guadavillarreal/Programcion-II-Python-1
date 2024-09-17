# hacer ejercicios de la clase 3

# # dado un numero entero positivo no multiplo de 10 
# presente en pantlla el valor dado y su invertido

aux, cc , r ,i = int 
n1= int (input("Ingrese un número que no sea muliplo de 10 "))
aux = n1 
while(0<cc):
    cc=cc+1
    aux = aux // 10

aux =n1
while(0<aux):
    r=aux % 10 
    aux = aux // 10 
    i =i +r  * 10^(cc-1)
    cc = cc-1 

print (" El número ingresado es: ", n1 )
print (" El inverso del número ingresado es: ", i )