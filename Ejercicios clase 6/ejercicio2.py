#diseñar un algoritmo que presente
# por pantalla las 10 primeras tablas de muliplicar

n = 0
mul = 1
while mul <= 10:
    result = n * mul
    n= n +1
    mul = mul +1
    print ("{n} x *{mul} = *{result} ")

print("FIN")