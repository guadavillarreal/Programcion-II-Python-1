#diseñar un algoritmo que presente
# por pantalla las 10 primeras tablas de muliplicar

n = 0
mul = 1

while n<12:
    n= n +1
    while mul <= 12:
        result = n * mul
        print (mul," x ",n," = ",result)
        mul = mul +1
    print(" ")
    mul=1
print("FIN") 

