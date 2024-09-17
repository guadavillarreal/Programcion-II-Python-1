#dado el radio de un circulo presentar por pantlla
# el diametro, el perimetro y el area del circulo

r=float(input("Ingrese el radio del circulo: "))

p= 2*r*3.14
d = 2*r
a = 2*3.14*r**2

print("El diametro es: ", d , " El perimetro es: " ,p,  " El área es: ", a)
print( f"El diametro es: *{d} ,  El perimetro es: ={p}  El área es: ={a} ")