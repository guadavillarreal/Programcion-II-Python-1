#Diseñar un algoritmo que permita ingresar una cantidad de Megabytes y 
# presentar  por pantalla su equivalente gibabyte, kilobytes, bytes y bits

mb = float(input("Ingrese la cantidad de Megabytes a evaluar "))
gb = mb/1024
kb= mb * 1024
by= kb *1024
bits = by*8

print(f"La canidad de Megabytes dada es: {mb}")
print(f"Equivale a {gb} Gigabyte, {kb} Kilobyte, {by} byte y {bits} Bits")