# Retornar la cantidad de veces que se repite el último caracter
n = input("Ingrese una palabra: ").lower()
n1 = n[-1]

count = 0
for i in n:
    if i == n1:
        count += 1

print(f"La cantidad de veces que se repite el ultimo caracter es: {count}")
