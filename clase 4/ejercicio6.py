#escribir un programa para convertir una medida dada en metros a sus 
# equivalentes en decimetros , centimetros y milimetros.Presentar por pantalla 
# las cuatro magnitudes con sus respectivas unidades

met=int(input("Ingrese la medida en metros"))

d = met*10
c = met*100
m = met *1000

print(f"La medida dada en metros es: ={met}")
print(f"La medida dada en decimetros es: ={d} ")
print(f"La medida dada en centimetros es: ={c} ")
print(f"La medida dada en milimetros es: ={m} ")
print(f"La medida dada en metros {met} son {d} decimetros, {c} centimetros, {d} decimetros")