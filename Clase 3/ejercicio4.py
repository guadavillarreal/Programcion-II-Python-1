#4. Dada la fecha de nacimiento de una persona en formato DD/MM/AAAA y la fecha 
# actual en el mismo formato indique su edad. 
import datetime

edad=0
hoy=datetime.date.today()#entrega la fecha actual
diaA=hoy.day #guardo en una var solo el dia
mesA=hoy.month #solo el mes
anioA=hoy.year #solo el año

print("Ingrese su fecha de nacimiento")
dia=int(input("Ingrese el dia "))
mes=int(input("Ingrese el mes "))
anio=int(input("Ingese el año "))

if mes<mesA:
    edad=anioA-anio
else:
    if mes==mesA:
        if dia<=diaA:
            edad=anioA-anio
        else:
            edad=anioA-(anio+1)
    else:
        edad=anioA-(anio+1)


print("Su edad es: ",edad)